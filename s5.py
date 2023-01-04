# import the tkinter file
from tkinter import *

# instantiate the Tk class or window
root = Tk()

# Add the title in the window
root.title("Calculator")

# create a operation method
def button_click(number):
    # the delete method are get value on 0 index and there are not accept the other indexing value 
    # inputData.delete(0,END)
    # get the current value in the variable 
    current = inputData.get()
    # delete the value
    inputData.delete(0,END)
    # insert the value using insert and show the proper formate
    inputData.insert(0,str(current) + str(number))
    
# create a clear button
def button_clr():
    inputData.delete(0,END)
    
# create a add button method
def button_add():
    first_number = inputData.get()
    inputData.delete(0,END)
    global f_number 
    global operation
    operation = "add"
    f_number = int(first_number)

# create a sub button method
def button_sub():
    first_number = inputData.get()
    inputData.delete(0,END)
    global f_number 
    global operation
    operation = "sub"
    f_number = int(first_number)

# create a multiply button method
def button_multiply():
    first_number = inputData.get()
    inputData.delete(0,END)
    global f_number 
    global operation
    operation = "multiply"
    f_number = int(first_number)

# create a divide button method
def button_divide():
    first_number = inputData.get()
    inputData.delete(0,END)
    global f_number 
    global operation
    operation = "divide"
    f_number = int(first_number)

# create a equal button method
def button_equal():
    second_number = inputData.get()
    inputData.delete(0,END)
    global s_number
    s_number = int(second_number)
    
    # check the operation
    if operation == "add":
        inputData.insert(0, f_number + s_number)
    if operation == "sub":
        inputData.insert(0, f_number - s_number)
    if operation == "multiply":
        inputData.insert(0, f_number * s_number)
    if operation == "divide":
        inputData.insert(0, f_number / s_number)
    
# create the input filed
inputData = Entry(root, width=35, borderwidth=5)
inputData.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

# create the button in the calculator
#  pass the perameter in the method use the lembda: functionName(perameter)
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# operation button
button_add_ = Button(root, text="+", padx=39, pady=20, command=button_add)
button_sub_ = Button(root, text="-", padx=40, pady=20, command=button_sub)
button_multiply_ = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide_ = Button(root, text="/", padx=40, pady=20, command=button_divide)
button_equal_ = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clr)

# Put the button on screen and create grid
# button 1 to 3
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

# button 4 to 6
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

# button 7 to 9
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

# button 0 or clear 
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

# button add or equal 
button_add_.grid(row=5, column=0)
button_equal_.grid(row=5, column=1, columnspan=2)

# button sub, multiply, divide
button_sub_.grid(row=6, column=0)
button_multiply_.grid(row=6,column=1)
button_divide_.grid(row=6, column=2)

# End the program using mainloop method
root.mainloop()