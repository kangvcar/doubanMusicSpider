# 豆瓣音乐爬虫项目

## 项目描述
该项目是一个基于Scrapy框架的豆瓣音乐爬虫，用于爬取豆瓣音乐TOP250的音乐信息以及这些音乐的评论信息。爬虫分为两个部分：

1. **豆瓣音乐信息爬虫 (`douban_music_spider`)**: 爬取豆瓣音乐TOP250的音乐的基本信息，并保存到`output/music_info.csv`文件中。同时，将音乐的ID保存到`output/music_ids.txt`文件中。
2. **豆瓣音乐评论爬虫 (`douban_music_comment`)**: 根据音乐ID爬取对应音乐的所有评论信息，并保存到`output/music_comments.csv`文件中。

## 环境要求

- Python 3.6+
- Scrapy 2.0+

## 项目结构
```
douban_music/
│   scrapy.cfg
│   README.md
│   requirements.txt
│
├───douban_music/
│   │   items.py
│   │   middlewares.py
│   │   pipelines.py
│   │   settings.py
│   │   __init__.py
│   │
│   └───spiders/
│           douban_music_comment_spider.py
│           douban_music_spider.py
│           __init__.py
│
└───output/
        music_comments.csv
        music_ids.txt
        music_info.csv
```

## 如何使用

### 安装依赖
首先，确保你已经安装了Python和Scrapy。然后，运行以下命令来安装所需的依赖：

```bash
pip install -r requirements.txt
```

### 运行爬虫

1. 运行豆瓣音乐信息爬虫：

```bash
scrapy crawl douban_music_spider
```

该命令会爬取豆瓣音乐TOP250的音乐信息，并将结果保存到`output/music_info.csv`文件中。同时，音乐的ID会被保存到`output/music_ids.txt`文件中。

2. 运行豆瓣音乐评论爬虫：

```bash
scrapy crawl douban_music_comment
```

该命令会根据`output/music_ids.txt`文件中的音乐ID，爬取这些音乐的所有评论信息，并将结果保存到`output/music_comments.csv`文件中。

## 输出文件说明

- `music_info.csv`: 保存了豆瓣音乐TOP250的音乐基本信息。包含的字段有：
  - `title`: 音乐标题
  - `performer`: 演出者
  - `release_date`: 发行日期
  - `album_type`: 专辑类型
  - `medium`: 媒介
  - `genre`: 流派
  - `rating`: 评分
  - `rating_count`: 评分人数
  - `cover_link`: 封面链接
  - `music_id`: 音乐ID

- `music_ids.txt`: 保存了豆瓣音乐TOP250的音乐ID。

- `music_comments.csv`: 保存了根据音乐ID爬取的所有评论信息。包含的字段有：
  - `username`: 用户名
  - `rating`: 评分
  - `comment_time`: 评论时间
  - `useful_count`: 有用数量
  - `content`: 评论内容
  - `music_title`: 音乐标题

## 注意事项

- 请遵守豆瓣的爬虫使用协议，不要对豆瓣的服务器造成过大的压力。
- 请确保在运行爬虫前，你有足够的磁盘空间来保存爬取的数据。
- 项目中的代码仅供学习和研究目的使用，请勿用于任何商业用途。

---

🎉 祝你使用愉快！ 🎉