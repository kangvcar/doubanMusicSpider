import scrapy
from douban_music.items import DoubanMusicCommentItem


class DoubanMusicTop250IDSpider(scrapy.Spider):
    name = 'douban_music_top250_id_comments'
    start_urls = ['https://music.douban.com/top250']

    def parse(self, response):
        # Extract music IDs from the Top250 list
        music_ids = response.css('.pl2 a::attr(href)').re(r'subject/(\d+)/')
        for mid in music_ids:
            comments_url = f'https://music.douban.com/subject/{mid}/comments/?start=0&limit=20&status=P&sort=new_score&comments_only=1'
            yield scrapy.Request(url=comments_url, callback=self.parse_comments)

        # Pagination for Top250 list
        next_page = response.css('.paginator .next a::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_comments(self, response):
        # Extract the HTML content from the JSON data
        html_content = response.json()['html']
        selector = scrapy.Selector(text=html_content)

        for comment in selector.css('li.comment-item'):
            item = DoubanMusicCommentItem()
            item['username'] = comment.css('.comment-info a::text').get()
            item['rating'] = comment.css('.comment-info span.rating::attr(title)').get()
            item['comment_time'] = comment.css('.comment-info span.comment-time::text').get().strip()
            item['useful_count'] = comment.css('span.vote-count::text').get()
            item['content'] = comment.css('p.comment-content span.short::text').get()
            yield item
