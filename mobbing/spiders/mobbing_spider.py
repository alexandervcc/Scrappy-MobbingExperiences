import scrapy

class QuotesSpider(scrapy.Spider):
    name = "mobbing-urls"
    
    def start_requests(self):
        urls = [
            'https://www.overcomebullying.org/workplace-bullying-stories.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        retrievedUrls = response.xpath('//div/p/a/@href').getall()
        data = []
        for entry in retrievedUrls:
            if entry[0]=="/":
                data.append(entry)
        
        #writing file
        with open('mobbing_urls.txt', 'w') as f:
            for item in data:
                f.write("%s\n" % item)
        



#.attrib['src']