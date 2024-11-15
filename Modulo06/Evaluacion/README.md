
# Guía de Configuración del Proyecto Django

Siga estos pasos para configurar y ejecutar el proyecto **"VENTA VIRTUAL DE VEHÍCULOS"**.

---

## 1. Requisitos Previos

- Tener **Python 3.8** o superior instalado.
- Instalar **pip**.
- Instalar **PostgreSQL** y asegurarse de que el servicio esté corriendo.

---

## 2. Descargar el Proyecto

Clone o descargue el repositorio del proyecto desde el siguiente enlace:

```
git clone [https://github.com/tantipann/bootcamp_python/tree/8f5175fde924d6197d906b8b9dc451dafe6a626e/Modulo06/Evaluacion/proyecto_vehiculos_django.git](https://github.com/tantipann/bootcamp_python/blob/c06b92fc6c9911aedb6da224cc69ca89cafc101a/Modulo06/Evaluacion/proyecto_vehiculos_django.rar)
```

Ingrese al directorio del proyecto:

```
cd proyecto_vehiculos_django
```

---

## 3. Crear y Activar el Entorno Virtual

1. Crear un entorno virtual con el siguiente comando:

```
python3 -m venv proyecto_vehiculos_django
```

2. Activar el entorno virtual:

**En Windows:**

```
proyecto_vehiculos_django\Scripts\activate
```

**En macOS/Linux:**

```
source proyecto_vehiculos_django/bin/activate
```

---

## 4. Instalar Dependencias

Ejecute el siguiente comando para instalar las librerías necesarias:

```
pip install -r requirements.txt
```

---

## 5. Configurar la Base de Datos PostgreSQL

1. Conéctese a PostgreSQL usando el cliente de línea de comandos:

```
psql -U postgres
```

2. Crear la base de datos **vehiculos_db**:

```
CREATE DATABASE vehiculos_db;
```

3. Crear un usuario con permisos para esta base de datos:

```
CREATE USER vehiculos_user WITH PASSWORD 'securepassword';
```

4. Conceder permisos al usuario sobre la base de datos:

```
GRANT ALL PRIVILEGES ON DATABASE vehiculos_db TO vehiculos_user;
```

5. Salir de PostgreSQL:

```
\q
```

---

## 6. Configuración en settings.py

Edite el archivo `settings.py` en el proyecto y configure la base de datos, *según el ejemplo anterior*:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vehiculos_db',
        'USER': 'vehiculos_user',
        'PASSWORD': 'securepassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 7. Cargar Estructura de la Base de Datos

1. Realice las migraciones para configurar la base de datos:

```
python manage.py makemigrations
python manage.py migrate
```

2. Crear un usuario administrador:

```
python manage.py createsuperuser
```

Siga las instrucciones para definir el nombre de usuario, correo electrónico y contraseña.

**Por ejemplo:**

```
usuario: admin
correo: admin@admin.cl
contraseña: admin
```

---

## 8. Ejecutar el Servidor

Inicie el servidor de desarrollo con el siguiente comando:

```
python manage.py runserver
```

Abra un navegador y vaya a [http://localhost:8000](http://localhost:8000) para ver la aplicación.

---

## 9. Navegación en el Sitio

La barra de navegación incluye enlaces a:

- **Inicio**: Redirige a la página principal.
- **Agregar**: Lleva al formulario para registrar un vehículo.
- **Listar**: Muestra el listado completo de los vehículos.

---

## 10. Funcionalidades del Proyecto

- **Barra de Navegación**: Incluye enlaces a las páginas de navegación del sito las cuales estan relacionadas con las funcionalidades **Inicio**, **Agregar Vehículos** y **Listar Vehículos**.
    *El acceso a las páginas depende de los permisos del usuario.*
  
- **Página de Inicio**: Muestra un mensaje de bienvenida.

- **Agregar Vehículos**: Formulario para ingresar nuevos vehículos a la base de datos.
    Se puede acceder tanto por el menú “Agregar” o como por la url http://localhost:8000/vehiculo/add
    *Esta opción está disponible únicamente para usuarios registrados que cuenten con permisos de "add_vehiculomodel".*

- **Listar Vehículos**: Tabla que muestra los vehículos existentes
    Su condición de precio se evalúa de acuerdo a las siguientes condiciones: **bajo**, entre 0 y 10000; **Medio**, para mayores de 10000 y 30000; y **alto**, para
mayores de 30000. .
    *Esta funcionalidad solo está disponible para usuarios registrados que posean el permiso de "visualizar_catalogo".*

---

## 11. Problemas Comunes

- **Error de base de datos**: Verifique que ha ejecutado las migraciones correctamente y que la configuración de `settings.py` es correcta.


© 2024 **VENTA VIRTUAL DE VEHÍCULOS**. Todos los derechos reservados.
