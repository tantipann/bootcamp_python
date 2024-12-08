
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
git clone https://github.com/tantipann/bootcamp_python/tree/8f5175fde924d6197d906b8b9dc451dafe6a626e/Modulo06/Evaluacion/proyecto_vehiculos_django.git [https://github.com/tantipann/bootcamp_python/blob/c06b92fc6c9911aedb6da224cc69ca89cafc101a/Modulo06/Evaluacion/proyecto_vehiculos_django.rar](https://github.com/tantipann/bootcamp_python/tree/15c56db05eb9e84d0846a1ef3c962804a71b08d9/Modulo06/Evaluacion)
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

1. Ingrese a la carpeta del proyecto:

```
cd config
```

2. Realice las migraciones para configurar la base de datos:

```
python manage.py makemigrations
python manage.py migrate
```

3. Crear un usuario administrador:

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
- **Iniciar Sesion**: Lleva al formulari de inicio de sesion
- **Cerrar Sesion**: Cierra la sesion activa.

---

## 10. Funcionalidades del Proyecto

 **1. Inicio de Sesión (Login)**
- Permite a los usuarios autenticarse en el sistema.
- Acceso controlado basado en credenciales registradas previamente.

 **2. Cierre de Sesión (Logout)**
- Funcionalidad que garantiza la seguridad cerrando la sesión activa del usuario.
- Redirecciona a la página de Inicio

**3. Página de Inicio**
- Muestra un mensaje de bienvenida.
- Sirve como punto de acceso a las demás funcionalidades.

**4. Registrar Usuarios**
- Permite registrar nuevos usuarios en el sistema.
- Los usuarios registrados reciben automáticamente permisos de `visualizar_catalogo`.
- Redirección a la página de inicio después del registro exitoso.

**5. Agregar Vehículos**
- Formulario para registrar nuevos vehículos en la base de datos.
- Acceso controlado mediante el permiso específico `add_vehiculo`.
- Se accede desde la barra de navegacion de desde la URL: `http://localhost:8000/vehiculo/add`.

**6. Listar Vehículos**
- Muestra una tabla con los vehículos registrados en el sistema.
- La tabla clasifica los vehículos según su precio en categorías: **bajo**, **medio** y **alto** dependiendo de una condición de precio.
- Acceso limitado a usuarios con el permiso `"visualizar_catalogo"`.

**7. Interfaz de Administración**
- Acceso reservado para usuarios con permisos de administrador y permisos específicos según configuración.
- Permite gestionar directamente la base de datos del sistema.
- Algunos usuarios no administradores pueden tener acceso limitado para agregar vehículos u otras funcionalidades según los permisos asignados.

**8. Barra de Navegación Dinámica**
- Muestra enlaces como **Inicio**, **Agregar**, **Listar**, **Registrar Usuario**, y otros.
- Los enlaces se ajustan según los permisos del usuario autenticado, asegurando una experiencia personalizada y segura.

---

### Nota
El sistema utiliza permisos detallados para garantizar que cada usuario acceda solo a las funcionalidades para las que está autorizado. Esto asegura la integridad y la seguridad de los datos.

## 11. Problemas Comunes

- **Error de base de datos**: Verifique que ha ejecutado las migraciones correctamente y que la configuración de `settings.py` es correcta.


© 2024 **VENTA VIRTUAL DE VEHÍCULOS**. Todos los derechos reservados.
