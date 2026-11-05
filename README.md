# Certamen 2 - Fundación Patrimonio Vivo

Proyecto web desarrollado en Django y Bootstrap para la gestión y difusión de lugares de interés patrimonial en Chile.

## Requisitos Previos
- Python 3.10 o superior
- Git

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/st1venssj/CER2-ZURITASTEVEN/tree/main
   cd Certamen2

2. Instalar dependencias:
    pip install -r requirements.txt

3.Aplicar migraciones de la base de datos:
    py manage.py makemigrations
    py manage.py migrate

4.Crear superusuario para la administracion y pruebas:
    py manage.py createsuperuser

5.Ejecutar el servidor de desarrollo:
    py manage.py runserver

    Accede a la aplicación en http://127.0.0.1:8000/


--------Estructura de Datos de Prueba-----------
Para probar las funcionalidades de filtrado y catálogo, ingresa a http://127.0.0.1:8000/admin/ y registra:

1.Categorías:
    -Monumento Histórico
    -Edificio Antiguo
    -Mural

2.Lugares Patrimoniales:
    -Reloj de Flores (Categoría: Monumento Histórico, Ubicación: Viña del Mar, Año: 1962)

    -Muelle Vergara (Categoría: Monumento Histórico, Ubicación: Viña del Mar, Año: 1894)

    -El Peral (Categoría: Monumento Histórico, Ubicación: Valparaíso, Año: 1902)

    -Museo a Cielo Abierto de Polanco (Categoría: Mural, Ubicación: Valparaíso, Año: 2012)

--------ROLES Y PERMISOS DE USUARIOS------------

    -Usuario Visitante (Anónimo): Puede acceder a la página principal (/) y consultar el catálogo con filtros (/catalogo/).

    -Usuario Autenticado (Administrador): Puede acceder al panel de gestión privado (/gestion/) para revisar la lista completa, agregar nuevos lugares o modificar los existentes.   

---------Ultimo paso para guardar todo en GitHub---------

Una vez modificado el 'README.md', presiona 'Ctrl + S' para guardar y ejecuta en la terminal:

En la terminal aplicamos estos comandos:
    git add .
    git commit -m "Documentacion README.md actualizada y requirements.txt listo"
    git push origin main