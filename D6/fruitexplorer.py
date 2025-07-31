
try:
    with open("frutas.txt", "r+") as archivo:
        archivo.write("melocoton\nuvasnispero\nalbaricoque\nlimon\nnaranja")
        
    with open("frutas.txt", "r") as archivo:
        frutas = archivo.readlines()
       
        for fruta in frutas:
            
            fruta_limpia = fruta.strip()
            
            if len(fruta_limpia) > 5:
                print (fruta_limpia)

except:
    print("Error!")
        
