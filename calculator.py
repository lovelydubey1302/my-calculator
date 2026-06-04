from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

entry = Entry(root, textvariable=equation, font=("Arial", 20))
entry.pack(fill="both", ipadx=8, ipady=15)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == '=':
            Button(frame, text=btn, font=("Arial", 18),
                   command=equal).pack(side="left", expand=True, fill="both")
        else:
            Button(frame, text=btn, font=("Arial", 18),
                   command=lambda b=btn: press(b)).pack(side="left", expand=True, fill="both")

Button(root, text="Clear", font=("Arial", 18),
       command=clear).pack(fill="both")

root.mainloop()