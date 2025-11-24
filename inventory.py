# inventory.py
"""
Módulo de inventario: operaciones CRUD sobre productos.
"""

from utils import (
    input_non_empty_string,
    input_int,
    input_float,
    print_error,
    print_success,
)


def get_next_product_id(inventory):
    """
    Obtener el siguiente ID disponible para un producto.

    - Si el inventario está vacío, devuelve 1.
    - Si ya hay productos, toma el máximo id y suma 1.
      Esto permite que, aunque se borren productos, no se repitan IDs.
    """
    if not inventory:
        return 1
    max_id = max(p["id"] for p in inventory)
    return max_id + 1


def find_product_by_id(inventory, product_id):
    """
    Buscar un producto por su ID dentro del inventario.

    - inventory: lista de diccionarios de productos
    - product_id: entero con el ID a buscar

    Devuelve:
    - el producto (diccionario) si lo encuentra
    - None si no existe
    """
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def list_products(inventory):
    """
    Listar todos los productos del inventario.

    Si no hay productos, muestra un mensaje indicando que
    el inventario está vacío.
    """
    if not inventory:
        print("\nNo products in inventory.\n")
        return

    print("\n--- Inventory ---")
    for product in inventory:
        # Se imprime cada campo importante del producto
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Brand: {product['brand']} | "
            f"Category: {product['category']} | "
            f"Price: {product['unit_price']:.2f} | "
            f"Stock: {product['stock']} | "
            f"Warranty: {product['warranty_months']} months"
        )
    print("-----------------\n")


def add_product(inventory):
    """
    Agregar un nuevo producto al inventario.

    Flujo:
    - Solicita nombre, marca, categoría, precio, stock y garantía.
    - Valida cada campo usando funciones de utils.
    - Asigna un ID automático.
    - Añade el producto a la lista de inventario.
    """
    print("\n=== Add New Product ===")

    # Se piden datos básicos del producto
    name = input_non_empty_string("Product name: ")
    brand = input_non_empty_string("Brand: ")
    category = input_non_empty_string("Category: ")

    # Validación: precio no negativo
    unit_price = input_float("Unit price: ", min_value=0.0)

    # Validación: stock no negativo
    stock = input_int("Stock quantity: ", min_value=0)

    # Validación: garantía no negativa
    warranty = input_int("Warranty (months): ", min_value=0)

    # Se genera el nuevo ID
    product_id = get_next_product_id(inventory)

    # Diccionario que representa el nuevo producto
    new_product = {
        "id": product_id,
        "name": name,
        "brand": brand,
        "category": category,
        "unit_price": unit_price,
        "stock": stock,
        "warranty_months": warranty,
        # Campo para reportes: cuánto se ha vendido de este producto
        "total_sold": 0,
    }

    # Se añade al inventario
    inventory.append(new_product)
    print_success(f"Product '{name}' added with ID {product_id}.")


def update_product(inventory):
    """
    Actualizar los datos de un producto existente.

    Flujo:
    - Muestra el inventario.
    - Pide el ID del producto a actualizar.
    - Permite cambiar nombre, marca, categoría, precio, stock y garantía.
    - Si se deja un campo vacío, se conserva el valor anterior.
    - Realiza validaciones básicas para los valores numéricos.
    """
    print("\n=== Update Product ===")

    if not inventory:
        print_error("Inventory is empty.")
        return

    # Primero se listan productos para que el usuario vea los IDs
    list_products(inventory)

    product_id = input_int("Enter product ID to update: ", min_value=1)
    product = find_product_by_id(inventory, product_id)

    if not product:
        print_error("Product not found.")
        return

    print("Press ENTER to keep the current value.\n")

    # Para cada campo textual, si el usuario escribe algo se actualiza
    new_name = input(f"New name ({product['name']}): ").strip()
    if new_name:
        product["name"] = new_name

    new_brand = input(f"New brand ({product['brand']}): ").strip()
    if new_brand:
        product["brand"] = new_brand

    new_category = input(f"New category ({product['category']}): ").strip()
    if new_category:
        product["category"] = new_category

    # Para los campos numéricos, se permite dejar vacío para no cambiar
    new_price_raw = input(
        f"New unit price ({product['unit_price']}): "
    ).strip()
    if new_price_raw:
        try:
            new_price = float(new_price_raw)
            if new_price < 0:
                print_error("Price cannot be negative. Keeping old value.")
            else:
                product["unit_price"] = new_price
        except ValueError:
            print_error("Invalid number. Keeping old value.")

    new_stock_raw = input(f"New stock ({product['stock']}): ").strip()
    if new_stock_raw:
        try:
            new_stock = int(new_stock_raw)
            if new_stock < 0:
                print_error("Stock cannot be negative. Keeping old value.")
            else:
                product["stock"] = new_stock
        except ValueError:
            print_error("Invalid integer. Keeping old value.")

    new_warranty_raw = input(
        f"New warranty months ({product['warranty_months']}): "
    ).strip()
    if new_warranty_raw:
        try:
            new_warranty = int(new_warranty_raw)
            if new_warranty < 0:
                print_error("Warranty cannot be negative. Keeping old value.")
            else:
                product["warranty_months"] = new_warranty
        except ValueError:
            print_error("Invalid integer. Keeping old value.")

    print_success("Product updated successfully.")


def delete_product(inventory):
    """
    Eliminar un producto del inventario.

    Flujo:
    - Muestra el inventario.
    - Pide el ID del producto.
    - Pide confirmación antes de borrar.
    - Elimina el producto de la lista si el usuario confirma.
    """
    print("\n=== Delete Product ===")

    if not inventory:
        print_error("Inventory is empty.")
        return

    list_products(inventory)
    product_id = input_int("Enter product ID to delete: ", min_value=1)
    product = find_product_by_id(inventory, product_id)

    if not product:
        print_error("Product not found.")
        return

    # Confirmación de seguridad
    confirm = input(
        f"Are you sure you want to delete '{product['name']}'? (y/n): "
    ).strip().lower()

    if confirm == "y":
        inventory.remove(product)
        print_success("Product deleted.")
    else:
        print("\nDeletion cancelled.\n")
