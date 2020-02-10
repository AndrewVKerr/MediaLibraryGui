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
class MediaLibraryGui(object):
    
    def __init__(self):
        pass
    
    def add_new_entry(self):
        pass
    
    def mainloop(self):
        pass
    
#===[ Global Function(s) ]===


#===[ Main ]===
if __name__ == "__main__":
    datafile = open("game_lib.pickle","rb")
    games = pickle.load(datafile)
    datafile.close()
    
    media_library_gui = MediaLibraryGui()
    media_library_gui.mainloop()