import math

def calculate_area_square():
    side = float(input("Enter the length of a side of the square: "))
    area = side * side
    print(f"The area of the square is: {area}")

def calculate_area_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area}")

def calculate_area_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

def main():
    while True:
        print("\nMenu:")
        print("1: Calculate the area of a square")
        print("2: Calculate the area of a circle")
        print("3: Calculate the area of a triangle")
        print("0: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calculate_area_square()
        elif choice == '2':
            calculate_area_circle()
        elif choice == '3':
            calculate_area_triangle()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()