#Ecjercicio fguncion numeros positivos
#lista a analizar
numlist=[3, -1, 0, 8, -5]
#metodo 1 list comprehension
def num_pos(lista):
    return [n for n in lista if n > 0]

#metdo 2 normal
def pos_num(lista):
    positives=[]  # Paso 1: Creamos una lista vacía para guardar los positivos
    for n in lista: # Paso 2: Recorremos cada número de la lista
        if n>0: # Paso 3: Si el número es mayor que cero...
            positives.append(n) # ... lo añadimos a la lista de positivos
    return positives # Paso 4: Al final, devolvemos la lista completa de positivos
         


print(pos_num(numlist))