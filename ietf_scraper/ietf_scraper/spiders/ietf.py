import scrapy

class ietfgit (scrapy.Spider):
    name = 'reddit_comments'
    start_urls = ['https://www.reddit.com/r/subreddit_name/comments/post_id/']

    def parse(self, response):
        # Extract comments using XPath
        comments = response.xpath('//div[contains(@class, "Comment")]//p[@class="Comment__body"]//text()').extract()

        # Print or process the extracted comments
        for comment in comments:
            print(comment.strip())

        # Follow links to next pages if available
        next_page = response.css('a[rel="nofollow next"]::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
