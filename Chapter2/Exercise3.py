from tkinter import *

def submit():
    username = user.get()
    password = passw.get()

    if username == 'admin' and password == '1234':
        status.set('Logged in successfully!')
    else:
        status.set('Username or password is incorrect!')

root = Tk()
#  Create the following labels inside that will ask the user for their log in status
Label(root, text='Username').grid(row=0, column=0)
Label(root, text='Password').grid(row=1, column=0)
Label(root, text='Status').grid(row=2, column=0)

#  Generate a string var for user,passw and status
user = StringVar()
passw = StringVar()
status = StringVar()

#  Adopt the Grid Columns
Entry(root, textvariable=user).grid(row=0, column=1)
Entry(root, textvariable=passw).grid(row=1, column=1)

Button(root, text='Submit', command=submit).grid(row=2, column=1)

Label(root, textvariable=status).grid(row=3, column=1)

root.mainloop()