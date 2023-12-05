
#Declare a variable that will ask the users to enter the first, second, and third number
x = int(input('Please enter the first number: '))
y = int(input('Please enter the second number: '))
z = int(input('Please enter the third number: '))


#Apply if elif else statement to acquire the largest number
if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

#Print the final output
print("the largest number is ", largest)