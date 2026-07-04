import random
secret = random.randint(1, 50)
attempts = 5
print("Welcome to the Number Guessing Game!")
print("Guess the secret number between 1 and 50.")
print("You have 5 lives ♥♥♥♥♥")
while attempts > 0:
    guess = int(input("\nEnter your guess: "))
    if guess == secret:
        print("Correct! You guessed the secret number!")
        break
    else:
        attempts -= 1
        difference = abs(secret - guess)
        if difference <= 3:
            hint = "Very close!"
        elif difference <= 10:
            hint = "Close!"
        else:
            hint = "Far away!"
        print(f"Wrong guess. Hint: {hint}")
        print("Lives left:", "♥" * attempts)
        if attempts == 0:
            print("\n Game Over! The secret number was:", secret)