# try:
#     archivo = open("numeros.txt", "r+")

#     archivo.write("1\n")
#     archivo.write("2\n")
#     archivo.write("3\n")
#     archivo.write("4\n")
#     archivo.write("5\n")
#     archivo.write("6\n")
#     archivo.close()
    
# except:
#     print("sorry")

try:
    # Primero escribe
    with open("numeros.txt", "w") as archivo:
        archivo.write("1\n2\n3\n4\n5\n6\n")
    
    # Luego lee
    with open("numeros.txt", "r") as archivo:
        print(archivo.read())
except:
    print("sorry")