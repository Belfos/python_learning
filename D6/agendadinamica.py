agenda = {}

while True:
    action = int(input("What do you want to do?\n1. Add contact\n2. Search\n3. Salir\n>"))
    if action == 1:
        name = input("Enter name\n>")
        number = input("Enter number\n>")
        agenda[name] = number
      
    elif action == 2:
        if not agenda:
            print("The agenda is empty!")
        else:
            print("Available contacts:")
            for nombre in agenda:
                print(f" - {nombre}")
            
            src_input = input("Enter contact name:\n> ")#source input de busqueda de contacto en la agenda
            if src_input in agenda:#si el nombre está en la agenda
                print(f"{src_input}'s number is: {agenda[src_input]}")#Devuelve el numero correspondiente al nombre
            else:
                print("Contact name not found!")
    elif action == 3:
        break
    else:
        print("INVALID INPUT")

        
        



    