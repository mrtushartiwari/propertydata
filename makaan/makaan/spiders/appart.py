# -*- coding: utf-8 -*-
import scrapy


class AppartSpider(scrapy.Spider):
	name = 'appart'
	allowed_domains = ['www.makaan.com']
	start_urls = ['https://www.makaan.com/pune-residential-property/buy-property-in-pune-city?page=1']

	def parse(self, response):
		urls = response.xpath('//a[@class="typelink"]/@href').extract()
		with open("Singlepagelinks.txt", "a") as myfile:
			for url in urls:
				myfile.write(str(url) + "\n")
				
		# follow pagination link
		for count in range(2,1909):		# total pages = 1909
			next_page_url = 'https://www.makaan.com/pune-residential-property/buy-property-in-pune-city?page={}'.format(count)
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)
			
	#def parse_details(self, response):
		#pass
        #yield {
        #    'name': response.css('h3.author-title::text').extract_first(),
        #    'birth_date': response.css('span.author-born-date::text').extract_first(),
        #}
            

