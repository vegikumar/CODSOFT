from tkinter import *
import random
root = Tk()
root.title("Password Generator")
root.geometry("500x500")
passstr = StringVar()
passlenlet = IntVar()
passlennum =  IntVar()
passlensym = IntVar()
passlenlet.set(0)
def passwordgen():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    for char in range(passlenlet.get()):
        password_list += random.choice(letters)
    for char in range(passlennum.get()):
        password_list += random.choice(symbols)
    for char in range(passlensym.get()):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    passstr.set(password)
Label(root, text="Password Generator").pack()
Label(root, text="Password letters length").pack(pady=3)
Entry(root, textvariable=passlenlet).pack(pady=3)
Label(root, text="Password numbers length").pack(pady=3)
Entry(root, textvariable=passlennum).pack(pady=3)
Label(root, text="Password symbols length").pack(pady=3)
Entry(root, textvariable=passlensym).pack(pady=3)
Button(root, text="Generate Password", command=passwordgen).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
root.mainloop()