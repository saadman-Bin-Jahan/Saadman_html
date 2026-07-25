import random
import math
lucky_number = random.randint(1, 100)
print("🎉 Your Lucky Number is:", lucky_number)
activities = [
    "Go for a walk",
    "Read a book",
    "Watch a movie",
    "Play a game",
    "Practice Python"
]
activity = random.choice(activities)
print("🎲 Random Activity:", activity)
secret = random.randint(1, 10)
print("\nGuess the secret number between 1 and 10.")
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("🎉 Correct! You guessed the number.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
number = float(input("\nEnter a decimal number: "))
a = int(input("Enter first integer for GCD: "))
b = int(input("Enter second integer for GCD: "))
print("\nMath Function Results")
print("---------------------")
print("ceil():", math.ceil(number))
print("floor():", math.floor(number))
print("fabs():", math.fabs(number))
print("copysign(5, number):", math.copysign(5, number))
print("gcd():", math.gcd(a, b))