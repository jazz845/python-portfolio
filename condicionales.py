edad = 41

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres niño.")

nombre = "Jaime"

if nombre == "Jaime":
    print("Bienvenido, Jaime.")
else:
    print("No te conozco.")

tiene_documento = True

if edad >= 18 and tiene_documento == True:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")

es_admin = False
es_supervisor = False

if es_admin or es_supervisor:
    print("Tiene acceso al sistema.")
else:
    print("Acceso denegado.")

años_experiencia = 1

if es_admin == True:
    print("Acceso total al sistema.")
elif años_experiencia >= 3:
    print("Acceso limitado.")
else:
    print("Sin acceso.")