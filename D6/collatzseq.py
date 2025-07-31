

def collatz(number):    
    if number % 2 == 0:
        result = number // 2    
    else:
        result = 3 * number + 1
    print(result, end=" ")    
    return result

try:
    number = int(input("Enter number:\n"))
    print(number, end=' ')
    while number != 1:
        number = collatz(number)
except ValueError:
    print("Enter a valid integer")