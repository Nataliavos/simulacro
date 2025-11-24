# Inventory and Sales Management System

Sistema integral de gestión de inventario y ventas para una tienda de electrónica, con reportes dinámicos basados en las ventas realizadas.

> **Importante:**  
> - Todas las interacciones con el usuario (menús y mensajes) están en **inglés**, como pide el enunciado.  
> - Los **comentarios y docstrings en el código están en español** para ayudarte a entender la lógica.

---

## 1. Objetivo del sistema

Simular un sistema de consola que permita:

- Gestionar el inventario (CRUD de productos).
- Registrar ventas con validación de stock.
- Aplicar descuentos según tipo de cliente.
- Generar reportes:
  - Top 3 productos más vendidos.
  - Ventas agrupadas por marca.
  - Ingresos brutos y netos.
  - Rendimiento del inventario (stock vs ventas).

Todo esto usando:

- Listas y diccionarios anidados.
- Módulos y funciones cortas.
- Manejo básico de excepciones.
- Al menos una función `lambda` para cálculos agregados.

---

## 2. Estructura del proyecto

```text
inventory_system/
├── main.py        # Punto de entrada, menú principal
├── models.py      # Modelos de dominio (productos, ventas, descuentos)
├── utils.py       # Funciones utilitarias (validaciones, mensajes)
├── inventory.py   # CRUD de productos (inventario)
├── sales.py       # Registro y consulta de ventas
└── reports.py     # Módulo de reportes
