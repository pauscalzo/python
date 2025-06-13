TuPrimeraPaginaScalzo
Proyecto realizado con Django para la entrega del curso de Python.
Consiste en una tienda online que permite administrar productos, categorías y marcas. Se pueden crear, visualizar y buscar productos.

- Funcionalidades principales
* Herencia de plantillas con base.html

* Modelo con 3 clases: Producto, Categoría, Marca

* Formulario para:

_Crear nueva marca

_Crear nueva categoría

_Cargar un nuevo producto (con imagen)

* Visualización de productos en cards con modales

* Buscador para filtrar productos por nombre

* Navegación con secciones ancladas (#nosotros, #comprar)

* Diseño responsive basado en plantilla Start Bootstrap

- Cómo probar el proyecto
1- Clonar el repositorio:
git clone https://github.com/usuario/TuPrimeraPaginaScalzo.git
cd TuPrimeraPaginaScalzo

2- Crear y activar entorno virtual:
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows

3- Instalar dependencias:
pip install -r requirements.txt

4- Migrar base de datos:
python manage.py migrate

5- Levantar el servidor:
python manage.py runserver

6- Acceder a:
http://127.0.0.1:8000/

- Orden de prueba sugerido
Desde la home, dirigite a:

+ Marca para crear una marca

+ Categoría para crear una categoría

+ Producto para subir un producto (debe haber marcas y categorías previamente creadas)

Volvé a la home y verificá que los productos aparecen en la sección Productos

Probá el buscador ingresando el nombre de un producto, la marca o la categoría.

Hecho por Paula Scalzo – Proyecto para curso de Python 2025