#Declare a variable that will ask the user to input the sides of the triangle
linesegment1 = int(input("Input the first side of the triangle: "))
linesegment2 = int(input("Input the second side of the triangle: "))
linesegment3 = int(input("Input the third side of the triangle: "))

#Declare an if statement if the sides can form a valid triangle.
if linesegment1 + linesegment2 > linesegment3 and linesegment2 + linesegment3 > linesegment1 and linesegment1 + linesegment3 > linesegment2:
    print("These side lengths can form a valid triangle.")

#Declare an else statement if the sides can form a valid triangle.
else:
    print("These side lengths cannot form a valid triangle.")