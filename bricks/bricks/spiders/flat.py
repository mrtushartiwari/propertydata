# -*- coding: utf-8 -*-
import scrapy
import re

class FlatSpider(scrapy.Spider):
	name = 'flat'
	allowed_domains = ["magicbricks.com"]
	start_urls = (
        'https://www.magicbricks.com/propertyDetails/2-BHK-1067-Sq-ft-Multistorey-Apartment-FOR-Sale-Baner-in-Pune&id=4d423237303834383231',
    )
	#startindex = 2
	#titles=values=[]
	#  detailurl = response.xpath('//a[@class="m-srp-card__title"]/@href').extract()   # it jumps form listing to main page
	
	custom_settings = {
	# specifies exported fields and order
	'FEED_EXPORT_FIELDS': ['price','bhk','address','bedroom','area','pricepersquare'],
	}

	

	def parse(self, response):
    	
		A = response.xpath('//div[@class="p_value"]/text()').extract()
		bl = "\n"
		for i in range(A.count(bl)):
			A.remove(bl)
			
		statusf = "Ready to Move"   
		t = response.xpath('//div[@class="p_value"]/text()').extract()
		for i in t:
			l = re.search("Under Construction", i)
			if l is not None:
				statusf = "Under Construction"

		transtype = "Old Property"
		for i in t:
			l = re.search("New Property", i)
			if l is not None:
				transtype = "New Property"
				
		B =response.xpath('//div[@class="descriptionCont"]/div').extract()		# description
		lengthofdes = len(B)
		startindex = 2
		titles=values=[]
		while lengthofdes > 0:
			#tit = response.xpath('//div[@class="descriptionCont"]/div[startindex]/div[1]/text()').extract()   # extract title  This is stupid as hell
			# how can you insert a variable in a string and expect it to act as a variable. lesson learned the hard way.
			tit = response.xpath('//div[@class="descriptionCont"]/div['+ str(startindex) +']/div[1]/text()').extract()
			titles.append(tit)
			val = response.xpath('//div[@class="descriptionCont"]/div[' + str(startindex) +']/div[2]/text()').extract()   # extract value
			values.append(val)
			startindex +=1
			lengthofdes -=1
			
		
		C = response.xpath('//div[@class="propInfoBlockInn"]//div[@class="p_value"]/text()').extract()
		for i in range(C.count(bl)):
			C.remove(bl)
		D = response.xpath('//div[@class="propInfoBlockInn"]//div[@class="p_title"]/text()').extract()
		try:
			D.remove('Super area')
		except ValueError:
			pass
		try:
			D.remove('Carpet area')
		except ValueError:
			pass
		try:
			D.remove('Society')
		except ValueError:
			pass
		try:
			D.remove('\nBedrooms\n')
		except ValueError:
			pass
		
		
		"""lengthofpropinfo = len(D)	
		while lengthofpropinfo > 0:
			tit1 = response.xpath('//div[@class="descriptionCont"]/div['+ str(startindex) +']/div[1]/text()').extract()
			titles1.append(tit)
			val1 = response.xpath('//div[@class="descriptionCont"]/div[' + str(startindex) +']/div[2]/text()').extract()   # extract value
			values1.append(val)
			startindex +=1
			lengthofdes -=1"""
			
			
		item = {
        	'price' : response.xpath('//div[@class="p_price"]/div/meta[@itemprop="price"]/@content').extract(),
        	'bhk' : response.xpath('//div[@class="p_bhk"]/text()').extract(),
        	'address' : response.xpath('//div[@class="p_text"]/span/text()').extract(),
        	'bedroom' : response.xpath('//div[@class="seeBedRoomDimen"]/text()').extract_first(),
        	'area' :response.xpath('//span[@id="coveredAreaDisplay"]/text()').extract(),
        	'pricepersquare' : response.xpath('//div[@class="fo_11px c_dark_gray"]/text()').extract(),
        	#'scociety' : response.xpath('//span[@class="prop_address"]/a/text()').extract(),
        	#'Carpetarea' : response.xpath('//span[@id="carpetAreaDisplay"]/text()').extract_first(),
        	#'superarea' : response.xpath('//span[@id="coveredAreaDisplay"]/text()').extract(),
            #'status' : statusf,
            #'transaction' : transtype,
            #'amenities' : response.xpath('//div[@class="amenities"]/ul/li/text()').extract(),
            #'connectivity' : response.xpath('//section[2]/ul/li/text()').extract(),
            #'descriptitles': titles,
            #'descripvalues': values,
            #'PropertyID' : response.xpath('//div[@class="propertyId"]/text()').extract_first(),
            #'propertyinfotitle' : D,
            #'propertyinfovalues' : C,
        	}
		yield item
        	
