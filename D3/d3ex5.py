# Ejercicio 5: Suma de caracteres

total_letras=0

while True:
    palabras = input("Escribe cualquier palabra: ").strip(" ")
    if palabras.lower() == "fin":
        break
    total_letras+=len(palabras)

print("total letras escritas", total_letras)
   
    