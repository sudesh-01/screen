import random

guesses = 0
num = random.randint(1, 100)
print("Hello, I am thinking of a number between 1 to 100, can you guess?")
while guesses < 7:
    print("Take a guess, enter your choice.")
    guess = int(input())
    guesses = guesses + 1
    if guess > num:
        print("high")
    if guess < num:
        print("low")
    if guess == num:
        break

if guess != num:
    num = str(num)
    guesses = str(guesses)
    print("Oops! Sorry, the number is " + num)
    print("It took you " + guesses + " guesses.")
if guess == num:
    guesses = str(guesses)
    num = str(num)
    print("correct")
    print("The number is " + num)
    print("It took you " + guesses + " guesses.")




