inventario = [
    {"nombre": "Laptop", "precio": 2500, "stock": 5},
    {"nombre": "Mouse", "precio": 50, "stock": 20},
    {"nombre": "Teclado", "precio": 120, "stock": 10},
    {"nombre": "Monitor", "precio": 800, "stock": 0},
    {"nombre": "Audifonos", "precio": 150, "stock": 8}
]

def listar_productos():
    print("=== INVENTARIO ===")
    for producto in inventario:
        print(
            f"Nombre: {producto['nombre']}, "
            f"Precio: ${producto['precio']}, "
            f"Stock: {producto['stock']}"
        )

def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return "Producto no encontrado."

def productos_disponibles():
    for producto in inventario:
        if producto["stock"] > 0:
            print(f"{producto['nombre']} - Stock: {producto['stock']}")

listar_productos() 
print(buscar_producto("Mouse"))
print(buscar_producto("Tablet"))
print("=== PRODUCTOS DISPONIBLES ===")
productos_disponibles() 