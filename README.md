# Restaurante App - Semana 11

## Datos del estudiante

**Nombre:** Stefany Gallegos Zari
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 11

## Descripción

Este proyecto corresponde a la evolución de la aplicación restaurante_app desarrollada durante las semanas anteriores.

En esta versión se incorporan colecciones para administrar productos, usuarios y ventas, además de una operación de venta que relaciona un usuario con un producto.

La aplicación permite registrar usuarios, registrar productos, consultar información, realizar ventas, controlar el stock y consultar las ventas realizadas por un usuario.

También se incorpora persistencia mediante archivos JSON para conservar la información después de cerrar y volver a ejecutar el programa.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md
