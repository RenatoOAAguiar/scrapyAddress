__autor__ = 'Renato'
from scrapy.spiders import Spider
from scrapy.selector import  Selector
from .searchResult import searchResultPages
from .searchEngine import SearchEngineResult
from scrapy.http import Request

class SpiderAddress(Spider):
    name = 'SpiderAddress'
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None

    def __init__(self, keyword, *args, **kwargs):
        super(SpiderAddress, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = 'google'
        self.selector = SearchEngineResult[self.searchEngine]
        pageUrls = searchResultPages(keyword, self.searchEngine , 1)
        print(pageUrls)
        for url in pageUrls:
            print("---------------URL--------------------"+url)
            self.start_urls.append(url)

    def parse(self, response):
        for url in Selector(response).xpath('//h3/a/@data-href').extract():
            print(url.replace('/url/?q=',''))
            yield Request(url.replace('/url/?q=',''), callback=self.parseAddress)
    
    def parseAddress(self, response):
        for data in Selector(response).xpath('//body/text()').extract():
            yield {'data':data}
