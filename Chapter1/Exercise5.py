# Declare a variable to count the number of loops
count = 0

# Begin with a while loop
while True:
    # Declare a variable that will ask the user to continue
    x = input("Do you want to Continue? (Y/N): ")

    # Expand the count of loops
    if x.upper() == "Y":
        count += 1

    # End the count if the user's input is N, then it will break the loop
    else:
        break

# Print the final output
print("The while loop was performed", count, "times.")