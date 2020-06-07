import scrapy
import json

# Página a testear: https://www.feriachilenadellibro.cl/literatura

book_array = []

def toJSON(books=[]):
		with open('./data/data.json', 'w') as output:
			json.dump(books, output)

class BookSpider(scrapy.Spider):
	name = "book_spider"
	start_urls = ['https://www.feriachilenadellibro.cl/literatura']
	
	

	def parse(self, response):
		DIV_SELECTOR = '/html/body/div[1]/main/div[2]/div[1]/div[4]/ol/li[*]'
		for book in response.xpath(DIV_SELECTOR):
			NAME_SELECTOR = './/div/div/strong/a/text()'
			PRICE_INTERNET_SELECTOR = './/div/div/div[1]/span[1]/span/span/span/text()'
			PRICE_SHOP_SELECTOR = './/div/div/div[1]/span[2]'
			AUTHOR_SELECTOR = './/div/div/span/p/text()'
			AUTHOR2_SELECTOR = './/div/div/span/text()'
			AUTHOR3_SELECTOR = './/div/div/span/p/span/text()'
			AUTHOR4_SELECTOR = './/div/div/span/h2/text()'

			IMAGE_SELECTOR = '.	//div/a/span/span/img/@src'
			URL_SELECTOR = './/div/a/@href'

			name = book.xpath(NAME_SELECTOR).extract_first().strip()
			name = name[0].upper() + name[1:].lower()
			
			price_internet = book.xpath(PRICE_INTERNET_SELECTOR).extract_first()
			price_internet = price_internet.replace('$', '')
			price_internet = price_internet.replace('.', '')			

			price_shop = book.xpath(PRICE_SHOP_SELECTOR).extract_first()
			price_shop = str(''.join(list(filter(str.isdigit, price_shop))))
			
			author = book.xpath(AUTHOR_SELECTOR).extract_first()
			author2 = book.xpath(AUTHOR2_SELECTOR).extract_first()
			author3 = book.xpath(AUTHOR3_SELECTOR).extract_first()
			author4 = book.xpath(AUTHOR4_SELECTOR).extract_first()

			url = book.xpath(URL_SELECTOR).extract_first()
			img = book.xpath(IMAGE_SELECTOR).extract_first()

			#if ',' in author:
			#	splited_author = author.split(',')
			#	author = splited_author[1] + ' ' + splited_author[0] 

			# author = author[0].upper() + author[1:].lower()

			book_obj = {
				'name': name,
				'author': author,
				'author2': author2,
				'author3': author3,
				'author4': author4,
				'price_internet': price_internet,
				'price_shop': price_shop,
				'url': url,
				'img': img
			}

			book_array.append(book_obj)


		toJSON(book_array)

	