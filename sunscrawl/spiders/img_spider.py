import scrapy
from ..items import SunscrawlItem


class ImgSpider(scrapy.Spider):
    name = "images"
    pages = 10
    start_urls = ['https://chicago.suntimes.com/search?page={}&q=gun+violence'.format(i+1) for i in range(pages)]

    def parse(self, response):
        item = SunscrawlItem()
        img_urls = []
        for new in response.css('div.c-compact-river'):
            for img in new.css("div.c-compact-river__entry"):
                img_urls.append(img.css("div.c-entry-box--compact__image img::attr(src)").extract()[1])
        item["image_urls"] = img_urls

        # next_page = response.css(
        #     'nav.c-pagination.u-clearfix a.c-pagination__next.c-pagination__link.p-button::attr(href)').get()
        # for counter in range(10):
        #     if next_page is not None:
        #         response.urljoin(next_page)
        #         yield scrapy.Request(next_page, callback=self.parse)
        #     counter += 1

        return item




