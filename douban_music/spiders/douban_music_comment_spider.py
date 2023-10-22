import scrapy
from douban_music.items import DoubanMusicCommentItem

class DoubanMusicCommentSpider(scrapy.Spider):
    name = 'douban_music_comment'

    # Step 1: Generate start_urls from music_ids.txt
    with open('music_ids.txt', 'r', encoding='utf-8') as f:
        music_ids = [line.strip() for line in f.readlines()]
    print(music_ids)
    start_urls = [f'https://music.douban.com/subject/{music_id}/' for music_id in music_ids]

    def parse(self, response):
        self.logger.info(f"Parsing: {response.url}")

        # Extract music name
        music_title = response.css('h1 span::text').get()
        print(music_title)

        # Construct the initial comments URL
        music_id = response.url.split("/")[4]
        comments_url = f'https://music.douban.com/subject/{music_id}/comments/?start=0&limit=20&status=P&sort=new_score&comments_only=1'
        print(comments_url)
        yield scrapy.Request(url=comments_url, callback=self.parse_comments, meta={'music_title': music_title})

    def parse_comments(self, response):
        # Extract the HTML content from the JSON data
        html_content = response.json()['html']
        selector = scrapy.Selector(text=html_content)
        music_title = response.meta['music_title']

        for comment in selector.css('li.comment-item'):
            item = DoubanMusicCommentItem()
            item['music_title'] = music_title
            item['username'] = comment.css('.comment-info a::text').get()
            item['rating'] = comment.css('.comment-info span.rating::attr(title)').get()
            item['comment_time'] = comment.css('.comment-info span.comment-time::text').get().strip()
            item['useful_count'] = comment.css('span.vote-count::text').get()
            item['content'] = comment.css('p.comment-content span.short::text').get()
            yield item

        # Handle pagination
        # Step 2: Update the base_url construction
        music_id = response.url.split("/")[4]
        base_url = f"https://music.douban.com/subject/{music_id}/comments/"
        next_page = selector.css('#paginator a[data-page="next"]::attr(href)').get()
        if next_page:
            next_page_url = base_url + next_page + '&comments_only=1'
            yield scrapy.Request(url=next_page_url, callback=self.parse_comments, meta={'music_title': music_title})
