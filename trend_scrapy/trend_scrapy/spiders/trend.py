import scrapy
from scrapy.spiders import BaseSpider

from trend_scrapy.items import TrendItem


class TrendSpider(BaseSpider):
    name = "trend"

    def start_requests(self):
        yield scrapy.Request('https://github.com/trending', self.parse_trend)

    def parse_trend(self, response):
        doc = response.xpath('//ol[@class="repo-list"]/li')
        for rank, li in reversed(list(enumerate(doc))):
            url = li.xpath('div/h3/a/@href').extract()[0] # url
            desc_list = li.xpath('div[@class="py-1"]/p/text()').extract()

            # emoji filtering
            desc = ''
            for str in desc_list:
                if str.isspace():
                    continue
                else:
                    desc = str.strip()
                    break

            language = li.xpath('div/span[@itemprop="programmingLanguage"]/text()').extract()
            if language:
                language = language[0].strip()
            else:
                language = ''
            star_count = int(li.xpath('div/a[1]/text()').extract()[3].replace(',', ''))
            fork_count = int(li.xpath('div/a[2]/text()').extract()[1].replace(',', ''))
            today_star_count = int(li.xpath('div/span[@class="float-right"]/text()').extract()[1].replace(',', '').replace('stars today', ''))
            print(url)
            print(desc) # desc
            print(language) # language
            print(star_count) # star count
            print(fork_count) # fork count
            print(today_star_count) #today star

            yield TrendItem(rank=rank+1, url=url, desc=desc, language=language, star_count=star_count, fork_count=fork_count, today_star_count=today_star_count)
