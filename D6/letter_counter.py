letters = {}
word = input("Escribe una palabra\n>")

for letter in word:
    if letter in letters:
        letters[letter] += 1
    else: 
        letters[letter] = 1

print(letters)




