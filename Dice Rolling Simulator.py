import random

while True:
    roll = input("Press Enter to roll the dice or type 'exit' to quit: ")
    if roll.lower() == "exit":
        print("Game closed.")
        break
    side = random.randint(1, 6)
    print("You rolled:", side)
