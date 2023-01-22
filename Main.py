import tkinter as tk
from subprocess import call


def morse_to_text():
    call(["python", "MorsetoCharUI.py"])

def text_to_morse():
    call(["python", "TexttoMorse.py"])

#Menu UI

root = tk.Tk()
root.configure(background="#4B0082")
root.geometry("700x500")
root.title("Morse Translator")

frame = tk.Frame(root, bg = "#9370DB")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

title = tk.Label(frame, text = "Morse Translator", font=('Arial', 30), bg="#9370DB", fg="white")
title.pack(padx = 5, pady=5)

group = tk.Label(frame, text = "Prsented by Group 8 - BSCS 3AB", font=('Arial', 12), bg="#9370DB", fg="white")
group.pack(padx = 5, pady=3)

blankspace = tk.Label(frame, bg="#9370DB")
blankspace.pack()

#Translate Morse Code to Text Button
btn1 = tk.Button(frame, text="Translate Morse Code to Text", font=('Arial', 16), padx=5, pady = 10, fg="white", bg="#9400D3", command = morse_to_text)
btn1.pack(fill="both")

blankspace = tk.Label(frame, bg="#9370DB")
blankspace.pack()

#Translate English Word/s to Morse Code Button
btn2 = tk.Button(frame, text="Translate English Word/s to Morse Code", font=('Arial', 16), padx=5, pady = 10, fg="white", bg="#9400D3", command = text_to_morse)
btn2.pack(fill="both")

blankspace = tk.Label(frame, bg="#9370DB")
blankspace.pack()

#Exit Program 
btn3 = tk.Button(frame, text="Exit Program", font=('Arial', 16), padx=5, pady = 10, fg="white", bg="#9400D3", command = root.quit)
btn3.pack(fill="both")


root.mainloop()

