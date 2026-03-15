# django-coderhouse-project
## Descripción
Este projecto es una aplicación web desarrollada con Django para el curso de Coderhouse, utiliza el patron MVT (Model - View - Template).

La aplicación simula un pequeño sistema de inventario IT donde se pueden registrar insumos, usuarios y estaciones de trabajo, además de realizar búsquedas de insumos en la base de datos.

***

## Tecnologías usadas
- Python
- Django 
- HTML
- Bootstrap 5
- SQLite (BD de Django por defecto)

***

## Modelos implementados
El projecto incluye tres modelos principales
### Insumo
Representa materiales o insumos del inventario. cosas como Ram, SSDs, o cajas de cable de red y herramientas como testers y pasa cables.

**Campos:**
- name
- category
- amount
### User
Representa la gente que trabaja en la officina, los usuarios del Área de IT, en futuro serán referenciados directamente que hacen revisan workstations o encargados de que tareas o proyectos.

**Campos:**
- name
- email

nota: en el futuro tendrían proyectos encargados
### WorkStation
Representa las computadoras a las que le brindamos servicio.

**Campos:**
- ws_number
- origin
- state
- location
- looked_by (esto no esta relacionado aun con usuarios)
- comments
- date_received

***

## Funcionalidades
la aplicación incluye las siguientes funciones:
- alta de insumos
- alta de usuarios
- alta de workstations
- búsqueda de insumos por nombre
- uso de herencia de plantillas HTML
- formularios basados en ModelForm

***

## Orden para probar la aplicación
1. Acceder a la pagina principal
2. crear un insumo
3. crear un usuario
4. crear una workstation
5. buscar un insumo
   Se puede ingresar un nombre o parte del nombre del insumo para realizar la búsqueda

***

## Estructura general del proyecto

El proyecto utiliza el patrón MVT:

- Models: definición de las entidades de la base de datos
- Views: lógica de la aplicación
- Templates: renderizado de la interfaz HTML

También se utiliza herencia de plantillas con un template base (index.html) del cual heredan las demás páginas.

***

## Futuras Addictions y cambios
Una lista de cosas que me gustaría agregar:

- buscar los otros modelos
- forms para actualizar y borrar
- un nuevo modelo llamado projecto o tarea (acompañado por sus forms)
- agregar una asociación entre workstation y los usuarios que la revisan