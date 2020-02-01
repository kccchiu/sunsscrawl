import scrapy
from ..items import SunscrawlItem

class ImgSpider(scrapy.Spider):
    name = "images"
    start_urls = ['https://chicago.suntimes.com/news search?q=gun+violence',
                  'https://chicago.suntimes.com/search?page=2&q=gun+violence']

    def parse(self, response):
        item = SunscrawlItem()
        image = []
        news = response.css('div.c-compact-river')
        for new in news:
            for img in new.css("div.c-compact-river__entry"):
                image.append(img.css("img::attr(src)"))
        item["image"] = image
        return item


