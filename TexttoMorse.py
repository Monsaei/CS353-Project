import tkinter as tk
import MorseTranslator as mt
import time

def inputmorsedisp():
    input = input_morse.get()
    prompt = tk.Label(mframe, text = "Your input: "+input+" translates to: ", font=('Helvetica', 10), bg="#9370DB", fg="white")
    prompt.pack(padx=5, pady=5)
    encoded = ''
    user_string = input.upper()
    for character in user_string:
        tmp = []
        mt.char_to_morse(mt.morse_fsm, character, tmp)
        encoded_tmp = "".join(tmp)
        encoded = encoded + encoded_tmp + " "
    result = tk.Label(mframe, text = encoded, font=('Helvetica', 16), bg="#9370DB", fg="white")
    result.pack(padx=5, pady=5)
    mt.morse_beep(encoded)
    extbtn = tk.Button(mframe, text="Exit", font=('Helvetica', 16), padx=5, pady = 10, fg="white", bg="#9370DB", command = chartomorse.quit)
    extbtn.pack()


chartomorse = tk.Tk()
chartomorse.grab_set()
chartomorse.configure(background="#4B0082")
chartomorse.geometry("800x500")
chartomorse.title("English Word/s to Morse Code")

mframe = tk.Frame(chartomorse, bg = "#9370DB")
mframe.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

blankspace = tk.Label(mframe, bg="#9370DB")
blankspace.pack()

title = tk.Label(mframe, text = "Please Enter the English Word/s you want to \n translate to Morse Code:", font=('Helvetica', 16), bg="#9370DB", fg="white")
title.pack(padx=5, pady=5)

input_str = tk.StringVar(chartomorse)
input_morse = tk.Entry(mframe, textvariable=input_str , width = 50)
input_morse.pack()

title = tk.Label(mframe, text = "Note: Arabic numbers 0-9 can be added and symbols =, +, and /", font=('Helvetica', 10), bg="#9370DB", fg="white")
title.pack(padx=5, pady=5)

blankspace = tk.Label(mframe, bg="#9370DB")
blankspace.pack()



pltbtn= tk.Button(mframe, text = "Enter English Word/s", font=('Helvetica', 16), bg="#9370DB", fg="white", command =inputmorsedisp, state ='disabled')
pltbtn.pack()

def pltbtn_upd(*args):
    if(len(input_str.get())>0):
        pltbtn.config(state = 'normal')
    else:
        pltbtn.config(state = 'disabled')
input_str.trace('w', pltbtn_upd)

chartomorse.mainloop()