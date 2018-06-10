# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    alllinks = []

    def start_requests(self):
        for line in self.alllinks:
            yield SplashRequest(line,callback=self.parse,args={'wait':'5'})

    def parse(self, response):
        pass
