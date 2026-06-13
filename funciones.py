def saludar(nombre):
    print(f"Hola, {nombre}. Bienvenido.")

saludar("Jaime")
saludar("Ana")
saludar("Carlos")

def presentar(nombre, edad, ocupacion):
    print(f"Me llamo {nombre}, tengo {edad} años y soy {ocupacion}.")

presentar("Jaime", 41, "IT Engineer")
presentar("Ana", 28, "Desarrolladora")

def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(f"El resultado es {resultado}")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

mi_imc = calcular_imc(96, 1.80)
categoria = clasificar_imc(mi_imc)
print(f"Tu IMC es {mi_imc:.2f} - {categoria}")

def verificar_acceso(nombre, es_admin, años_experiencia):
    if es_admin:
        return "Acceso total al sistema."
    elif años_experiencia >= 3:
        return "Acceso limitado."
    else:
        return "Sin acceso."
acceso_jaime = verificar_acceso("Jaime", True, 5)
acceso_ana = verificar_acceso("Ana", False, 4)
acceso_carlos = verificar_acceso("Carlos", False, 1)
print(f"Jaime: {acceso_jaime}")
print(f"Ana: {acceso_ana}")
print(f"Carlos: {acceso_carlos}")

#verion mejorada de la función verificar_acceso
def verificar_acceso(nombre, es_admin, años_experiencia):
    if es_admin:
        return f"{nombre}: Acceso total."
    elif años_experiencia >= 3:
        return f"{nombre}: Acceso limitado."
    else:
        return f"{nombre}: Sin acceso."

print(verificar_acceso("Jaime", True, 5))
print(verificar_acceso("Ana", False, 4))
print(verificar_acceso("Carlos", False, 1))