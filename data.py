from tkinter import *
from tkinter import simpledialog
import interface

window = Tk()
window.withdraw()

user_name = simpledialog.askstring("Input",'Your Name: ')
name = simpledialog.askstring("Input",'Persons name: ')
language = simpledialog.askstring("Input",'Language you want to use: ')
region = simpledialog.askstring("Input",'Where the person from: ')
relation = simpledialog.askstring("Input",'Relation with you: ')
