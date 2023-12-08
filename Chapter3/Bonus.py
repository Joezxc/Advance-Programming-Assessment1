# Menu for burger types, toppings, condiments, and sides with their respective prices
menu = {
    'Burgers': {'Beef': 15, 'Chicken': 8, 'Vegetarian': 7},
    'Toppings': {'Cheese': 1.5, 'Peanut Butter': 1, 'Avocado': 2},
    'Condiments': {'Ketchup': 0.5, 'Mayonnaise': 0.5, 'BBQ Sauce': 1},
    'Sides': {'Fries': 3, 'Drink': 2.5}
}


# Function to display the menu
def display_menu():
    print("Welcome to Burger Shack!")
    print("----- Menu -----")
    for category, items in menu.items():
        print(f"{category}:")
        for item, price in items.items():
            print(f"{item} - ${price}")
        print()


# Function to take the order
def take_order():
    burger = input("Choose a burger type (Beef/Chicken/Vegetarian): ").capitalize()
    toppings = input("Choose toppings (Comma separated, e.g. Cheese,Peanut Butter): ").split(',')
    condiments = input("Choose condiments (Comma separated, e.g. Ketchup,Mayonnaise): ").split(',')
    sides = input("Choose sides (Comma separated, e.g. Fries,Drink): ").split(',')

    return burger, toppings, condiments, sides


# Function to calculate the total cost of the order
def calculate_total(burger, toppings, condiments, sides):
    total = menu['Burgers'][burger]

    for topping in toppings:
        total += menu['Toppings'].get(topping, 0)

    for condiment in condiments:
        total += menu['Condiments'].get(condiment, 0)

    for side in sides:
        total += menu['Sides'].get(side, 0)

    return total


# Function to handle payment and return change
def process_payment(total):
    payment = float(input(f"Total amount: ${total}\nEnter payment amount: $"))
    while payment < total:
        payment = float(input("Payment is less than the total amount. Please enter the correct amount: $"))

    change = payment - total
    return change


# Main program
def main():
    display_menu()
    order = take_order()
    total_cost = calculate_total(*order)
    print(f"Total cost of your order is: ${total_cost}")
    change = process_payment(total_cost)
    print(f"Thank you for your order! Your change is: ${change:.2f}")


if __name__ == "__main__":
    main()