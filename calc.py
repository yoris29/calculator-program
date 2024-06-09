from tkinter import *

def button_click(button_name, operand):
   prev_txt = label.cget("text")
   new_txt = button_name.cget('text')
   label.config(text=str(prev_txt)+str(new_txt))
def calculate():
   result = eval(label.cget('text'))
   label.config(text=str(result))

def clear_click():
   label.config(text="")

window = Tk()

label = Label(
   window,
   bg="white",
   width=30,
   height=5,
)
label.grid(row=0, column=0, columnspan=4)

# Row 1
button_1 = Button(
   window,
   text="1",
   command=lambda: button_click(button_1, ""),
   height=5,
   width=10
)
button_1.grid(row=1, column=0)

button_2 = Button(
   window,
   text="2",
   command=lambda: button_click(button_2, ""),
   height=5,
   width=10,
)
button_2.grid(row=1, column=1)

button_3 = Button(
   window,
   text="3",
   command=lambda: button_click(button_3, ""),
   height=5,
   width=10,
)
button_3.grid(row=1, column=3)

button_plus = Button(
   window,
   text="+",
   command=lambda: button_click(button_plus, "+"),
   height=5,
   width=10,
)
button_plus.grid(row=1, column=4)

# Row 2
button_4 = Button(
   window,
   text="4",
   command=lambda: button_click(button_4, ""),
   height=5,
   width=10
)
button_4.grid(row=2, column=0)

button_5 = Button(
   window,
   text="5",
   command=lambda: button_click(button_5, ""),
   height=5,
   width=10,
)
button_5.grid(row=2, column=1)

button_6 = Button(
   window,
   text="6",
   command=lambda: button_click(button_6, ""),
   height=5,
   width=10,
)
button_6.grid(row=2, column=3)

button_minus = Button(
   window,
   text="-",
   command=lambda: button_click(button_minus, "-"),
   height=5,
   width=10,
)
button_minus.grid(row=2, column=4)

# Row 3
button_7 = Button(
   window,
   text="7",
   command=lambda: button_click(button_7, ""),
   height=5,
   width=10
)
button_7.grid(row=3, column=0)

button_8 = Button(
   window,
   text="8",
   command=lambda: button_click(button_8, ""),
   height=5,
   width=10,
)
button_8.grid(row=3, column=1)

button_9 = Button(
   window,
   text="9",
   command=lambda: button_click(button_9, ""),
   height=5,
   width=10,
)
button_9.grid(row=3, column=3)

button_multiplication = Button(
   window,
   text="*",
   command=lambda: button_click(button_multiplication, "*"),
   height=5,
   width=10,
)
button_multiplication.grid(row=3, column=4)

# Row 4
button_0 = Button(
   window,
   text="0",
   command=lambda: button_click(button_0, ""),
   height=5,
   width=10
)
button_0.grid(row=4, column=0)

button_dot = Button(
   window,
   text=".",
   command=lambda: button_click(button_dot, "."),
   height=5,
   width=10,
)
button_dot.grid(row=4, column=1)

button_equal = Button(
   window,
   text="=",
   command= calculate,
   height=5,
   width=10,
)
button_equal.grid(row=4, column=3)

button_div = Button(
   window,
   text="/",
   command=lambda: button_click(button_div, "/"),
   height=5,
   width=10,
)
button_div.grid(row=4, column=4)

# Row 5 
button_clear = Button(
   window,
   text="clear",
   command= clear_click,
   height=5,
   width=20,
)
button_clear.grid(row=5, column=1, columnspan=3)

window.mainloop()