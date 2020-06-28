# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.response import Response
from scrapy.selector import SelectorList
import re


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    # start_urls = ['http://movie.douban.com/subject/1292722/comments?status=P']

    rules = (
        Rule(LinkExtractor(allow=r'/top250.*'), callback=None, follow=True),
        Rule(LinkExtractor(allow=r'/subject/\d+/$'), callback='parse_movie', follow=True),
        Rule(LinkExtractor(allow=r'/subject/\d+/comments\?status=P$'), callback='parse_comment', follow=False),
    )

    def parse_movie(self, response: Response):
        item = {}
        item['entity'] = 'movie'
        item['movie'] = response.xpath('//h1/span[@property="v:itemreviewed"]/text()').get().split()[0]
        item['year'] = response.xpath('//h1/span[@class="year"]/text()').get()[1:-1]
        item['score'] = response.xpath('//strong/text()').get()
        item['director'] = response.xpath('//a[@rel="v:directedBy"]/text()').getall()
        item['actor'] = response.xpath('//a[@rel="v:starring"]/text()').getall()
        item['genre'] = response.xpath('//span[@property="v:genre"]/text()').getall()
        info = ''.join(response.xpath('//div[@id="info"]/text()').getall())
        item['country'] = info.replace('/', '').split()[0]
        item['length'] = re.search(r'\d+', response.xpath('//span[@property="v:runtime"]/text()').get()).group()
        item['rank'] = re.search(r'\d+', response.xpath('//span[@class="top250-no"]/text()').get()).group()
        item['img_url'] = response.xpath('//div[@id="mainpic"]//img/@src').get()
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_comment(self, response):
        item = {}
        item['entity'] = 'comment'
        item['movie'] = response.xpath('//h1/text()').get().split()[0]
        item['comment'] = response.xpath('//span[@class="short"]/text()').getall()
        return item
