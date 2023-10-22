# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMusicItem(scrapy.Item):
    music_id = scrapy.Field()    # 音乐ID
    title = scrapy.Field()       # 歌曲名称
    cover_link = scrapy.Field()  # 封面链接
    performer = scrapy.Field()   # 表演者
    release_date = scrapy.Field()  # 发行时间
    album_type = scrapy.Field()   # 专辑类型
    medium = scrapy.Field()      # 介质
    genre = scrapy.Field()       # 流派
    rating = scrapy.Field()      # 豆瓣评分
    rating_count = scrapy.Field()  # 评价人数


class DoubanMusicCommentItem(scrapy.Item):
    music_title = scrapy.Field()  # 歌曲名称
    username = scrapy.Field()    # 用户名
    rating = scrapy.Field()      # 评分
    comment_time = scrapy.Field()  # 评论时间
    useful_count = scrapy.Field()  # 有用数量
    content = scrapy.Field()     # 评论内容
