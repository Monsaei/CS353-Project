import tkinter as tk
import MorseTranslator as mt


def inputmorsedisp():
    input = input_morse.get()
    prompt = tk.Label(mframe, text = "Your input: "+input+" translates to: ", font=('Helvetica', 10), bg="#9370DB", fg="white")
    prompt.pack(padx=5, pady=5)
    mt.morse_to_char(morse_fsm, )

morsetochar = tk.Tk()
morsetochar.grab_set()
morsetochar.configure(background="#4B0082")
morsetochar.geometry("800x500")
morsetochar.title("Morse Code to Plain Text")

mframe = tk.Frame(morsetochar, bg = "#9370DB")
mframe.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

blankspace = tk.Label(mframe, bg="#9370DB")
blankspace.pack()

title = tk.Label(mframe, text = "Please Enter the Morse Code you want to translate to Plaintext:", font=('Helvetica', 16), bg="#9370DB", fg="white")
title.pack(padx=5, pady=5)

input_morse = tk.Entry(mframe, width = 50)
input_morse.pack()
    
title = tk.Label(mframe, text = "Note: Each character of morse code is separated by space, use '/' to separate words", font=('Helvetica', 10), bg="#9370DB", fg="white")
title.pack(padx=5, pady=5)

morsebtn = tk.Button(mframe, text = "Enter Morse Code", font=('Helvetica', 16), bg="#9370DB", fg="white", command =inputmorsedisp)
morsebtn.pack()

morsetochar.mainloop()