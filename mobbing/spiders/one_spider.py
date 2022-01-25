import scrapy

class QuotesSpider(scrapy.Spider):
    name = "mobbing-example"
    
    def start_requests(self):
        urls = [
            'https://www.overcomebullying.org/im-better-off-being-away-from-that-toxic-work-environment-and-toxic-woman.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        retrievedP = response.xpath('//div[@class="Liner"]/div/p/text()').getall()
        textStr = str(retrievedP)
        stories = textStr.split("\\n")
        story = ""
        for item in stories:
            if len(item)>len(story):
                story=item
        #writing file
        story = story.strip()
        with open('mobbing_stories.txt', 'a') as f:
            f.write("%s\n" % story)