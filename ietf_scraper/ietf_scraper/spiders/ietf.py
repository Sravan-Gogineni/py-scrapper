import scrapy

class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["http://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        return{
         #title = response.css('span.title::text').get()
            'title' :  response.xpath('//span[@class="title"]/text()').get(),
           'author' :  response.xpath('//span[@class= " author-name"]/text()').get(),
           'date'   : response.xpath('//span[@class="date"]/text()').get(),
           'subheading' : response.xpath('//span[@class= "subheading"]/text()').get(),
         'subheading2' : response.xpath('//span[@class= "subheading"]/text()').get(),
         subheading3 =  response.xpath('//span[@class= "subheading"]/text()').get(),
         subheading4 =  response.xpath('//span[@class= "subheading"]/text()').get(),
         subheading5 =  response.xpath('//span[@class= "subheading"]/text()').get(),
         subheading6 =  response.xpath('//span[@class = "subheading"]/text()').get(),
         address = response.xpath('//span[@class="address"]/text()').get(),
         phone = response.xpath('//span[@class="phone"]/text()').get(),
         email = response.xpath('//span[@class="email"]/text()').get(),
        }
      
        
