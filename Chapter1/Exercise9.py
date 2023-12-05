# Create an integer list with consist of 10 integers
integer_list = [23, 56, 12, 87, 5, 42, 9, 33, 71, 19]

# Output the list using a for loop
print("List using a for loop:")
for num in integer_list:
    print(num, end=" ")
print("\n")

# Output the highest and lowest value
max_value = max(integer_list)
min_value = min(integer_list)
print(f"Highest value in the list: {max_value}")
print(f"Lowest value in the list: {min_value}\n")

# Sort the elements in ascending order
integer_list.sort()
print("Sorted elements in ascending order:", integer_list)
print()

# Sort the elements in descending order
integer_list.sort(reverse=True)
print("Sorted elements in descending order:", integer_list)
print()

# Append two elements
integer_list.append(99)
integer_list.append(101)

# Print the list after appending
print("List after appending two elements:", integer_list)