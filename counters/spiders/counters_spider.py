import scrapy

class CountersSpider(scrapy.Spider):
    name = "counters"

    start_urls = [
            'http://champion.gg/champion/riven/'
    ]

    def parse(self, response):
        champion = 
        role =
        data =
        patch =
        filename = 'output.json'
        with open(filename, 'wb') as f:
            f.write(stats)
