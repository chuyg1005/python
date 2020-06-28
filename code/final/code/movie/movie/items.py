# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # table = scrapy.Field()  # 表名
    entity = scrapy.Field()  # movie or comment
    movie = scrapy.Field()  # 电影名
    year = scrapy.Field()  # 发行日期
    rank = scrapy.Field()  # 排名
    genre = scrapy.Field()  # 类型
    length = scrapy.Field()  # 片长
    score = scrapy.Field()  # 评分
    # language = scrapy.Field()  # 语言
    img_url = scrapy.Field()  # 图片路径
    # desc = scrapy.Field()  # 一句话评论
    director = scrapy.Field()  # 导演
    actor = scrapy.Field()  # 主演
    country = scrapy.Field()  # 国家
    comment = scrapy.Field()  # 评论
