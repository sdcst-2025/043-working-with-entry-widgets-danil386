"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk 


win = tk.Tk()


def clickFunction(event):
    b = e1.get()
    b = float(b)
    c = e2.get()
    c = float(c)

    try:
        ff1 = (-b+(((b**2)-(4*c))**0.5))/2 
        ff1 = ff1.real
        ff1 = round(ff1,4)
        a_entry.insert(0,ff1)
    except:
        ff1 = "not possible"
        a_entry.insert(0,ff1)


    try:
        ff2 = (-b-(((b**2)-(4*c))**0.5))/2
        ff2 = ff2.real
        ff2 = round(ff2,4)
        b_entry.insert(0,ff2)
    except:
        ff2 = "not possible"
        b_entry.insert(0,ff2)



l0 = tk.Label(win, text="The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c are coefficients.")
l1 = tk.Label(win, text="Enter a value for b:")
e1 = tk.Entry(win, width=20)
l2 = tk.Label(win, text="Enter a value for c:")
e2 = tk.Entry(win, width=20)
b1 = tk.Button(win, text="Click to factor")

b1.bind("<Button>",clickFunction)

a_label = tk.Label(win, text="Your factored forms:")
a_entry = tk.Entry(win, width=20)
b_entry = tk.Entry(win, width=20)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
b1.grid(row=4, column=1, columnspan=2)
a_label.grid(row=5,column=1)
a_entry.grid(row=5,column=2)
b_entry.grid(row=6,column =2)


win.mainloop()