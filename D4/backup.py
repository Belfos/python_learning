#Crea una copia _backup de un archivo

archivo = input("Nombre del archivo.txt: ")
partes = archivo.split(".")
nuevo_archivo = f"{partes[0]}_backup.{partes[1]}"
try:
    with open(archivo, "r") as fuente:
        contenido = fuente.read()
    with open(nuevo_archivo, "w") as backup:
        backup.write(contenido)
except:
    print("Algo salio mal")



    


