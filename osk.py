import tkinter as tk
from tkinter import ttk

key = tk.Tk()

key.title('On Screen Keyboard')


key.geometry('1385x320')  # Window size
key.maxsize(width=1385, height=320)
key.minsize(width=1385, height=320)

style = ttk.Style()
key.configure(bg='gray27')
style.configure('TButton', background='gray21')
style.configure('TButton', foreground='white')

theme = "light"


# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key, state='readonly', textvariable=equation)
Dis_entry.grid(rowspan=1, columnspan=100, ipadx=999, ipady=20)


# showing all data in display
exp = " "
is_shift = False

# Necessary functions


def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def Backspace():
    global exp
    exp = exp[:-1]
    equation.set(exp)


def Shift():
    global is_shift
    is_shift = not is_shift
    display()


def Clear():
    global exp
    exp = " "
    equation.set(exp)

def Theme():
    global theme
    if theme == "dark":
        key.configure(bg='gray27')
        style.configure('TButton', background='gray21')
        style.configure('TButton', foreground='white')
        theme = "light"
    elif theme == "light":
        key.configure(bg='gray99')
        style.configure('TButton', background='azure')
        style.configure('TButton', foreground='black')
        theme = "dark"


def display():
    if (is_shift):
        # Adding keys line wise
        # First Line Button
        tilda = ttk.Button(key, text='~', width=6, command=lambda: press('~'))
        tilda.grid(row=1, column=0, ipadx=6, ipady=10)

        num1 = ttk.Button(key, text='!', width=6, command=lambda: press('!'))
        num1.grid(row=1, column=1, ipadx=6, ipady=10)

        num2 = ttk.Button(key, text='@', width=6, command=lambda: press('@'))
        num2.grid(row=1, column=2, ipadx=6, ipady=10)

        num3 = ttk.Button(key, text='#', width=6, command=lambda: press('#'))
        num3.grid(row=1, column=3, ipadx=6, ipady=10)

        num4 = ttk.Button(key, text='$', width=6, command=lambda: press('$'))
        num4.grid(row=1, column=4, ipadx=6, ipady=10)

        num5 = ttk.Button(key, text='%', width=6, command=lambda: press('%'))
        num5.grid(row=1, column=5, ipadx=6, ipady=10)

        num6 = ttk.Button(key, text='^', width=6, command=lambda: press('^'))
        num6.grid(row=1, column=6, ipadx=6, ipady=10)

        num7 = ttk.Button(key, text='&', width=6, command=lambda: press('&'))
        num7.grid(row=1, column=7, ipadx=6, ipady=10)

        num8 = ttk.Button(key, text='*', width=6, command=lambda: press('*'))
        num8.grid(row=1, column=8, ipadx=6, ipady=10)

        num9 = ttk.Button(key, text='(', width=6, command=lambda: press('('))
        num9.grid(row=1, column=9, ipadx=6, ipady=10)

        num0 = ttk.Button(key, text=')', width=6, command=lambda: press(')'))
        num0.grid(row=1, column=10, ipadx=6, ipady=10)

        under = ttk.Button(key, text='_', width=6, command=lambda: press('_'))
        under.grid(row=1, column=11, ipadx=6, ipady=10)

        plus = ttk.Button(key, text='+', width=6, command=lambda: press('+'))
        plus.grid(row=1, column=12, ipadx=6, ipady=10)

        backspace = ttk.Button(
            key, text='<---', width=6, command=Backspace)
        backspace.grid(row=1, column=13, ipadx=6, ipady=10)

        # Second Line Buttons

        tab_button = ttk.Button(key, text='Tab', width=6,
                                command=lambda: press('\t'))
        tab_button.grid(row=2, column=0, columnspan=2, ipadx=55, ipady=10)

        Q = ttk.Button(key, text='Q', width=6, command=lambda: press('Q'))
        Q.grid(row=2, column=2, ipadx=6, ipady=10)

        W = ttk.Button(key, text='W', width=6, command=lambda: press('W'))
        W.grid(row=2, column=3, ipadx=6, ipady=10)
