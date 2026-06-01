import tkinter as tk
from tkinter import font

root = tk.Tk()
root.withdraw()

available_font = font.families()

for x in list(available_font):
    print(x);


#pi_font = tkinter.font.Font(
#    family="times"
#    size=16
#    weight="Bold"
#    slant="italic"
#)

#print(tkinter.font.families())
root.destroy()


