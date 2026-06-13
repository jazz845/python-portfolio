def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b
def calcular(operacion, a, b):
    if operacion == "sumar":
        return sumar(a, b)
    elif operacion == "restar":
        return restar(a, b)
    elif operacion == "multiplicar":
        return multiplicar(a, b)
    elif operacion == "dividir":
        return dividir(a, b)
print(calcular("sumar", 10, 5))
print(calcular("restar", 10, 5))
print(calcular("multiplicar", 10, 5))
print(calcular("dividir", 10, 5))
print(calcular("dividir", 10, 0))