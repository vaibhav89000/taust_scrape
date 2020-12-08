# -*- coding: utf-8 -*-
import scrapy
import time
import os
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import re

from ..items import TaustItem


class GetdataSpider(scrapy.Spider):
    name = 'getdata'

    def start_requests(self):
        index = 0
        yield SeleniumRequest(
            url="https://www.taust.ee/otsi/?search_type=c&name=o%C3%BC&limit=20&sort=code&page=1https://www.taust.ee/otsi/?search_type=c&name=o%C3%BC&limit=20&sort=code&page=1",
            wait_time=1000,
            screenshot=True,
            callback=self.parse,
            meta={'index': index},
            dont_filter=True
        )

    def parse(self, response):
        driver = response.meta['driver']
        html = driver.page_source
        response_obj = Selector(text=html)
        index = response.meta['index']

        details = response_obj.xpath("//table/tbody/tr")

        Taust_Item = TaustItem()

        for idx, detail in enumerate(details):
            nimi = detail.xpath(".//td[1]/a/text()").get()
            kood = detail.xpath(".//td[2]/a/text()").get()
            address = detail.xpath(".//td[3]/text()").get()
            telefon = detail.xpath(".//td[4]/text()").get()
            email = detail.xpath(".//td[5]/a/text()").get()

            Taust_Item['nimi'] = nimi
            Taust_Item['kood'] = kood
            Taust_Item['address'] = address
            Taust_Item['telefon'] = telefon
            Taust_Item['email'] = email

            yield Taust_Item

            print('\n'*2)
            print(nimi,kood,address,telefon,telefon,email)
            print('\n' * 2)
        index += 1
        if(index<=10):
            yield SeleniumRequest(
                url="https://www.taust.ee/otsi/?search_type=c&name=o%C3%BC&limit=20&sort=code&page=1https://www.taust.ee/otsi/?search_type=c&name=o%C3%BC&limit=20&sort=code&page={}".format(index),
                wait_time=1000,
                screenshot=True,
                callback=self.parse,
                meta={'index': index},
                dont_filter=True
            )


