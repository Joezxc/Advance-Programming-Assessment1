# Declare an input for the user to enter the preferred first number
option1 = int(input("Input the first number: "))

# Declare an input for the user to enter the preferred  second number
option2 = int(input("Input the second number:: "))

# Conduct addition operation
add_sum = option1 + option2

# Conduct substraction operation
sub_difference = option1 - option2

# Conduct multiplication operation
multiplication_product = option1 * option2

# Test if the second number is not zero before using the division operation
if option2 != 0:
    div_quotient = option1 / option2
    remainder_quotient = option1 % option2
else:
    division_quotient = "Unable to divide by zero"
    remainder_quotient = "Unable to divide by zero"

# Final Outcome
print("Final Outcome:")
print("Addition Operation:", add_sum)
print("Subtraction Operation:", sub_difference)
print("Multiplication Operation:", multiplication_product)
print("Division Operation:", div_quotient)
print("Remainder:", remainder_quotient)