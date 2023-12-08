import operator

# Function to calculate the result using the given operator and numbers
def calculate(op, num1, num2):
    return op(num1, num2)

# Function to display the menu
def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Q. Quit")

# Function to check if the first number is greater than the second number
def check_greater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Function to return the appropriate operator function based on the user's choice
def get_operator(choice):
    switcher = {
        1: operator.add,
        2: operator.sub,
        3: operator.mul,
        4: operator.truediv,
        5: operator.mod,
        6: check_greater
    }
    return switcher.get(choice, None)

# Function to implement the calculator
def main():
    while True:
        menu()
        choice = input("Enter your operation choice (1-6) or Q to quit: ")
        if choice.upper() == 'Q':
            break
        elif choice.isdigit() and 1 <= int(choice) <= 6:
            choice = int(choice)
            op = get_operator(choice)
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if op:
                result = calculate(op, num1, num2)
                print(f"The result is: {result}")
            else:
                print("Invalid choice")
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()