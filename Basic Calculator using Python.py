def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

while True:
    print("\nOptions: 1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")
    choice = input("Enter choice: ")

    if choice == "5":
        print("Calculator closed.")
        break

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(x, y))
    elif choice == "2":
        print("Result:", subtract(x, y))
    elif choice == "3":
