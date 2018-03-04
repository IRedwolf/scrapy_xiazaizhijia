# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyXiazaizhijiaItem

class XiazaizhijiaSpider(scrapy.Spider):
    name = 'xiazaizhijia'
    allowed_domains = ['xiazaizhijia.com']
    start_urls = ['http://www.xiazaizhijia.com/bizhi/85167.html']
    image_urls = []

    def parse(self, response):
        item = ScrapyXiazaizhijiaItem()
        item['image_urls'] = []
        down_load = response.css('.sel-size a:nth-child(2)::attr(href)').extract_first()
        item['image_urls'].append(down_load)
        item['name'] = response.css('.main-title h1::text').extract_first()
        return item



