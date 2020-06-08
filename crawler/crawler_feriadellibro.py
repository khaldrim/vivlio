import scrapy
import json
import unicodedata

# Página a testear: https://www.feriachilenadellibro.cl/literatura

book_array = []
def toJSON(books=[]):
		with open('./data/data.json', 'w') as output:
			json.dump(books, output, ensure_ascii=False)

class BookSpider(scrapy.Spider):
	name = "book_spider"
	start_urls = ['https://www.feriachilenadellibro.cl/literatura']
	
	
	def parse(self, response):
		DIV_SELECTOR = '/html/body/div[1]/main/div[2]/div[1]/div[4]/ol/li[*]'
		for elem in response.xpath(DIV_SELECTOR):
			URL_SELECTOR = './/div/a/@href'
			IMAGE_SELECTOR = './/div/a/span/span/img/@src'

			url = elem.xpath(URL_SELECTOR).extract_first()
			
			#Extraigo la imagen aqui, es más sencillo
			img = elem.xpath(IMAGE_SELECTOR).extract_first()

			yield scrapy.Request(url=url, callback=self.parse_book, meta={'img': img})

			
			# NEXT_PAGE_SELECTOR = './/div[5]/div[2]/ul'
			# next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
			# print(next_page)
			# if next_page:
			# 	yield scrapy.Request(
			# 		response.urljoin(next_page),
			# 		callback=self.parse
			# 	)

	#TODO: Hacer parseador de pagina para sacar todas las paginas, luego ir pagina por pagina sacando los libros

	def parse_book(self, response):
		DIV_SELECTOR = '/html/body/div[1]/main/div[2]'
		for book in response.xpath(DIV_SELECTOR):
			NAME_SELECTOR = './/div[1]/div[2]/div[1]/div/h1/span/text()'
			SINOPSIS_SELECTOR = './/div[1]/div[4]/div/div[2]/div/div/p/span/text()'
			SINOPSIS_V2_SELECTOR = './/div[1]/div[4]/div/div[2]/div/div/p/text()'
			SINOPSIS_V3_SELECTOR = './/div[1]/div[4]/div/div[2]/div/div/text()'
			PAGE_NUM_SELECTOR = './/div[1]/div[4]/div/div[4]/div/table/tbody/tr[7]/td/text()'
			INTERNET_PRICE_SELECTOR = './/div[1]/div[2]/div[2]/div[3]/span[1]/span/span/span/text()'
			SHOP_PRICE_SELECTOR = './/div[1]/div[2]/div[2]/div[3]/span[2]'
			AUTHOR_SELECTOR = './/div[1]/div[4]/div/div[4]/div/table/tbody/tr[2]/td/text()'
			ISBN_SELECTOR = './/div[1]/div[4]/div/div[4]/div/table/tbody/tr[3]/td/text()'
			EDITORIAL_SELECTOR = './/div[1]/div[4]/div/div[4]/div/table/tbody/tr[4]/td/text()'
			BINDING_SELECTOR = './/div[1]/div[4]/div/div[4]/div/table/tbody/tr[5]/td/text()'

			#Name
			name = book.xpath(NAME_SELECTOR).extract_first()

			#Sinopsis
			sinopsis = book.xpath(SINOPSIS_SELECTOR).extract_first()
			sinopsis_v2 = book.xpath(SINOPSIS_V2_SELECTOR).extract_first()
			sinopsis_v3 = book.xpath(SINOPSIS_V3_SELECTOR).extract_first()

			if sinopsis is not None:
				selected_sinopsis = sinopsis
			elif sinopsis_v2 is not None:
				selected_sinopsis = sinopsis_v2
			elif sinopsis_v3 is not None:
				selected_sinopsis = sinopsis_v3
			else:
				selected_sinopsis = None

			#Page number
			page_number = book.xpath(PAGE_NUM_SELECTOR).extract_first()

			#Price
			internet_price = book.xpath(INTERNET_PRICE_SELECTOR).extract_first()
			internet_price = internet_price.replace('$', '')
			internet_price = internet_price.replace('.', '')	

			shop_price = book.xpath(SHOP_PRICE_SELECTOR).extract_first()
			shop_price = str(''.join(list(filter(str.isdigit, shop_price))))

			#Author
			author = book.xpath(AUTHOR_SELECTOR).extract_first()
			
			#ISBN
			isbn = book.xpath(ISBN_SELECTOR).extract_first()

			#Editorial
			editorial = book.xpath(EDITORIAL_SELECTOR).extract_first()

			#BookBinding
			book_binding = book.xpath(BINDING_SELECTOR).extract_first()

			#Creates book object
			book_obj = {
				'name': name,
				'sinopsis': selected_sinopsis,
				'page_number': page_number,
				'internet_price': internet_price,
				'shop_price': shop_price,
				'author': author,
				'isbn': isbn,
				'editorial': editorial,
				'binding': book_binding,
				'url': response.request.url,
				'img': response.meta['img']
			}

			book_array.append(book_obj)

		toJSON(book_array)

	