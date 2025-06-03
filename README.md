# OrdinarioWebIIBackend
Proyecto Ordinario de la materia de desarrollo web, para un sistema de cotizaciones de eventos, backend desarrollado en Django

# Cotizaciones Backend

Proyecto backend para un sistema de cotización de eventos, desarrollado con Django, Django REST Framework y PostgreSQL, todo dockerizado.

## Tecnologías utilizadas

- Python 3.10
- Django
- Django REST Framework
- PostgreSQL 15
- Docker & Docker Compose

## Cómo iniciar el proyecto

1. Clona el repositorio:

   git clone https://github.com/TU_USUARIO/cotizaciones_backend.git
   cd cotizaciones_backend

2. Levanta los contenedores:

   docker-compose up --build

3. Aplica migraciones:

   docker-compose exec web python manage.py migrate

4. Crea un superusuario:

   docker-compose exec web python manage.py createsuperuser

5. Accede en el navegador:

   http://localhost:8000  
   http://localhost:8000/admin

## Estructura esperada

cotizaciones_backend/  
├── docker-compose.yml  
├── Dockerfile  
├── requirements.txt  
├── .env  
├── manage.py  
├── cotizaciones_backend/  
│   └── settings.py, urls.py, etc.  
└── apps/  
    └── core/

## Variables de entorno (.env)

DB_NAME=cotizaciones  
DB_USER=cotiza_user  
DB_PASS=cotiza_pass  
DB_HOST=db  
DB_PORT=5432  

## Comandos útiles

- Levantar todo:  
  docker-compose up --build

- Acceder al contenedor web:  
  docker-compose exec web bash

- Aplicar migraciones:  
  docker-compose exec web python manage.py migrate

- Crear superusuario:  
  docker-compose exec web python manage.py createsuperuser

- Apagar contenedores:  
  docker-compose down

## Migraciones basadas en modelos

Ya no es necesario importar un archivo SQL manualmente.  
Toda la estructura de la base de datos ha sido definida mediante modelos Django (`apps/core/models.py`), lo que permite manejarla con migraciones de forma limpia y controlada.

## Estado del desarrollo

- [x] Docker configurado  
- [x] PostgreSQL conectado  
- [x] Modelos creados (migraciones aplicadas)  
- [ ] API lista  
- [ ] Autenticación y usuarios  

