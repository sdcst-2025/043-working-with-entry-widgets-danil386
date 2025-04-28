#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk 


win = tk.Tk()


def clickFunction(event):
    side1 = e1.get()
    side1 = float(side1)
    side2 = e2.get()
    side2 = float(side2)

    hypotenuse= ((side1**2)+(side2**2))**0.5
    a_entry.insert(0,hypotenuse)


l1 = tk.Label(win, text="Enter a value for a side length:")
e1 = tk.Entry(win, width=20)
l2 = tk.Label(win, text="Enter another value for a side length:")
e2 = tk.Entry(win, width=20)
b1 = tk.Button(win, text="Click to find your hypotenuse")

b1.bind("<Button>",clickFunction)

a_label = tk.Label(win, text="Your hypotenuse has a value of:")
a_entry = tk.Entry(win, width=20)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
b1.grid(row=4, column=1, columnspan=2)
a_label.grid(row=5,column=1)
a_entry.grid(row=5,column=2)




win.mainloop()