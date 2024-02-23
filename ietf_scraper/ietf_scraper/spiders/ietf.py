import scrapy
import csv
import os

class AmazonMobileSpider(scrapy.Spider):
    name = 'amazon_mobiles'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=mobile']

    def parse(self, response):
        mobile_names = response.css('.s-title-instructions h2 a::text').extract()

        for mobile_name in mobile_names:
            yield {
                'mobile_name': mobile_name
            }

        next_page = response.css('.s-pagination-next::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

        
        csv_file_path = os.path.join('spiders', 'mobiles.csv')
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['mobile_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if response.url == self.start_urls[0]:
                writer.writeheader()

            for mobile_name in mobile_names:
                writer.writerow({'mobile_name': mobile_name})
