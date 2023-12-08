import tkinter as tk

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def get_data(self):
        return f"Name: {self.name}\nAge: {self.age}\nBreed: {self.breed}"

    @classmethod
    def oldest_dog_woof(cls, dog1, dog2):
        if dog1.age > dog2.age:
            oldest_dog = dog1
        else:
            oldest_dog = dog2
        return f"{oldest_dog.name} (the oldest dog) says: Woof!"

def display_dog_data():
    dog1 = Dog(entry_name1.get(), int(entry_age1.get()), entry_breed1.get())
    dog2 = Dog(entry_name2.get(), int(entry_age2.get()), entry_breed2.get())

    data1 = dog1.get_data()
    data2 = dog2.get_data()

    label_dog1.config(text=f"Dog 1:\n{data1}")
    label_dog2.config(text=f"Dog 2:\n{data2}")

    woof_text = Dog.oldest_dog_woof(dog1, dog2)
    label_oldest_dog.config(text=woof_text)

root = tk.Tk()
root.title("Dog Characteristics")

label_name1 = tk.Label(root, text="Dog 1 Name:")
label_name1.grid(row=0, column=0)
entry_name1 = tk.Entry(root)
entry_name1.grid(row=0, column=1)

label_age1 = tk.Label(root, text="Dog 1 Age:")
label_age1.grid(row=1, column=0)
entry_age1 = tk.Entry(root)
entry_age1.grid(row=1, column=1)

label_breed1 = tk.Label(root, text="Dog 1 Breed:")
label_breed1.grid(row=2, column=0)
entry_breed1 = tk.Entry(root)
entry_breed1.grid(row=2, column=1)

label_name2 = tk.Label(root, text="Dog 2 Name:")
label_name2.grid(row=3, column=0)
entry_name2 = tk.Entry(root)
entry_name2.grid(row=3, column=1)

label_age2 = tk.Label(root, text="Dog 2 Age:")
label_age2.grid(row=4, column=0)
entry_age2 = tk.Entry(root)
entry_age2.grid(row=4, column=1)

label_breed2 = tk.Label(root, text="Dog 2 Breed:")
label_breed2.grid(row=5, column=0)
entry_breed2 = tk.Entry(root)
entry_breed2.grid(row=5, column=1)

button_display = tk.Button(root, text="Display Dog Data", command=display_dog_data)
button_display.grid(row=6, columnspan=2)

label_dog1 = tk.Label(root, text="")
label_dog1.grid(row=7, column=0)

label_dog2 = tk.Label(root, text="")
label_dog2.grid(row=7, column=1)

label_oldest_dog = tk.Label(root, text="")
label_oldest_dog.grid(row=8, columnspan=2)

root.mainloop()