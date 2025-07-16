#lista de personas

personas = [{}]

while True:
    nombre = input("Nombre/salir: ")
    if nombre.lower() == "salir":
        break
    edad = int(input("Edad: "))
    personas.append({"nombre": nombre, "edad": edad})

print(personas)