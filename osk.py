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
    #1

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

        #2

        E = ttk.Button(key, text='E', width=6, command=lambda: press('E'))
        E.grid(row=2, column=4, ipadx=6, ipady=10)

        R = ttk.Button(key, text='R', width=6, command=lambda: press('R'))
        R.grid(row=2, column=5, ipadx=6, ipady=10)

        T = ttk.Button(key, text='T', width=6, command=lambda: press('T'))
        T.grid(row=2, column=6, ipadx=6, ipady=10)

        Y = ttk.Button(key, text='Y', width=6, command=lambda: press('Y'))
        Y.grid(row=2, column=7, ipadx=6, ipady=10)

        U = ttk.Button(key, text='U', width=6, command=lambda: press('U'))
        U.grid(row=2, column=8, ipadx=6, ipady=10)

        I = ttk.Button(key, text='I', width=6, command=lambda: press('I'))
        I.grid(row=2, column=9, ipadx=6, ipady=10)

        O = ttk.Button(key, text='O', width=6, command=lambda: press('O'))
        O.grid(row=2, column=10, ipadx=6, ipady=10)

        P = ttk.Button(key, text='P', width=6, command=lambda: press('P'))
        P.grid(row=2, column=11, ipadx=6, ipady=10)

        curly_l = ttk.Button(
            key, text='{', width=6, command=lambda: press('{'))
        curly_l.grid(row=2, column=12, ipadx=6, ipady=10)

        curly_r = ttk.Button(key, text='}', width=6,
                             command=lambda: press('}'))
        curly_r.grid(row=2, column=13, ipadx=6, ipady=10)

        # Third Line Buttons

        A = ttk.Button(key, text='A', width=6, command=lambda: press('A'))
        A.grid(row=3, column=0, ipadx=6, ipady=10)

        S = ttk.Button(key, text='S', width=6, command=lambda: press('S'))
        S.grid(row=3, column=1, ipadx=6, ipady=10)

        D = ttk.Button(key, text='D', width=6, command=lambda: press('D'))
        D.grid(row=3, column=2, ipadx=6, ipady=10)

        F = ttk.Button(key, text='F', width=6, command=lambda: press('F'))
        F.grid(row=3, column=3, ipadx=6, ipady=10)

        G = ttk.Button(key, text='G', width=6, command=lambda: press('G'))
        G.grid(row=3, column=4, ipadx=6, ipady=10)

        H = ttk.Button(key, text='H', width=6, command=lambda: press('H'))
        H.grid(row=3, column=5, ipadx=6, ipady=10)

        J = ttk.Button(key, text='J', width=6, command=lambda: press('J'))
        J.grid(row=3, column=6, ipadx=6, ipady=10)

        K = ttk.Button(key, text='K', width=6, command=lambda: press('K'))
        K.grid(row=3, column=7, ipadx=6, ipady=10)

        L = ttk.Button(key, text='L', width=6, command=lambda: press('L'))
        L.grid(row=3, column=8, ipadx=6, ipady=10)

        colon = ttk.Button(key, text=':', width=6,
                           command=lambda: press(':'))
        colon.grid(row=3, column=9, ipadx=6, ipady=10)

        quotation = ttk.Button(key, text='"', width=6,
                               command=lambda: press('"'))
        quotation.grid(row=3, column=10, ipadx=6, ipady=10)

        pipe = ttk.Button(key, text='|', width=6, command=lambda: press('|'))
        pipe.grid(row=3, column=11, ipadx=6, ipady=10)

        enter = ttk.Button(key, text='Enter', width=6,
                           command=lambda: press('\n'))
        enter.grid(row=3, column=12, columnspan=2, ipadx=55, ipady=10)

        # Fourth line Buttons

        shift = ttk.Button(key, text='Shift', width=6, command=Shift)
        shift.grid(row=4, column=0, columnspan=2, ipadx=55, ipady=10)

        Z = ttk.Button(key, text='Z', width=6, command=lambda: press('Z'))
        Z.grid(row=4, column=2, ipadx=6, ipady=10)

        X = ttk.Button(key, text='X', width=6, command=lambda: press('X'))
        X.grid(row=4, column=3, ipadx=6, ipady=10)

        C = ttk.Button(key, text='C', width=6, command=lambda: press('C'))
        C.grid(row=4, column=4, ipadx=6, ipady=10)

        V = ttk.Button(key, text='V', width=6, command=lambda: press('V'))
        V.grid(row=4, column=5, ipadx=6, ipady=10)

        B = ttk.Button(key, text='B', width=6, command=lambda: press('B'))
        B.grid(row=4, column=6, ipadx=6, ipady=10)

        N = ttk.Button(key, text='N', width=6, command=lambda: press('N'))
        N.grid(row=4, column=7, ipadx=6, ipady=10)

        M = ttk.Button(key, text='M', width=6, command=lambda: press('M'))
        M.grid(row=4, column=8, ipadx=6, ipady=10)

        ang_l = ttk.Button(key, text='<', width=6, command=lambda: press('<'))
        ang_l.grid(row=4, column=9, ipadx=6, ipady=10)

        ang_r = ttk.Button(key, text='>', width=6, command=lambda: press('>'))
        ang_r.grid(row=4, column=10, ipadx=6, ipady=10)

        question = ttk.Button(key, text='?', width=6,
                              command=lambda: press('?'))
        question.grid(row=4, column=11, ipadx=6, ipady=10)

        clear = ttk.Button(key, text='Clear', width=6, command=Clear)
        clear.grid(row=4, column=12, columnspan=2, ipadx=55, ipady=10)

        # Fifth Line Buttons

        space = ttk.Button(key, text='Space', width=6,
                           command=lambda: press(' '))
        space.grid(row=5, column=2, columnspan=8, ipadx=350, ipady=10)

        theme = ttk.Button(key, text='Theme', width=6, command=Theme)
        theme.grid(row=5, column=12, columnspan=2, ipadx=55, ipady=10)

        key.mainloop()
    else:
        # Adding keys line wise
        # First Line Button
        tick = ttk.Button(key, text='`', width=6, command=lambda: press('`'))
        tick.grid(row=1, column=0, ipadx=6, ipady=10)

        num1 = ttk.Button(key, text='1', width=6, command=lambda: press('1'))
        num1.grid(row=1, column=1, ipadx=6, ipady=10)

        num2 = ttk.Button(key, text='2', width=6, command=lambda: press('2'))
        num2.grid(row=1, column=2, ipadx=6, ipady=10)

        num3 = ttk.Button(key, text='3', width=6, command=lambda: press('3'))
        num3.grid(row=1, column=3, ipadx=6, ipady=10)

        num4 = ttk.Button(key, text='4', width=6, command=lambda: press('4'))
        num4.grid(row=1, column=4, ipadx=6, ipady=10)

        num5 = ttk.Button(key, text='5', width=6, command=lambda: press('5'))
        num5.grid(row=1, column=5, ipadx=6, ipady=10)

        num6 = ttk.Button(key, text='6', width=6, command=lambda: press('6'))
        num6.grid(row=1, column=6, ipadx=6, ipady=10)

        num7 = ttk.Button(key, text='7', width=6, command=lambda: press('7'))
        num7.grid(row=1, column=7, ipadx=6, ipady=10)

        num8 = ttk.Button(key, text='8', width=6, command=lambda: press('8'))
        num8.grid(row=1, column=8, ipadx=6, ipady=10)

        num9 = ttk.Button(key, text='9', width=6, command=lambda: press('9'))
        num9.grid(row=1, column=9, ipadx=6, ipady=10)

        num0 = ttk.Button(key, text='0', width=6, command=lambda: press('0'))
        num0.grid(row=1, column=10, ipadx=6, ipady=10)

        minus = ttk.Button(key, text='-', width=6, command=lambda: press('-'))
        minus.grid(row=1, column=11, ipadx=6, ipady=10)

        equal = ttk.Button(key, text='=', width=6, command=lambda: press('='))
        equal.grid(row=1, column=12, ipadx=6, ipady=10)

        backspace = ttk.Button(
            key, text='<---', width=6, command=Backspace)
        backspace.grid(row=1, column=13, ipadx=6, ipady=10)

        # Second Line Buttons

        tab_button = ttk.Button(key, text='Tab', width=6,
                                command=lambda: press('\t'))
        tab_button.grid(row=2, column=0, columnspan=2, ipadx=55, ipady=10)

        Q = ttk.Button(key, text='q', width=6, command=lambda: press('q'))
        Q.grid(row=2, column=2, ipadx=6, ipady=10)

        W = ttk.Button(key, text='w', width=6, command=lambda: press('w'))
        W.grid(row=2, column=3, ipadx=6, ipady=10)

        E = ttk.Button(key, text='e', width=6, command=lambda: press('e'))
        E.grid(row=2, column=4, ipadx=6, ipady=10)

        R = ttk.Button(key, text='r', width=6, command=lambda: press('r'))
        R.grid(row=2, column=5, ipadx=6, ipady=10)

        T = ttk.Button(key, text='t', width=6, command=lambda: press('t'))
        T.grid(row=2, column=6, ipadx=6, ipady=10)

        Y = ttk.Button(key, text='y', width=6, command=lambda: press('y'))
        Y.grid(row=2, column=7, ipadx=6, ipady=10)

        U = ttk.Button(key, text='u', width=6, command=lambda: press('u'))
        U.grid(row=2, column=8, ipadx=6, ipady=10)

        I = ttk.Button(key, text='i', width=6, command=lambda: press('i'))
        I.grid(row=2, column=9, ipadx=6, ipady=10)

        O = ttk.Button(key, text='o', width=6, command=lambda: press('o'))
        O.grid(row=2, column=10, ipadx=6, ipady=10)

        P = ttk.Button(key, text='p', width=6, command=lambda: press('p'))
        P.grid(row=2, column=11, ipadx=6, ipady=10)

        sq_l = ttk.Button(key, text='[', width=6, command=lambda: press('['))
        sq_l.grid(row=2, column=12, ipadx=6, ipady=10)

        sq_r = ttk.Button(key, text=']', width=6, command=lambda: press(']'))
        sq_r.grid(row=2, column=13, ipadx=6, ipady=10)

        # Third Line Buttons

        A = ttk.Button(key, text='a', width=6, command=lambda: press('a'))
        A.grid(row=3, column=0, ipadx=6, ipady=10)

        S = ttk.Button(key, text='s', width=6, command=lambda: press('s'))
        S.grid(row=3, column=1, ipadx=6, ipady=10)

        D = ttk.Button(key, text='d', width=6, command=lambda: press('d'))
        D.grid(row=3, column=2, ipadx=6, ipady=10)

        F = ttk.Button(key, text='f', width=6, command=lambda: press('f'))
        F.grid(row=3, column=3, ipadx=6, ipady=10)

        G = ttk.Button(key, text='g', width=6, command=lambda: press('g'))
        G.grid(row=3, column=4, ipadx=6, ipady=10)

        H = ttk.Button(key, text='h', width=6, command=lambda: press('h'))
        H.grid(row=3, column=5, ipadx=6, ipady=10)

        J = ttk.Button(key, text='j', width=6, command=lambda: press('j'))
        J.grid(row=3, column=6, ipadx=6, ipady=10)

        K = ttk.Button(key, text='k', width=6, command=lambda: press('k'))
        K.grid(row=3, column=7, ipadx=6, ipady=10)

        L = ttk.Button(key, text='l', width=6, command=lambda: press('l'))
        L.grid(row=3, column=8, ipadx=6, ipady=10)
        
        #3

        semi_co = ttk.Button(key, text=';', width=6,
                             command=lambda: press(';'))
        semi_co.grid(row=3, column=9, ipadx=6, ipady=10)

        quotation = ttk.Button(key, text="'", width=6,
                               command=lambda: press('"'))
        quotation.grid(row=3, column=10, ipadx=6, ipady=10)

        back_slash = ttk.Button(key, text='\\', width=6,
                                command=lambda: press('\\'))
        back_slash.grid(row=3, column=11, ipadx=6, ipady=10)

        enter = ttk.Button(key, text='Enter', width=6,
                           command=lambda: press('\n'))
        enter.grid(row=3, column=12, columnspan=2, ipadx=55, ipady=10)

        # Fourth line Buttons

        shift = ttk.Button(key, text='Shift', width=6, command=Shift)
        shift.grid(row=4, column=0, columnspan=2, ipadx=55, ipady=10)

        Z = ttk.Button(key, text='z', width=6, command=lambda: press('z'))
        Z.grid(row=4, column=2, ipadx=6, ipady=10)

        X = ttk.Button(key, text='x', width=6, command=lambda: press('x'))
        X.grid(row=4, column=3, ipadx=6, ipady=10)

        C = ttk.Button(key, text='c', width=6, command=lambda: press('c'))
        C.grid(row=4, column=4, ipadx=6, ipady=10)

        V = ttk.Button(key, text='v', width=6, command=lambda: press('v'))
        V.grid(row=4, column=5, ipadx=6, ipady=10)

        B = ttk.Button(key, text='b', width=6, command=lambda: press('b'))
        B.grid(row=4, column=6, ipadx=6, ipady=10)

        N = ttk.Button(key, text='n', width=6, command=lambda: press('n'))
        N.grid(row=4, column=7, ipadx=6, ipady=10)

        M = ttk.Button(key, text='m', width=6, command=lambda: press('m'))
        M.grid(row=4, column=8, ipadx=6, ipady=10)

        comma = ttk.Button(key, text=',', width=6, command=lambda: press(','))
        comma.grid(row=4, column=9, ipadx=6, ipady=10)

        dot = ttk.Button(key, text='.', width=6, command=lambda: press('.'))
        dot.grid(row=4, column=10, ipadx=6, ipady=10)

        slash = ttk.Button(key, text='/', width=6, command=lambda: press('/'))
        slash.grid(row=4, column=11, ipadx=6, ipady=10)

        clear = ttk.Button(key, text='Clear', width=6, command=Clear)
        clear.grid(row=4, column=12, columnspan=2, ipadx=55, ipady=10)

        # Fifth Line Buttons

        space = ttk.Button(key, text='Space', width=6,
                           command=lambda: press(' '))
        space.grid(row=5, column=2, columnspan=8, ipadx=350, ipady=10)

        theme = ttk.Button(key, text='Theme', width=6, command=Theme)
        theme.grid(row=5, column=12, columnspan=2, ipadx=55, ipady=10)

        key.mainloop()


display()
