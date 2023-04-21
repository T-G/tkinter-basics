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
from tkinter import Frame, Button


# main window
window = tk.Tk()
window.title('Tkinter Basics - Frame')
window.geometry('600x400')  # width x height

# Frame Widget
frame = Frame(master=window)

# Buttons
btnLeft = Button(master=frame, text='Frame Button Left',
                 bg='black', fg='white')
btnLeft.pack(side=tk.LEFT)

btnRight = Button(master=frame, text='Frame Button Right',
                  bg='black', fg='white')
btnRight.pack(side=tk.RIGHT)

# Place the widget
frame.pack()

# main loop
window.mainloop()
