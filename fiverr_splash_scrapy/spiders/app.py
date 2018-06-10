# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['google.com']
    start_urls = ['']


    def start_requests(self):
        for line in self.start_urls:
            yield SplashRequest(line,callback=self.parse,args={'wait':'5'})

    def parse(self, response):
        pass
