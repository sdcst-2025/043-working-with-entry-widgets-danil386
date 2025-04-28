"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk 


win = tk.Tk()


def clickFunction(event):
    name = e1.get()
    name = str(name)
    number = e2.get()
    number = str(number)
    grade = e3.get()
    grade = str(grade)

    info = f"{name}, {number}, {grade}"
    a_entry.insert(0,info)


l1 = tk.Label(win, text="Enter your name:")
e1 = tk.Entry(win, width=20)
l2 = tk.Label(win, text="Enter your student number:")
e2 = tk.Entry(win, width=20)
l3 = tk.Label(win, text="Enter your grade:")
e3 = tk.Entry(win, width=20)
b1 = tk.Button(win, text="Click to see your information")

b1.bind("<Button>",clickFunction)

a_label = tk.Label(win, text="You are:")
a_entry = tk.Entry(win, width=20)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
l3.grid(row=3,column=1)
e3.grid(row=3,column=2)
b1.grid(row=4, column=1, columnspan=2)
a_label.grid(row=5,column=1)
a_entry.grid(row=5,column=2)




win.mainloop()