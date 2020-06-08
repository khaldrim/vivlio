# Crawler

# Objetivo

Extraer data de páginas de librerías chilenas como: https://www.antartica.cl, https://www.feriachilenadellibro.cl/, etc. Además, aplicar aumento de datos
para obtener un corpus sobre el cual indexar.

##### Disclaimer: El proyecto tiene como objetivo plantear un sistema de recuperación de información sencillo, no se enviarán solicitudes constantemente a los sitios mencionados para no denegar el servicio que brindan.

# Guias:

	- https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3

# Recomendaciones:

	Utilizar ambientes virtuales, para ello utilizar la siguiente guía: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server-es


# Pasos para crear un ambiente virtual:
```shell
	cd vivlio/crawler
	python3 -m venv env
	source env/bin/activate
```

Nota: Para desactivar el ambiente virtual
```shell
	deactivate
``` 	

# Instalar dependencias:

Luego de crear el ambiente virtual:

```shell
	pip install scrapy
```

# Requisitos:
	
	- Python v3.8.2
	- Scrappy v2.1.0

# Uso:

```shell
	scrapy runspider <nombre_archivo>.py
```
