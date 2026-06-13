dispositivos = ["MacBook", "iPhone", "iPad", "AirPods"]

print(dispositivos)
print(dispositivos[0])
print(dispositivos[2])
print(len(dispositivos))
print(dispositivos[-1])
print(dispositivos[-2])

dispositivos.append("Apple Watch")
print(dispositivos)

dispositivos.remove("iPad")
print(dispositivos)

dispositivos[0] = "MacBook Pro"
print(dispositivos)

usuario = {
    "nombre": "Jaime",
    "edad": 41,
    "ocupacion": "IT Engineer",
    "es_admin": True
}

print(usuario)
print(usuario["nombre"])
print(usuario["es_admin"])

usuario["edad"] = 42
usuario["ciudad"] = "Medellín"
del usuario["ocupacion"]

print(usuario)

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

empleados = [
    {"nombre": "Jaime", "rol": "IT Engineer", "activo": True},
    {"nombre": "Ana", "rol": "Desarrolladora", "activo": True},
    {"nombre": "Carlos", "rol": "Diseñador", "activo": False},
    {"nombre": "María", "rol": "DevOps", "activo": True},
]

for empleado in empleados:
    if empleado["activo"]:
        print(f"{empleado['nombre']} - {empleado['rol']}")

def buscar_empleado(nombre):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return empleado
    return "Empleado no encontrado."
print(buscar_empleado("Ana"))
print(buscar_empleado("Carlos"))
print(buscar_empleado("Pedro"))