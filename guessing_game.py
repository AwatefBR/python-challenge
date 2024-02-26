"""
A very simple guessing game
"""
import random


computer_choice = random.randint(1, 99)
count = 0

while True:
    user_guess = input("Please enter a number between 1 and 99") 
    if user_guess.isdigit() == False:
        count = +1
        print("ERROR :This is not a number. Enter a number between 1 and 99. TRY AGAIN")
    else:
        user_guess = int(user_guess)
        if user_guess > 99 or user_guess < 1 :
            print("sorry, your number is not between 1 and 99. TRY AGAIN")
        else:
            count += 1
            if user_guess > computer_choice :
                count = +1
                print("Too high! TRY AGAIN")
            elif user_guess < computer_choice :
                count += 1
                print("Too low ! TRY AGAIN")
            elif user_guess == computer_choice :
                count += 1
                print(f"Congratulations ! you guessed right. It took you {count} guesses")
                break