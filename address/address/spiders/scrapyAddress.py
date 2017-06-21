__autor__ = 'Renato'
from scrapy.spiders import Spider
from scrapy.selector import  Selector
from searchResult import searchResultPages
from searchEngine import SearchEngineResult

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
        pageUrls = searchResultPages(keyword, self.searchEngine , 2)
        print(pageUrls)
        for url in pageUrls:
            print("---------------URL--------------------"+url)
            self.start_urls.append(url)

    def parse(self, response):
        for body in Selector(response).xpath('//body//text()').extract():
            yield {'body':body}
        for title in response.css('body'):
            yield {
            'body': title.css('body ::text').extract()
            }
        pass