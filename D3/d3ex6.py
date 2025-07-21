#Contador de palabras de mas de 5 caracteres

lista_palabras = ["cacahuete", "albornoz", "pez", "gato", "abubilla"]

def contador(lista):
    cuenta = 0
    palabras_largas = []
    for p in lista:
        if len(p) > 5: #por cada objeto en la lista mira si tiene mas de 5 caracteres
            cuenta += 1 #suma 1 a cuenta
            palabras_largas.append(p) #mete en la lista vacia las largas
    return cuenta, palabras_largas

print(contador(lista_palabras))

