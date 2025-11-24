# models.py
"""
Modelos de dominio y constantes para el sistema de inventario y ventas.
"""

from datetime import datetime

# Diccionario con los tipos de cliente y su descuento asociado (en forma decimal)
# regular -> 0%, vip -> 10%, wholesale -> 15%
CUSTOMER_DISCOUNTS = {
    "regular": 0.0,
    "vip": 0.10,
    "wholesale": 0.15,
}


def create_initial_inventory():
    """
    Crear el inventario inicial con 5 productos precargados.

    Cada producto es un diccionario con:
    - id: identificador único del producto
    - name: nombre del producto
    - brand: marca
    - category: categoría
    - unit_price: precio unitario
    - stock: cantidad en inventario
    - warranty_months: garantía en meses
    - total_sold: cantidad total vendida (para reportes)
    """
    return [
        {
            "id": 1,
            "name": "Smartphone X100",
            "brand": "TechWave",
            "category": "Smartphone",
            "unit_price": 350.0,
            "stock": 20,
            "warranty_months": 12,
            "total_sold": 0,
        },
        {
            "id": 2,
            "name": "Laptop Pro 15",
            "brand": "ByteBook",
            "category": "Laptop",
            "unit_price": 950.0,
            "stock": 10,
            "warranty_months": 24,
            "total_sold": 0,
        },
        {
            "id": 3,
            "name": "Wireless Headphones",
            "brand": "SoundMax",
            "category": "Audio",
            "unit_price": 80.0,
            "stock": 30,
            "warranty_months": 6,
            "total_sold": 0,
        },
        {
            "id": 4,
            "name": "4K Smart TV 55\"",
            "brand": "VisionPlus",
            "category": "TV",
            "unit_price": 650.0,
            "stock": 8,
            "warranty_months": 18,
            "total_sold": 0,
        },
        {
            "id": 5,
            "name": "Bluetooth Speaker",
            "brand": "SoundMax",
            "category": "Audio",
            "unit_price": 45.0,
            "stock": 25,
            "warranty_months": 6,
            "total_sold": 0,
        },
    ]


def create_sale_record(
    sale_id,
    customer_name,
    customer_type,
    product,
    quantity,
    discount_rate,
):
    """
    Crear y devolver un diccionario que representa una venta.

    Parámetros:
    - sale_id: identificador único de la venta
    - customer_name: nombre del cliente
    - customer_type: tipo de cliente (regular, vip, wholesale)
    - product: diccionario de producto tomado del inventario
    - quantity: cantidad vendida
    - discount_rate: tasa de descuento en forma decimal (0.10 = 10%)

    Cálculos:
    - gross_amount: total bruto (precio * cantidad)
    - discount_amount: valor del descuento aplicado
    - net_amount: total neto después del descuento
    """
    unit_price = product["unit_price"]
    gross_amount = unit_price * quantity
    discount_amount = gross_amount * discount_rate
    net_amount = gross_amount - discount_amount

    return {
        "id": sale_id,
        "customer_name": customer_name,
        "customer_type": customer_type,
        "product_id": product["id"],
        "product_name": product["name"],
        "brand": product["brand"],
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_rate": discount_rate,
        "discount_amount": discount_amount,
        "gross_amount": gross_amount,
        "net_amount": net_amount,
        # Fecha y hora actual como string legible
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
