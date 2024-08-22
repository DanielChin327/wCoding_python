def calculate_bills_and_coins(change):
    denominations = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
    }

    for denomination in denominations:
        if change >= denomination:
            denominations[denomination] = change // denomination # // discards the remainder
            change %= denomination # // rounds the change to the divisible number of the bill
    return denominations

def calculate_change(items, payment):
    sum_items = sum(items)
    change = payment - sum_items
    print(f"The cost is {sum_items}. The payment is {payment}")
    if change < 0:
        print("Your payment is insufficient")
    elif change == 0:
        print("Your payment is exact. There is no change due")
    elif change > 0:
        print(f"Your change due is : {change}")
        denominations = calculate_bills_and_coins(change)
        print("Here are the bills due: ")
        print(denominations)
        # for denomination, count in denominations.items():
        #     if count > 0:
        #         print(f"{denomination} won: {count}")

def start():
    while True:
        items = []
        while True:
            item = input("Write down item amounts: (type 'done' to finish): ")
            if item.lower() == 'done':
                break
            try:
                item = int(item)  # Convert the input to an integer
                items.append(item)
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        while True:
            payment = input("Write down your payment: ")
            try:
                payment = int(payment)  # Convert the payment to an integer
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        calculate_change(items, payment)

        repeat = input("Press any key to calculate another. Type 'stop' to stop: ")
        if repeat.lower() == 'stop':
            print("Have a nice day!")
            break

start()
