import scrapy


# Página a testear: https://www.antartica.cl/antartica/servlet/LibroServlet?action=browseSubCategoria&id_subcategoria=20090505&id_categoria=200905
# Antartica -> Literatura Latinoamericana -> Novela Chilena

class BookSpider(scrapy.Spider):
	name = "book_spider"
	start_urls = ['https://www.antartica.cl/antartica/servlet/LibroServlet?action=browseSubCategoria&id_subcategoria=20090505&id_categoria=200905']

	def parse(self, response):
		print("--------------------")
		#/html/body/table/tbody/tr[2]/td/table/tbody/tr[4]/td[1]/table/tbody/tr/td/table[2]
		TABLE_SELECTOR = '//table[@cellspacing="5"]'
		for book in response.xpath(TABLE_SELECTOR):
			#/html/body/table/tbody/tr[2]/td/table/tbody/tr[4]/td[1]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/a
			
			print(book)
			NAME_SELECTOR = 'tbody/tr[2]/td[2]/a[@class="txtTitulosRutaSeccionLibros"]/text()'
			
			yield {
				'name': book.xpath(NAME_SELECTOR).extract_first(),
			}


		print("--------------------")
		#TABLE_SELECTOR = '/html/body/table/tbody/tr[2]/td/table/tbody/tr[4]/td[1]/table/tbody/tr/td/table[2]'
		#TABLE_SELECTOR = '/html/body/table'
		#book = response.xpath(TABLE_SELECTOR)
		#print(book)
		#print("hi")


		#TABLE_SELECTOR = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(4)"
		#TABLE_SELECTOR = "html body table tbody tr td table tbody tr td table tbody tr td table"
		#for book in response.css(TABLE_SELECTOR):
			#print(book)
		#	NAME_SELECTOR = './/tbody/tr[2]/td[2]/a'
			
			#PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
			#MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
			#IMAGE_SELECTOR = 'img ::attr(src)'

		#	yield {
		#		'name': book.xpath(NAME_SELECTOR).extract_first(),
			#	'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
			#	'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
			#	'image': brickset.css(IMAGE_SELECTOR).extract_first(),
		#	}

		#NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
		#next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		#if next_page and i < stop:
		#	i+=1
		#	yield scrapy.Request(
		#		response.urljoin(next_page),
		#		callback=self.parse
		#	)