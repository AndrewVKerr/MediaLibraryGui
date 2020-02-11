#!/usr/bin/python3
# Andrew Kerr
# 2/10/2020

'''A GUI verson of the MediaLibrary program.

This program is used to keep track of game entrys, the ability to add/remove/edit/search entrys exist.
'''

#===[ Import(s) ]===
import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
#===[ Constant(s) ]===
TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

#===[ Class(es) ]===
class MainMenu(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self,text="Game Library", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")
        
        self.btn_add = tk.Button(self,text="Add",font=BUTTON_FONT)
        self.btn_add.grid(row=1,column=1)
        
        self.btn_edit = tk.Button(self,text="Edit",font=BUTTON_FONT)
        self.btn_edit.grid(row=2,column=1) 
        
        self.btn_search = tk.Button(self,text="Search",font=BUTTON_FONT)
        self.btn_search.grid(row=3,column=1)
        
        self.btn_remove = tk.Button(self,text="Remove",font=BUTTON_FONT)
        self.btn_remove.grid(row=4,column=1)
        
        self.btn_save = tk.Button(self,text="Save",font=BUTTON_FONT)
        self.btn_save.grid(row=5,column=1)    

class SearchMenu(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.lbl_title = tk.Label(self,text="Search", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")
        
        self.lbl_search_by = tk.Label(self,text="Search by:")
        self.lbl_search_by.grid(row=1,column=0,sticky="sw")
        
        self.ent_search_by = tk.Entry(self)
        self.ent_search_by.grid(row=2,column=0,sticky="nw")           
        
        self.lbl_search_for = tk.Label(self,text="Search for:")
        self.lbl_search_for.grid(row=3,column=0,sticky="sw")
        
        self.ent_search_for = tk.Entry(self)
        self.ent_search_for.grid(row=4,column=0,sticky="nw")        
        
        self.lbl_print_filters = tk.Label(self,text="Print Filters:")
        self.lbl_print_filters.grid(row=1,column=1,columnspan=2,sticky="news")
        
        self.frm_filters = PrintFilters(self)
        self.frm_filters.grid(row=2,column=1,rowspan=3,columnspan=2,sticky="news")      
        
        self.scr_search_results = ScrolledText(self,width=40,height=8)
        self.scr_search_results.grid(row=5,column=0,columnspan=3,sticky="news")
        
        self.grid_rowconfigure(5,weight=1)
        
        self.btn_back = tk.Button(self,text="Back",font=BUTTON_FONT)
        self.btn_back.grid(row=6,column=0,sticky="news")
        
        self.btn_reset = tk.Button(self,text="Reset",font=BUTTON_FONT)
        self.btn_reset.grid(row=6,column=1,sticky="news")
        
        self.btn_submit = tk.Button(self,text="Submit",font=BUTTON_FONT)
        self.btn_submit.grid(row=6,column=2,sticky="news")
        

class PrintFilters(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        
        self.chk_title = tk.Checkbutton(self,text="Title")
        self.chk_title.grid(row=0,column=0,sticky="nsw")
        
        self.chk_genre = tk.Checkbutton(self,text="Genre")
        self.chk_genre.grid(row=0,column=1,sticky="nsw")  
        
        self.chk_company = tk.Checkbutton(self,text="Company")
        self.chk_company.grid(row=0,column=2,sticky="nsw")        
        
        self.chk_publisher = tk.Checkbutton(self,text="Publisher")
        self.chk_publisher.grid(row=1,column=0,sticky="nsw")        
        
        self.chk_release_year = tk.Checkbutton(self,text="Release Year")
        self.chk_release_year.grid(row=1,column=1,sticky="nsw")        
        
        self.chk_console = tk.Checkbutton(self,text="Console")
        self.chk_console.grid(row=1,column=2,sticky="nsw")        
        
        self.chk_rating = tk.Checkbutton(self,text="Rating")
        self.chk_rating.grid(row=2,column=0,sticky="nsw")
        
        self.chk_single_multi = tk.Checkbutton(self,text="Single/Multi Player")
        self.chk_single_multi.grid(row=2,column=1,sticky="nsw")         
        
        self.chk_price = tk.Checkbutton(self,text="Price")
        self.chk_price.grid(row=2,column=2,sticky="nsw")
        
        self.chk_beaten = tk.Checkbutton(self,text="Beaten?")
        self.chk_beaten.grid(row=3,column=0,sticky="nsw")         
        
        self.chk_purchase_date = tk.Checkbutton(self,text="Date Purchase")
        self.chk_purchase_date.grid(row=3,column=1,sticky="nsw")
        
        self.chk_notes = tk.Checkbutton(self,text="Notes")
        self.chk_notes.grid(row=3,column=2,sticky="nsw")           
        

class FileSaved(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.lbl_title = tk.Label(self,text="Search", font=TITLE_FONT)
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
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    main_menu = MainMenu()
    main_menu.grid(row=0,column=0,sticky="news")
    
    search_menu = SearchMenu()
    search_menu.grid(row=0,column=0,sticky="news")
    
    root.mainloop()