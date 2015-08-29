
# -*- coding:UTF-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from cililian.items import CililianItem


class cililianSpider(Spider):
    name = "cililian"
    start_urls = ["http://cililian.me/list/720p/1.html"]
    allowed_domains = ["cililian.me"]
    mykeyword = "720p"
    def __init__(self, keyword="720p", *args, **kwargs):
        super(cililianSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://cililian.me/list/%s/1.html' % keyword]
        self.mykeyword = keyword


    def parse(self, response):
        sel = Selector(response)
        i=0
        items= []
        while i<10:
            i=i+1
            pathstr1 = '//*[@id="container"]/div[3]/ul/li[%d]/div[1]/a/text()'%i
            pathstr2 = '//*[@id="container"]/div[3]/ul/li[%d]/div[1]/a/span/text()'%i
            pathstr = pathstr1+"|"+pathstr2
            matchcontents = sel.xpath(pathstr)
            item = CililianItem()
            item['keyword'] = self.mykeyword
            outstr = ""
            for matchcontent in matchcontents:
                  outstr = outstr + matchcontent.extract()
            item['name'] = outstr.rstrip()
            movietype = item['name'][-3:]

            pathstr = '//*[@id="container"]/div[3]/ul/li[%d]/div[2]/a[1]/@href'%i
            matchcontents = sel.xpath(pathstr)
            outstr = ""
            for matchcontent in matchcontents:
                  outstr = outstr + matchcontent.extract()
            item['link'] = outstr

            pathstr = '//*[@id="container"]/div[3]/ul/li[%d]/dl/dt/span[1]/text()'%i
            matchcontents = sel.xpath(pathstr)
            outstr = ""
            for matchcontent in matchcontents:
                  outstr = outstr + matchcontent.extract()
            item['size'] = outstr.strip()
            moviesize = outstr.strip()[:-3]
            if "GB" in outstr.strip() and movietype<>"mvb" and float(moviesize)<4 and float(moviesize)>1:
                items.append(item)
		print item['link']
        return items
