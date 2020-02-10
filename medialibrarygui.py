#!/usr/bin/python3
# Andrew Kerr
# 2/10/2020

'''A GUI verson of the MediaLibrary program.

This program is used to keep track of game entrys, the ability to add/remove/edit/search entrys exist.
'''

#===[ Import(s) ]===
import pickle
import tkinter as tk
from tkinter import scrolledtext

#===[ Constant(s) ]===
TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

#===[ Class(es) ]===
class MainMenu(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self,text="Game Library", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")

    
#===[ Global Function(s) ]===


#===[ Main ]===
if __name__ == "__main__":
    datafile = open("game_lib.pickle","rb")
    games = pickle.load(datafile)
    datafile.close()
    
    root = tk.Tk()
    root.title("Media Library")
    root.geometry("500x500")
    
    main_menu = MainMenu()
    
    root.mainloop()