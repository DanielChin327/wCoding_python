items = {
    'potion': {'quantity': 20, 'price': 100},
    'hi-potion': {'quantity': 5, 'price': 500},
    'antidote': {'quantity': 10, 'price': 50},
    'phoenix-down': {'quantity': 5, 'price': 200},
}

shopping_cart = {}

def add_to_shopping_cart(item, quantity):
    if item in shopping_cart:
        shopping_cart[item] += quantity
    else:
        shopping_cart[item] = quantity

def sell_item(item):
    while True:
        if item in items:
            quantity = input('How many?: ')
            try:
                quantity = int(quantity)
                if items[item]['quantity'] < quantity:
                    print("We don't have enough...")
                else:
                    items[item]['quantity'] -= quantity
                    add_to_shopping_cart(item, quantity)
                    print(f"Added {quantity} {item}(s) to your shopping cart.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("\nWe don't carry that item.")
            break

def cancel_item(item):
    if item in shopping_cart:
        quantity = input('How many would you like to remove?: ')
        try:
            quantity = int(quantity)
            if shopping_cart[item] < quantity:
                print("You don't have that many in your cart.")
            else:
                shopping_cart[item] -= quantity
                items[item]['quantity'] += quantity  # Restore the item to inventory
                if shopping_cart[item] == 0:
                    del shopping_cart[item]  # Remove item from cart if quantity is 0
                print(f"Removed {quantity} {item}(s) from your shopping cart.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    else:
        print("That item is not in your shopping cart.")

def get_total_cost():
    total_cost = 0
    for item, quantity in shopping_cart.items():
        total_cost += items[item]['price'] * quantity
    return total_cost

def print_bill():
    print("\n--- Your Bill ---")
    for item_name, quantity in shopping_cart.items():
        price = items[item_name]['price']
        print(f"{item_name}: {quantity} pcs x {price} gil = {quantity * price} gil")
    print(f"Total: {get_total_cost()} gil")
    print("Thank you for shopping!")

def operate_store():
    while True:
        print("\nThe RPG Store!")
        print("-------------------------\n")
        for item_name, details in items.items(): #item_name is key. details is values
            print(f"{item_name}: {details['quantity']} available, {details['price']} gil each")

        action = input("\nWhat would you like to do: (buy / cancel / leave)? ").strip().lower()
        if action == 'buy':
            item = input("What item would you like to buy?: ").strip().lower()
            sell_item(item)
        elif action == 'cancel':
            item = input("What item would you like to remove?: ").strip().lower()
            cancel_item(item)
        elif action == 'leave':
            if shopping_cart:
                print_bill()
            else:
                print("You didn't buy anything. Thank you for visiting!")
            break
        else:
            print("Invalid action. Please choose 'buy', 'cancel', or 'leave'.")

        # Display the shopping cart
        if shopping_cart:
            print("\nShopping Cart:")
            for item_name, quantity in shopping_cart.items():
                print(f"{item_name}: {quantity} pcs")
        else:
            print("\nYour shopping cart is empty.")


if __name__ == "__main__":
    operate_store()


# What does if __name__ == "__main__": do?
# This code block means that operate_store() will only be called if the script is executed directly.
