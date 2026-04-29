# Proyecto Django ECCI

Proyecto base de Django listo para ejecutar localmente, con Docker y preparado para subir a GitHub.

## Estructura principal

```txt
mi_proyecto/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── manage.py
├── mi_proyecto/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── myapp/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── migrations/
    └── templates/
        └── index.html
```

## Ejecutar con Docker

1. Copiar variables de entorno:

```bash
cp .env.example .env
```

2. Construir y levantar el contenedor:

```bash
docker compose up --build
```

3. Abrir en el navegador:

```txt
http://localhost:9000
```

La ruta raíz `/` redirige a `/myapp/`.

## Ejecutar migraciones

En otra terminal:

```bash
docker compose exec web python manage.py migrate
```

## Crear superusuario

```bash
docker compose exec web python manage.py createsuperuser
```

Luego entrar a:

```txt
http://localhost:9000/admin/
```

## Ejecutar sin Docker

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver 0.0.0.0:9000
```

## Subir a GitHub

```bash
git init
git add .
git commit -m "Proyecto Django base con Docker"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```
