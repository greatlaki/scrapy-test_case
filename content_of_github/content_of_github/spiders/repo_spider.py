import scrapy

NAME ="li.Box-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)"
ABOUT = "li.Box-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(2)"
LINK = "li.Box-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a::attr(href)"
STARS = "li.Box-row:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3)"
EX_LINK = "li.js-responsive-underlinenav-item:nth-child(2) > a::attr(href)"


class GitSpider(scrapy.Spider):
    name = "github"
    start_urls = ["https://github.com/scrapy"]

    def parse(self, response):
        for link in response.css(EX_LINK):
            yield response.follow(link, callback=self.parse_repo)

    def parse_repo(self, response):
        yield {
            "name": response.css(NAME).get(-1).split('\n')[-2].strip(),
            "about": response.css(ABOUT).get(-1).split("\n")[-2].strip(),
            "link": response.css(LINK).get(-1),
            "stars": response.css(STARS).get().split("\n")[-2].strip(),
        }

