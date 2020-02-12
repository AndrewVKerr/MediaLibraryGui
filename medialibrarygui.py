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
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)        
        
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
        
        options = ["Genre","Title","Company","Publisher","Console","Release Year","Rating","Multi/Single player","Price","Beaten","Date Purchase"]
        self.tkvar_search_by = tk.StringVar(self)
        self.tkvar_search_by.set(options[1])
        
        self.drp_search_by = tk.OptionMenu(self,self.tkvar_search_by,*options)
        self.drp_search_by.grid(row=2,column=0,sticky="new")           
        
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
        
        self.lbl_title = tk.Label(self,text="File Saved", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")
        
        self.btn_okay = tk.Button(self,text="Ok")
        self.btn_okay.grid(row=1,column=1)
        
class EditSelectionMenu(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.lbl_title = tk.Label(self,text="Which title to edit?", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")
        
        options = ["one","two"]
        
        self.tkvar_title = tk.StringVar(self)
        self.tkvar_title.set(options[0])
        
        self.drp_title = tk.OptionMenu(self,self.tkvar_title,*options)
        self.drp_title.grid(row=1,column=0,columnspan=3,sticky="news")
        
        self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT)
        self.btn_cancel.grid(row=2,column=0,sticky="news")
        
        self.btn_select = tk.Button(self,text="Select",font=BUTTON_FONT)
        self.btn_select.grid(row=2,column=2,sticky="news")     
        
class EditEntryMenu(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)  
        self.grid_columnconfigure(4, weight=1) 
        
        self.lbl_title = tk.Label(self,text="Edit Game", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=4,sticky="news")
        
        self.lbl_genre = tk.Label(self,text="Genre: ")
        self.lbl_genre.grid(row=1,column=0,sticky="nes")
        
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row=1,column=1,sticky="nws")   
        
        self.lbl_title = tk.Label(self,text="Title: ")
        self.lbl_title.grid(row=1,column=2,sticky="nes")
        
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row=1,column=3,sticky="nws")
        
        self.lbl_company = tk.Label(self,text="Company: ")
        self.lbl_company.grid(row=2,column=0,sticky="nes")
        
        self.ent_company = tk.Entry(self)
        self.ent_company.grid(row=2,column=1,sticky="nws")           
        
        self.lbl_publisher = tk.Label(self,text="Publisher: ")
        self.lbl_publisher.grid(row=2,column=2,sticky="nes")
        
        self.ent_publisher = tk.Entry(self)
        self.ent_publisher.grid(row=2,column=3,sticky="nws")           
        
        self.lbl_console = tk.Label(self,text="Console: ")
        self.lbl_console.grid(row=3,column=0,sticky="nes")
        
        self.ent_console = tk.Entry(self)
        self.ent_console.grid(row=3,column=1,sticky="nws")     
        
        self.lbl_release_year = tk.Label(self,text="Release Year: ")
        self.lbl_release_year.grid(row=3,column=2,sticky="nes")
        
        self.ent_release_year = tk.Entry(self)
        self.ent_release_year.grid(row=3,column=3,sticky="nws")   
        
        self.lbl_rating = tk.Label(self,text="Rating: ")
        self.lbl_rating.grid(row=4,column=0,sticky="nes")
        
        self.ent_rating = tk.Entry(self)
        self.ent_rating.grid(row=4,column=1,sticky="nws")   
        
        self.lbl_multi_single = tk.Label(self,text="Player Mode: ")
        self.lbl_multi_single.grid(row=4,column=2,sticky="nes")
        
        options = ["Multi","Single"]
        
        self.tkvar_multi_single = tk.StringVar(self)
        self.tkvar_multi_single.set(options[0])
        
        self.ent_multi_single = tk.OptionMenu(self,self.tkvar_multi_single,*options)
        self.ent_multi_single.grid(row=4,column=3,sticky="news")   

        self.lbl_price = tk.Label(self,text="Price: ")
        self.lbl_price.grid(row=5,column=0,sticky="nes")
        
        self.ent_price = tk.Entry(self)
        self.ent_price.grid(row=5,column=1,sticky="nws")           
        
        self.chk_beaten = tk.Checkbutton(self,text="Beaten?")
        self.chk_beaten.grid(row=5,column=3,sticky="nws")
        
        self.lbl_notes = tk.Label(self,text="Notes:")
        self.lbl_notes.grid(row=6,column=0,sticky="ne")
        
        self.scr_notes = ScrolledText(self,width=40,height=8)
        self.scr_notes.grid(row=6,column=1,columnspan=3,rowspan=2,sticky="news")
        
        self.grid_rowconfigure(6,weight=1)
        
        self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT)
        self.btn_cancel.grid(row=8,column=1,sticky="news")
        
        self.btn_reset = tk.Button(self,text="Reset",font=BUTTON_FONT)
        self.btn_reset.grid(row=8,column=2,sticky="news")        
        
        self.btn_confirm = tk.Button(self,text="Confirm",font=BUTTON_FONT)
        self.btn_confirm.grid(row=8,column=3,sticky="news")
        
class RemoveSelectionMenu(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.lbl_title = tk.Label(self,text="Which title to remove?", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")
        
        options = ["one","two"]
        
        self.tkvar_title = tk.StringVar(self)
        self.tkvar_title.set(options[0])
        
        self.drp_title = tk.OptionMenu(self,self.tkvar_title,*options)
        self.drp_title.grid(row=1,column=0,columnspan=3,sticky="news")
        
        self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT)
        self.btn_cancel.grid(row=2,column=0,sticky="news")
        
        self.btn_select = tk.Button(self,text="Select",font=BUTTON_FONT)
        self.btn_select.grid(row=2,column=2,sticky="news")          
        
        
class RemoveConfirmMenu(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.lbl_title = tk.Label(self,text="These games are marked for Removal?", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")
        
        self.scr_marked_entrys = ScrolledText(self,width=40,height=8)
        self.scr_marked_entrys.grid(row=1,column=0,columnspan=3,sticky="news")
        
        self.grid_rowconfigure(1,weight=1)
        
        self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT)
        self.btn_cancel.grid(row=2,column=0,sticky="news")
        
        self.btn_confirm = tk.Button(self,text="Confirm?",font=BUTTON_FONT)
        self.btn_confirm.grid(row=2,column=2,sticky="news") 
        
#===[ Global Function(s) ]===


#===[ Main ]===
if __name__ == "__main__":
    datafile = open("game_lib.pickle","rb")
    games = pickle.load(datafile)
    datafile.close()
    
    root = tk.Tk()
    root.title("Media Library")
    #root.geometry("500x500")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    mainMenu = MainMenu()
    mainMenu.grid(row=0,column=0,sticky="news")
    
    searchMenu = SearchMenu()
    searchMenu.grid(row=0,column=0,sticky="news")
    
    fileSaved = FileSaved()
    fileSaved.grid(row=0,column=0,sticky="news")
    
    editSelectionMenu = EditSelectionMenu()
    editSelectionMenu.grid(row=0,column=0,sticky="news")
    
    editEntryMenu = EditEntryMenu()
    editEntryMenu.grid(row=0,column=0,sticky="news")
    
    removeSelectionMenu = RemoveSelectionMenu()
    removeSelectionMenu.grid(row=0,column=0,sticky="news")
    
    removeConfirmMenu = RemoveConfirmMenu()
    removeConfirmMenu.grid(row=0,column=0,sticky="news")
    
    mainMenu.tkraise()
    searchMenu.tkraise()
    
    root.mainloop()