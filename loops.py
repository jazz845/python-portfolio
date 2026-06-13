numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

contador = 1

while contador <= 5:
    print(f"Vuelta número {contador}")
    contador = contador + 1

usuarios = [
    {"nombre": "Jaime", "es_admin": True},
    {"nombre": "Carlos", "es_admin": False},
    {"nombre": "Ana", "es_admin": True},
    {"nombre": "Pedro", "es_admin": False},
]
for usuario in usuarios:
    if usuario["es_admin"]:
        print(f"{usuario['nombre']} es administrador.")
    else:
        print(f"{usuario['nombre']} no es administrador.")

for usuario in usuarios:
    if usuario["es_admin"]:
        print(f"{usuario['nombre']} es administrador.")