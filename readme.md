# TuPrimeraPaginaScalzo   
Proyecto final del curso de Python 2025 – Plataforma ecommerce desarrollada con Django.  

Esta aplicación simula una **tienda online** con funcionalidades de gestión de productos, registro de usuarios, perfiles, mensajería entre usuarios, y más.  

---

## Funcionalidades principales

- **Herencia de plantillas** (`base.html`) con bloques reutilizables
- **Modelo principal: Producto** con:
  - Nombre (CharField)
  - Marca (CharField)
  - Descripción enriquecida (CKEditor)
  - Imagen (ImageField)
  - Fecha de creación
- Formularios para:
  - Crear productos, categorías y marcas
  - Editar y eliminar productos (solo para staff)
- Visualización de productos en tarjetas
- Detalle individual de cada producto
- Buscador por nombre, categoría o marca
- Páginas: Home, About, Productos
- Diseño responsive basado en plantilla **Start Bootstrap**
- Sistema de autenticación:
  - Registro, login, logout
  - Validaciones de email único
  - Vista de perfil y edición de datos (nombre, email, avatar, bio, fecha)
  - Cambio de contraseña desde el perfil
- Uso de:
  - 2 CBV
  - 1 Mixin (`LoginRequiredMixin`)
  - 1 Decorador (`@staff_member_required`)
- Mensajes con `messages.success()` luego de acciones

---

## Cómo correr el proyecto

# 1. Clonar el repositorio
git clone https://github.com/pauscalzo/TuPrimeraPaginaScalzo.git
cd TuPrimeraPaginaScalzo

# 2. Crear entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Migrar la base de datos
python manage.py migrate

# 5. Crear superusuario (opcional para admin)
python manage.py createsuperuser

# 6. Levantar el servidor
python manage.py runserver

Accedé a la aplicación en:  
http://127.0.0.1:8000/

---

## Orden de prueba sugerido

1. Registrate o iniciá sesión
2. Accedé al perfil y probá editar tus datos y cambiar tu avatar
3. Cargá una nueva **categoría** y una nueva **marca**
4. Cargá un **producto nuevo** (debe tener imagen y descripción enriquecida)
5. Navegá al listado de productos y usá el **buscador**
6. Hacé clic en “Leer más” para ver el detalle
7. Si sos staff, probá **editar y eliminar** productos

---

## Autora

Paula Scalzo  