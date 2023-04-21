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
window.title('Tkinter basics - Button')
window.geometry('600x400')  # width x height

# Button Widget
btn = tk.Button(master=window,
                text='Close',
                width=45,  # text-unit -> width of one char of text
                height=10,  # text-unit -> height of one char of text
                bg='red',  # background color
                fg='white',  # fore color
                command=window.destroy  # what to do when clicked
                )

# place the button
btn.pack()


# main loop
window.mainloop()
