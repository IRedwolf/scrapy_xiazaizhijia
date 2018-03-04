# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyXiazaizhijiaItem
from scrapy.linkextractors import LinkExtractor
class XiazaizhijiaSpider(scrapy.Spider):
    name = 'xiazaizhijia'
    allowed_domains = ['xiazaizhijia.com']
    start_urls = ['http://www.xiazaizhijia.com/bizhi/mn/']
    image_urls = []

    def parse(self, response):
        # 解析当期页的url
        le = LinkExtractor(restrict_css='div.wp-list dt a')
        for link in le.extract_links(response):
            print(link.url)
            yield scrapy.Request(link.url, callback=self.parse_item)

        # 解析下一页的url
        le = LinkExtractor(restrict_css='div.page a:nth-last-child(2)')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_item(self, response):
        item = ScrapyXiazaizhijiaItem()
        item['image_urls'] = []
        down_load = response.css('.sel-size a:nth-child(2)::attr(href)').extract_first(default='N\A')
        item['image_urls'].append(down_load)
        item['name'] = response.css('.main-title h1::text').extract_first()
        yield item



