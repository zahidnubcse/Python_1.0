import random

secret_number = random.randint(1, 10)

print("Welcome to Number Guessing Game!!")
print ("Let's think a number between 1 and 10")

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
     print("Congratulation!! you guess the correct number")
     break

    elif guess > secret_number:
     print ("Try again..You guess too high number")

    else:
     print ("Try again..You guess too low number.")    