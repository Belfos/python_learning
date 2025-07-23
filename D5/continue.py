#continue vuelve a niniciar el bucle si una condicion es false

while True:
    print("Who are you?")
    name = input(">")
    #si el nombre no es pablo vuelve al while
    if name != "Pablo":
        continue
    
    print("Hello Pablo. Password? (its a dog breed)")
    password = input(">")
    if password == "labrador":
        break

print("Access granted")


