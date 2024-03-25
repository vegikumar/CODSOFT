from tkinter import *
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = choice.get()
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation"
    result_label.config(text="Result: " + str(result))
root = Tk()
root.geometry("200x200")
root.title("Simple Calculator")
entry1 = Entry(root)
entry1.pack()
entry2 = Entry(root)
entry2.pack()
choice = StringVar(root)
choice.set('+')
operation_menu = OptionMenu(root, choice, '+', '-', '*', '/')
operation_menu.pack()
calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.pack()
result_label = Label(root, text="Result: ")
result_label.pack()
root.mainloop()