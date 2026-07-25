while True:
    try:
        bill = float(input("Enter shopping bill amount: $"))
        discount = float(input("Enter discount percentage: "))
        if bill < 0:
            raise ValueError("Bill amount cannot be negative.")
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100.")
    except ValueError as e:
        print("Value Error:", e)
    except TypeError:
        print("Type Error: Invalid data type.")
    else:
        discount_amount = bill * (discount / 100)
        final_amount = bill - discount_amount
        print("\nShopping Summary")
        print("----------------")
        print(f"Original Bill : ${bill:.2f}")
        print(f"Discount      : {discount:.2f}%")
        print(f"You Save      : ${discount_amount:.2f}")
        print(f"Final Bill    : ${final_amount:.2f}")
        break
    finally:
        print("Program cycle completed.\n")