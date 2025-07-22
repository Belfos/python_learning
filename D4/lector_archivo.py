try:
    archivo = open("datos.txt", "r")
    data = archivo.read()
    print(data)
    archivo.close()
except Exception as e:
    print("Error:", e)


