def calculate_change(paid, ticket_price):
    change = paid - ticket_price
    if change == 0:
        pass  
    return change
def parking_ticket_payment():
    ticket_price = float(input("Enter parking ticket amount: $"))
    total_paid = 0.0
    print("Accepted coins: 0.25, 0.50, 1.00, 2.00")
    print("Enter 0 to finish inserting coins.")
    while total_paid < ticket_price:
        coin = float(input("Insert coin: $"))
        if coin == 0:
            break
        if coin not in [0.25, 0.50, 1.00, 2.00]:
            print("Invalid coin. Try again.")
            continue
        total_paid += coin
        print(f"Total inserted: ${total_paid:.2f}")
    if total_paid < ticket_price:
        print("Payment cancelled. Not enough money.")
        return
    change = calculate_change(total_paid, ticket_price)
    print("\nPayment successful!")
    print(f"Ticket Price : ${ticket_price:.2f}")
    print(f"Paid         : ${total_paid:.2f}")
    print(f"Change       : ${change:.2f}")
parking_ticket_payment()
