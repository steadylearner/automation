# -*- coding: utf-8 -*-
import scrapy

class RemoteJobSpider(scrapy.Spider):
    name = 'remote_job'
    start_urls = [
        "https://github.com/frontendbr/vagas/issues",
        "https://github.com/react-brasil/vagas/issues",
        "https://github.com/backend-br/vagas/issues",
    ]

    def parse(self, response):

        # text, href dict
        # filter it with text
        # use href

        titles = response.xpath("//a[@data-hovercard-type='issue']/text()").getall()
        hrefs = response.xpath("//a[@data-hovercard-type='issue']/@href").getall()

        before_filter = dict(list(zip(titles, hrefs)))

        # remote_variations = ["Remote", "remote", "Remoto", "remoto"]

        with_remote = dict(filter(lambda elem:
            "Remote" in elem[0] or "Remoto" in elem[0] or "remoto" in elem[0] or "remote" in elem[0]
        , before_filter.items()))

        print(with_remote)

        for item in with_remote.items():
            href = item[1]
            # preifx = "https://github.com/react-brasil/vagas/issues"
            yield response.follow(href, self.parse_jobs)

    def parse_jobs(self, response):
        print(response.url)

        title = response.xpath("//span[@class='js-issue-title']/text()").get().strip()
        urls = response.css("tbody  a::attr(href)").getall()
        email_list = []

        for payload in urls:
            if payload.startswith("mailto"):
                email_index = urls.index(payload)
                email_with_mailto = urls.pop(email_index)
                email = email_with_mailto.split(":")[1]
                email_list.append(email)

        yield {
            "title": title,
            "urls": urls,
            "email_list": email_list,
            # "page": response.url
        }

