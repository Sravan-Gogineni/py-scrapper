import scrapy
from ..items import AmazonItem

class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://www.amazon.com/s?k=desk&crid=3045GGLV5NKMN&sprefix=desk%2Caps%2C118&ref=nb_sb_noss_1"]

    def parse(self, response):
        items = AmazonItem()
        product_name = response.css('')
        
        
      
        
