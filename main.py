from random import randint

random_num = randint (1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10"))
    # store it in a variable called guess.

    if guess > random_num:
        print("Too high!, Try again.")

    elif  guess < random_num:
        print("Print Too low!, Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break