import tkinter as tk
import MorseTranslator as mt


def inputmorsedisp():
    input = input_morse.get()
    prompt = tk.Label(mframe, text = "Your input: "+input+" translates to: ", font=('Helvetica', 10), bg="#9370DB", fg="white")
    prompt.pack(padx=5, pady=5)
    result = tk.Label(mframe, text = mt.decode_morse(mt.morse_fsm, input), font=('Helvetica', 16), bg="#9370DB", fg="white")
    result.pack(padx=5, pady=5)
    extbtn = tk.Button(mframe, text="Exit", font=('Helvetica', 16), padx=5, pady = 10, fg="white", bg="#9370DB", command = morsetochar.quit)
    extbtn.pack()

morsetochar = tk.Tk()
morsetochar.grab_set()
morsetochar.configure(background="#4B0082")
morsetochar.geometry("800x500")
morsetochar.title("Morse Code to English Word/s")

mframe = tk.Frame(morsetochar, bg = "#9370DB")
mframe.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

blankspace = tk.Label(mframe, bg="#9370DB")
blankspace.pack()

title = tk.Label(mframe, text = "Please Enter the Morse Code you want to translate to Plaintext:", font=('Helvetica', 16), bg="#9370DB", fg="white")
title.pack(padx=5, pady=5)

input_str = tk.StringVar(morsetochar)
input_morse = tk.Entry(mframe, textvariable=input_str , width = 50)
input_morse.pack()
    
title = tk.Label(mframe, text = "Note: Each character of morse code is separated by space, use '/' to separate words", font=('Helvetica', 10), bg="#9370DB", fg="white")
title.pack(padx=5, pady=5)

morsebtn = tk.Button(mframe, text = "Enter Morse Code", font=('Helvetica', 16), bg="#9370DB", fg="white", command =inputmorsedisp, state ='disabled')
morsebtn.pack()

def morsebtn_upd(*args):
    if(len(input_str.get())>0):
        morsebtn.config(state = 'normal')
    else:
        morsebtn.config(state = 'disabled')
input_str.trace('w', morsebtn_upd)

morsetochar.mainloop()