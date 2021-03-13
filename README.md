# resuelve-back

Prueba de Resuelve tu deuda Back-end

### DOCKER

Para ejecutar el proyecto, puede ser a través de un contenedor de docker.

**Requisitos:**

- docker v20.10
- docker-compose v1.27

**Instrucciones:**

1. Descargamos el proyecto del repositorio de GitHub

```
git clone https://github.com/vaneEmy/resuelve-back.git
```

2. Nos dirigimos a la carpeta **resuelve-back** donde se encuentran el archivo *dockerfile* y el *docker-compose.yaml*

```
cd resuelve-back
```

3. Construimos la imagen de docker 

```
docker build .
```

4. Construimos el servicio **app**, la cual levantará la aplicación en el puerto 8000

```
docker-compose build
```

5. Podemos realizar peticiones desde nuestro host *http://127.0.0.1:8000*
