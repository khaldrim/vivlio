# vivlio




# Backend
## Iniciar
Seguir los siguientes comandos, ubicándose en la carpeta root
```
sudo docker-compose build
sudo docker-compose run django python ./django/manage.py makemigrations
sudo docker-compose run django python ./django/manage.py migrate
```

Luego, cada vez que se desee iniciar, se debe poner el siguiente comando
```
sudo docker-compose up
```

Para crear un superusuario, utilizar el siguiente comando
```
sudo docker-compose run django python ./django/manage.py createsuperuser
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

