# Make a variable row is equivalent to 5
rows = 5

for i in range(1, rows + 1): # Use for loop
    for j in range(1, i + 1): # Add the rows and plus 1
        print(j, end=" ")
    print() # print the output