archivo = open("datos.txt", "r")

lineas = archivo.readlines()

numlines = 0
for num in lineas:
    numlines += 1

print(numlines)

