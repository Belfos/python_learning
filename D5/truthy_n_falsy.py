
#strings vacias devuelven false
name = ''
while not name:
    print('Enter your name:')
    name = input('>')
print('How many guests will you have?')
#ints y floats con valor 0 devuelven false
num_of_guests = int(input('>'))
if num_of_guests:
    print('Be sure to have enough room for all your guests.')
print('Done')
