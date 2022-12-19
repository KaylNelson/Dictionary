#Dictionary
from pydictionary import Dictionary as dy


#tkinter
import tkinter as tk
from tkinter import *

#customtkinter
import customtkinter as ctk


root = ctk.CTk()
root.geometry('700x550')
root.title("Ultimate Dictionary")


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


frame = ctk.CTkFrame(master=root, corner_radius=20)
frame.pack(pady=20, padx=60, fill='both', expand=True)

#Funcitons

def definition():
    output.delete(1.0, END)
    define= dy(word_defi.get())
    lyst = define.meanings()
    myString = '\n'.join(f'{i+1}. {e}' for i, e in enumerate(lyst))
    output.insert("0.0", myString)


def synonym():
    output.delete(1.0, END)
    define= dy(word_syn.get())
    lyst = define.synonyms()
    myString = '\n'.join(f'{i+1}. {e}' for i, e in enumerate(lyst))
    output.insert("0.0", myString)


def antonym():
    output.delete(1.0, END)
    define= dy(word_ant.get())
    lyst = define.antonyms()
    myString = '\n'.join(f'{i+1}. {e}' for i, e in enumerate(lyst))
    output.insert("0.0", myString)

#Definition

frame.label_defi = ctk.CTkLabel(master=frame, text="DEFINITION:", font=('Times', 30), text_color="White")
frame.label_defi.place(x=10, y=5, anchor=tk.NW)

word_defi = ctk.CTkEntry(master=frame, placeholder_text="Enter word here", font=('Times', 20), text_color="white",
                               width=250, height=30)
word_defi.place(x=200, y=8)

defi_button = ctk.CTkButton(master=frame, text="Lookup", command=definition, width=100, height=30, fg_color="#31C5C7", hover_color="#1F7B7C")
defi_button.place(x=465, y=8)

#Synonym

label_syn = ctk.CTkLabel(master=frame, text="SYNONYM:", font=('Times', 30), text_color="White")
label_syn.place(x=10, y=75)

word_syn = ctk.CTkEntry(master=frame, placeholder_text="Enter word here", font=('Times', 20), 
                               width=250, height=30)
word_syn.place(x=200, y=77)

syn_button = ctk.CTkButton(master=frame, text="Lookup", command=synonym, width=100, height=30, fg_color="#31C5C7", hover_color="#1F7B7C")
syn_button.place(x=465, y=77)

#Antonym

label_ant = ctk.CTkLabel(master=frame, text="ANTONYM:", font=('Times', 30), text_color="White")
label_ant.place(x=10, y=145)

word_ant = ctk.CTkEntry(master=frame, placeholder_text="Enter word here", font=('Times', 20), width=250, height=30)
word_ant.place(x=200, y=147)

ant_button = ctk.CTkButton(master=frame, text="Lookup", command=antonym, width=100, height=30, fg_color="#31C5C7", hover_color="#1F7B7C")
ant_button.place(x=465, y=147)

#Answer

output = ctk.CTkTextbox(master=frame, width=560, height=300, corner_radius=15)
output.place(x=10, y=200)


root.mainloop()
