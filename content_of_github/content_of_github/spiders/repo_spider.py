import scrapy

from const_of_css import *


class GitSpider(scrapy.Spider):
    name = "github"
    start_urls = ["https://github.com/scrapy"]

    def parse(self, response):
        link_repo = "li.js-responsive-underlinenav-item:nth-child(2) > a::attr(href)"
        for link in response.css(link_repo.get(-1)):
            yield response.follow(link, callback=self.parse_repo)

    def parse_repo(self, response):
        yield {
            "name": response.css(NAME).get(-1).split('/')[-1],
            "about": response.css(ABOUT.get(-1).split("\n")[-2].strip()),
            "link": response.css(LINK.get(-1)),
            "stars": response.css(STARS.get(-1).split("\n")[-2].strip()),
        }