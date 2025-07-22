
contador = 0
with open("datos.txt", "r") as file:
    for line in file:
        print(line)
        words= line.split()
        contador += len(words)
    print(f"El documento contiene {contador} palabras.")
