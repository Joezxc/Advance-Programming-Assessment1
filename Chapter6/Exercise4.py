import json

def collect_student_data():
    # Collect the student's name, ID, and course
    name = input("Enter the student's name: ")
    id = input("Enter the student's ID: ")
    course = input("Enter the student's course: ")

    # Store the input in a dictionary
    student_data = {
        'Name': name,
        'ID': id,
        'Course': course,
        'CourseDetails': {}
    }

    return student_data

def add_course_details(student_data):
    # Collect the group and year
    group = input("Enter the student's group: ")
    year = input("Enter the student's year: ")

    # Store the input in the 'CourseDetails' section of the dictionary
    student_data['CourseDetails'] = {
        'Group': group,
        'Year': year
    }

    return student_data

def write_student_data_to_file(file_name, data):
    # Write the dictionary to the specified file in JSON format
    with open(file_name, 'w') as file:
        json.dump(data, file)

def read_student_data_from_file(file_name):
    # Read the contents of the file
    with open(file_name, 'r') as file:
        data = json.load(file)

    return data

def display_student_data(student_data):
    # Access the keys in the dictionary and display the student's details
    print("Name:", student_data['Name'])
    print("ID:", student_data['ID'])
    print("Course:", student_data['Course'])
    print("Group:", student_data['CourseDetails']['Group'])
    print("Year:", student_data['CourseDetails']['Year'])

def main():
    student_data = collect_student_data()
    student_data = add_course_details(student_data)
    write_student_data_to_file("student_data.json", student_data)
    student_data = read_student_data_from_file("student_data.json")
    display_student_data(student_data)

if __name__ == "__main__":
    main()