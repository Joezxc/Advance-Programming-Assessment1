def calculate_product_of_list(lst):
    product = 1
    for item in lst:
        product *= item
    return product

# Example list
my_list = [2, 4, 6, 8, 10]

# Calculate the product of the list items by calling the function
result = calculate_product_of_list(my_list)

# Display the result
print(f"The product of the items in the list is: {result}")