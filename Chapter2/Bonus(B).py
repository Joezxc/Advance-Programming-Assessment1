from datetime import datetime

input_date = input("Enter your date of birth in the format mm/dd/yyyy: ")
dob = datetime.strptime(input_date, "%m/%d/%Y")

age = (datetime.now() - dob).days // 365

print("Your age is {} years".format(age))