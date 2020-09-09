# vivlio




# Backend
## Iniciar
Seguir los siguientes comandos, ubicándose en la carpeta root
```
sudo docker-compose build
sudo docker-compose run django python ./django/manage.py migrate
```

Para crear un superusuario, utilizar el siguiente comando
```
sudo docker-compose run django python ./django/manage.py createsuperuser
```

Para poblar la base de datos:
```
sudo docker-compose run django python ./django/manage.py populate
```

Luego, cada vez que se desee iniciar, se debe poner el siguiente comando
```
sudo docker-compose up
```

El backend correrá con la ip 0.0.0.0, puerto 8000. Para acceder al administrador, se utiliza la siguiente url
```
0.0.0.0:8000/admin
```

## Ejecutar comandos de python
Si se desea crear una nueva app, o realizar migraciones, correr el siguiente comando:
```
sudo docker-compose run django python ./django/manage.py "MICOMANDO"
```

## Visualizar documentación de api
La documentación se encuentra en
```
http://0.0.0.0:8000/doc/
```
Para realizar las consultas a elastic search, utilizar las siguientes urls:
Listar todos los libros:
```
http://0.0.0.0:8000/api/books/
```
Buscar libros cuyo título contenga una o varias letras
```
http://0.0.0.0:8000/api/books/?title__wildcard=*a*
```
## Problemas posibles
### ElasticSeach
Max virtual memory areas vm.max_map_count 'x' likely too low, increase to at least 262144

```
sudo sysctl -w vm.max_map_count=262144
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

