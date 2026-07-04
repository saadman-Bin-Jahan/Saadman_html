rows = int(input("Enter number of rows: "))

i = 1
while i <= rows:
    # Print spaces first
    j = 1
    while j <= rows - i:
        print(" ", end="")
        j += 1
    
    # Print stars next
    k = 1
    while k <= i:
        print("*", end="")
        k += 1
    
    print()  # Move to next line
    i += 1