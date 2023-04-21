'''
Life Cycle of a Tkinter App:
1. import the Tkinter package -> import tkinter
2. create Main Window (entry point)
3. create Widgets (button, text, lable, frame etc.)
4. keep the mainloop alive
'''
import tkinter as tk

# main window
window = tk.Tk()
window.title('Tkinter Basics - Checkbox')
window.geometry('600x400')  # width x height

# Checkbutton Widget
check1_btn = tk.Checkbutton(master=window, text='Correct')
check2_btn = tk.Checkbutton(master=window, text='Incorrect')

# place the check button
check1_btn.grid(row=0, column=0)
check2_btn.grid(row=1, column=0)

# main loop
window.mainloop()
