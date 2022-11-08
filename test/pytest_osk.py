import tkinter as tk
from tkinter import ttk
import osk

# Necessary functions

def test_press():
    assert osk.press('9') == True
    print("Ho premuto 9")

def test_Backspace():
    assert osk.Backspace() == True
    print("Ho cancellato il carattere")
    
def test_shift():
    assert osk.Shift() == True
    print("Ho premuto shift")

def test_clear():
    assert osk.Clear() == True
    print("Ho cancellato tutto")

def test_theme():
    assert osk.Theme() == True
    print("Ho cambiato tema")

def test_display():
    assert osk.display() == True
    print("Ho acceso lo schermo")

test_press()
test_Backspace()
test_clear()
test_theme()
test_shift()
test_display()