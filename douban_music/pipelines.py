# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from douban_music.items import DoubanMusicItem, DoubanMusicCommentItem
import csv
import os

if not os.path.exists('output'):
    os.makedirs('output')

class DoubanMusicPipeline:
    def process_item(self, item, spider):
        return item


# In pipelines.py

class SaveMusicIDPipeline:
    def open_spider(self, spider):
        self.file = open('output/music_ids.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item, DoubanMusicItem):  # Ensure we are processing the correct item type
            if 'music_id' in item:
                self.file.write(item['music_id'] + '\n')
        return item

    def close_spider(self, spider):
        self.file.close()


class CsvExporterPipeline:
    def __init__(self):
        self.file = None
        self.writer = None

    def open_spider(self, spider):
        self.file = open('output/music.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        # Write header
        self.writer.writerow(['music_id', 'title', 'performer', 'release_date', 'album_type', 'medium', 'genre', 'rating', 'rating_count', 'cover_link'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, DoubanMusicItem):  # Ensure we are processing the correct item type
            self.writer.writerow([item['music_id'], item['title'], item['performer'], item['release_date'], item['album_type'], item['medium'], item['genre'], item['rating'], item['rating_count'], item['cover_link']])
        return item


class CsvCommentExporterPipeline:
    def __init__(self):
        self.file = None
        self.writer = None

    def open_spider(self, spider):
        self.file = open('output/comments_output.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        # Write header for comments
        self.writer.writerow(['music_title', 'username', 'rating', 'comment_time', 'useful_count', 'content'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, DoubanMusicCommentItem):
            self.writer.writerow([item['music_title'], item['username'], item['rating'], item['comment_time'], item['useful_count'], item['content']])
        return item
