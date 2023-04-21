'''
Life Cycle of a Tkinter App:
1. import the Tkinter package -> import tkinter
2. create Main Window (entry point)
3. create Widgets (button, text, lable, frame etc.)
4. keep the mainloop alive

# Label -> Read only text on screen
# Entry -> one line text box
'''

import tkinter as tk
from tkinter import Label, Entry


# main window
window = tk.Tk()
window.title('Tkinter Basics - labels and Entry')
window.geometry('600x400')  # width x height

# Label Widget
lblFName = Label(master=window, text='First Name:')
lblLName = Label(master=window, text='Last Name:')

# Entry Widget
entFName = Entry(window)
entLName = Entry(window)


# place the label and Entry
lblFName.grid(row=0, column=0)
entFName.grid(row=0, column=1)

lblLName.grid(row=1, column=0)
entLName.grid(row=1, column=1)


# main loop
window.mainloop()
