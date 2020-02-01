import scrapy


class PostsSpider(scrapy.Spider):
    name = "news"
    start_urls = ['https://chicago.suntimes.com/news search?q=gun+violence',
                  'https://chicago.suntimes.com/search?page=2&q=gun+violence']

    def parse(self, response):
        data = {}
        news = response.css('div.c-compact-river')
        for new in news:
            for n in new.css("div.c-compact-river__entry"):
                yield {
                    'Section': n.css('ul.c-entry-box--compact__labels li a span::text').get(),
                    'Title': n.css('h2.c-entry-box--compact__title a::text').get(),
                    'Description': n.css('p.c-entry-box--compact__dek::text').get(),
                    'Author': n.css(
                        'div.c-byline span.c-byline-wrapper span.c-byline__item span.c-byline__author-name::text').get(),
                    'Date': n.css(
                        'div.c-byline span.c-byline-wrapper span.c-byline__item time.c-byline__item::text').get().strip()
                }

        next_page = response.css(
            'nav.c-pagination.u-clearfix a.c-pagination__next.c-pagination__link.p-button::attr(href)').get()

        for counter in range(10):
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
            counter += 1
