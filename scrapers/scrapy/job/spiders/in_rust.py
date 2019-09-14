# -*- coding: utf-8 -*-
import scrapy


class InRustSpider(scrapy.Spider):
    name = 'in_rust'
    start_urls = ['https://this-week-in-rust.org/']

    def parse(self, response):

        for href in response.css("div.custom-xs-text-left > a::attr(href)").getall():
            yield response.follow(href, self.parse_post_and_jobs)

    def parse_post_and_jobs(self, response):
        date = ".".join(response.url.split("/")[4:7]).replace(".","-")

        post_titles = response.css("#news-blog-posts + ul > li > a::text").getall()
        post_urls = response.css("#news-blog-posts + ul > li > a::attr(href)").getall()
        posts = { "posts": len(post_titles), **dict(zip(post_titles, post_urls)) }

        job_titles = response.css("#rust-jobs + ul > li > a::text").getall()
        job_urls = response.css("#rust-jobs + ul > li > a::attr(href)").getall()
        jobs = { "job": len(job_titles), **dict(zip(job_titles, job_urls)) }

        # sorted(list, key = lambda i: i["Posts"], reverse = True)
        yield {
            "date": date,
            **posts,
            **jobs,
        }
