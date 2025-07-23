import sys

#este programa solo se cierra si escribes exit con sys.exit
while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')