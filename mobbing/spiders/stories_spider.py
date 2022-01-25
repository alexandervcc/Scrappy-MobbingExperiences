import scrapy

class QuotesSpider(scrapy.Spider):
    name = "mobbing-stories"
    
    def start_requests(self):
        urlFile = open("/home/alexander/Desktop/github/Tesis/projects/mobbing/mobbing_urls.txt", "r")
        content = urlFile.read().split('\n')
        urls = [ ]
        for url in content:
            urls.append("https://www.overcomebullying.org"+url)
 
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
        



#.attrib['src']