# Certamen 2 - Fundación Patrimonio Vivo

Proyecto web desarrollado en **Django y Bootstrap** para la gestión y difusión de lugares de interés patrimonial en Chile.

## Requisitos Previos

Antes de instalar el proyecto, asegúrate de contar con los siguientes programas:

- Python 3.10 o superior.
- Git.

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/st1venssj/CER2-ZURITASTEVEN.git
cd CER2-ZURITASTEVEN
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Aplicar migraciones de la base de datos

```bash
py manage.py makemigrations
py manage.py migrate
```

### 4. Crear superusuario para la administración y pruebas

```bash
py manage.py createsuperuser
```

### 5. Ejecutar el servidor de desarrollo

```bash
py manage.py runserver
```

Accede a la aplicación desde el siguiente enlace:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Estructura de Datos de Prueba

Para probar las funcionalidades de filtrado y catálogo, ingresa al panel de administración:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Registra las siguientes categorías y lugares patrimoniales:

### 1. Categorías

- Monumento Histórico
- Edificio Antiguo
- Mural

### 2. Lugares Patrimoniales

| Nombre | Categoría | Ubicación | Año |
|---|---|---|---|
| Reloj de Flores | Monumento Histórico | Viña del Mar | 1962 |
| Muelle Vergara | Monumento Histórico | Viña del Mar | 1894 |
| El Peral | Monumento Histórico | Valparaíso | 1902 |
| Museo a Cielo Abierto de Polanco | Mural | Valparaíso | 2012 |

---

## Roles y Permisos de Usuarios

### Usuario Visitante (Anónimo)

- Puede acceder a la página principal (`/`).
- Puede consultar el catálogo de lugares patrimoniales con filtros (`/catalogo/`).

### Usuario Autenticado (Administrador)

- Puede acceder al panel de gestión privado (`/gestion/`).
- Puede revisar la lista completa de lugares patrimoniales.
- Puede agregar nuevos lugares.
- Puede modificar los lugares existentes.

---

## Último Paso: Guardar los Cambios en GitHub

Una vez modificado el archivo `README.md`, presiona `Ctrl + S` para guardar los cambios.

Luego, ejecuta los siguientes comandos en la terminal:

### 1. Agregar los archivos modificados

```bash
git add .
```

### 2. Crear un commit

```bash
git commit -m "Documentacion README.md actualizada y requirements.txt listo"
```

### 3. Subir los cambios a GitHub

```bash
git push origin main
```

