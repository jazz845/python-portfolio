peso = 96
altura = 1.80
IMC = peso / (altura ** 2)

if IMC < 18.5:
    print("Bajo peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
else:
    print("Obesidad")