import scrapy

class Novel(scrapy.Spider):
    #爬虫名称 值在启动爬虫时会用到
    name = "novel"
    # 爬虫启始url
    start_urls = [
        'https://www.qbiqu.com/',
    ]
    def parse(self, response):
        # 定义存储的数据格式
        yield {
            'text': response.xpath('//div[@class="bookname"]/h1[1]/text()').extract_first(),
            'content': response.xpath('//div[@id="content"]/text()').extract(),
            # 'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
            # 'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
        }
        # 下一章的链接
        next_page_url = response.xpath('//div[@class="bottem1"]/a[3]/@href').extract_first()
        # 如果下一章的链接不等于首页 则爬取url内容  ps：最后一章的下一章链接为首页
        if next_page_url != 'https://www.xbiquge6.com/0_638/':
            yield scrapy.Request(response.urljoin(next_page_url))
