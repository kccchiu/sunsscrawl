import scrapy

class PostsSpider(scrapy.Spider):
    # pages = int(input('How many pages of news do you want to scrape: '))
    pages = 999
    if pages >= 1000 or type(pages) != int:
        raise ValueError(
            "The value you entered is either too big or invalid. Please enter a number that is less than 1000")

    name = "news"
    # start_urls = ['https://chicago.suntimes.com/search?page={}&q=gun+violence'.format(i + 701) for i in range(pages)]
    start_urls = ['https://chicago.suntimes.com/search?page={}&q=gun'.format(i + 1) for i in range(pages)]

    def parse(self, response):
        for new in response.css('div.c-compact-river'):
            for n in new.css("div.c-compact-river__entry"):
                yield {
                    'section': n.css('ul.c-entry-box--compact__labels li a span::text').get(),
                    'title': n.css('h2.c-entry-box--compact__title a::text').get(),
                    'description': n.css('p.c-entry-box--compact__dek::text').get(),
                    'name': n.css(
                        'div.c-byline span.c-byline-wrapper span.c-byline__item span.c-byline__author-name::text').get(),
                    'created': n.css(
                        'div.c-byline span.c-byline-wrapper span.c-byline__item time.c-byline__item::text').get().strip(),
                    'image-link': n.css("div.c-entry-box--compact__image img::attr(src)").extract()[1]
                }
