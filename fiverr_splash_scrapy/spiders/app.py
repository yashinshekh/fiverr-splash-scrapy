# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['kiezebrink.eu']
    start_urls = ['https://kiezebrink.eu/en/wholesale/frozen-foods/']

    script1 = """
            function main(splash, args)
            assert (splash:go(args.url))
            assert (splash:wait(0.5))
            return {
                html = splash: html(),
                png = splash:png(),
                har = splash:har(),
            }
            end
          """

    def start_requests(self):
        for line in self.start_urls:
            yield SplashRequest(line,callback=self.parse,
                                endpoint='render.html',
                                args={
                                    'html': 1,
                                    'lua_source': self.script1,
                                    'wait': 0.5,
                                })

    def parse(self, response):
        pass
