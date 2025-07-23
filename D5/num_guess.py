import random
import sys

num = random.randint(0, 10)

for guess_left in range(6 , 1 , -1):
    print(f"Guess the number, you have {guess_left} guesses left:")
    guess = int(input(">"))
    if num == guess:
        print("You gessed it!")
        sys.exit()
    elif guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
    else:
        break

print("You Lost!")
sys.exit()


