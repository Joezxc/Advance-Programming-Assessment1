# Use a for loop with a range
for i in range(1, 101):
    # Use an if loop and print FizzBuzz
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Use an elif loop and print Fizz and Buzz
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    # End with a else loop
    else:
        print(i)
        # Print the string