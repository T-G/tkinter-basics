import tkinter as tk
from tkinter import Text

# window object
window = tk.Tk()

window.title('Tkinter Basics - Text')

window.geometry('600x400')

# Text Widget (Text Area) - it is used to insert multi-line fields - display and edit
txt = Text(master=window, height=5, width=50)

# place the widget
txt.pack()

# mainloop
window.mainloop()
