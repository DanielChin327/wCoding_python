def calculate_bills_and_coins(change):
    change_counter = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
    }

    for counter in change_counter:
        if change >= counter:
            change_counter[counter] = change // counter # // discards the remainder 9000 / 5000 -> 1
            change %= counter # // collects the remainder  9000 % 5000 -> results in 4000
    return change_counter

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
        change_back = calculate_bills_and_coins(change)
        print("Here are the bills due: ")
        print(change_back)
        for change, count in change_back.items(): #change is key, count is value
            if count > 0:
                print(f"{change} won: {count}")

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
