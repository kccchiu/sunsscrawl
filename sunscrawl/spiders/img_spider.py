import scrapy
from ..items import SunscrawlItem


class ImgSpider(scrapy.Spider):
    # pages = int(input('How many pages of image do you want to scrape: '))
    pages = 999
    if pages >= 1000 or type(pages) != int:
        raise ValueError(
            "The value you entered is either too big or invalid. Please enter a number that is less than 1000")

    name = "images"
    # start_urls = ['https://chicago.suntimes.com/search?page={}&q=gun+violence'.format(i + 1) for i in range(pages)]
    start_urls = ['https://chicago.suntimes.com/search?page={}&q=gun'.format(i + 1) for i in range(pages)]

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
