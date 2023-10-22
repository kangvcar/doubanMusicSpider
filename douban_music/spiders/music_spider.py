import scrapy
from douban_music.items import DoubanMusicItem


class DoubanMusicSpider(scrapy.Spider):
    name = 'douban_music'
    start_urls = ['https://music.douban.com/top250']

    def parse(self, response):
        for music_block in response.css('table'):
            item = DoubanMusicItem()

            # Extract music ID from the link
            music_link = music_block.css('div.pl2 > a::attr(href)').get()
            item["music_id"] = music_link.split('/')[-2] if music_link else None

            # Extract title and performer
            title_link = music_block.css('div.pl2 > a')
            # item["title"] = title_link.css('::text').get().split('\n')[0].strip()
            title_text = title_link.xpath('normalize-space(.)').get()
            if title_text:
                item["title"] = title_text
            cover_link = music_block.css('img::attr(src)').get()
            if cover_link:
                item["cover_link"] = cover_link
            performer_title = title_link.css('::attr(title)').get()
            if performer_title and ' - ' in performer_title:
                item["performer"] = performer_title.split(' - ')[0]

            # Extract release date, album type, medium, and genre
            details = music_block.css('p.pl::text').get().split(' / ')
            item["performer"] = details[0]
            item["release_date"] = details[1]
            item["album_type"] = details[2]
            item["medium"] = details[3]
            item["genre"] = details[4] if len(details) > 4 else None

            # Extract rating
            item["rating"] = music_block.css('span.rating_nums::text').get()

            # Extract rating count
            count_text = music_block.css('span.pl::text').get()
            item["rating_count"] = int(count_text.split('(')[1].split('人')[0].replace(',', ''))
            print(item)
            yield item

        # Handle pagination using the "next" link
        next_page = response.css('div.paginator span.next a::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

