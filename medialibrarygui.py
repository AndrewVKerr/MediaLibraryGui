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
from tkinter import messagebox as mb

#===[ Constant(s) ]===
TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

#===[ Class(es) ]===

class Screen(tk.Frame):

	current = 0

	def __init__(self,master):
		tk.Frame.__init__(self,master)

	def switch_frame():
		screens[Screen.current].tkraise()

class MainMenu(Screen):

	def __init__(self,master=None):
		Screen.__init__(self,master)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)        

		self.lbl_title = tk.Label(self,text="Game Library", font=TITLE_FONT)
		self.lbl_title.grid(row=1,column=0,columnspan=3,sticky="news")

		self.btn_add = tk.Button(self,text="Add",font=BUTTON_FONT,command=self.go_add)
		self.btn_add.grid(row=2,column=1,sticky="news")

		self.btn_edit = tk.Button(self,text="Edit",font=BUTTON_FONT,command=self.go_edit)
		self.btn_edit.grid(row=3,column=1,sticky="news") 

		self.btn_search = tk.Button(self,text="Search",font=BUTTON_FONT,command=self.go_search)
		self.btn_search.grid(row=4,column=1,sticky="news")

		self.btn_remove = tk.Button(self,text="Remove",font=BUTTON_FONT,command=self.go_remove)
		self.btn_remove.grid(row=5,column=1,sticky="news")

		self.btn_save = tk.Button(self,text="Save",font=BUTTON_FONT,command=self.go_save)
		self.btn_save.grid(row=6,column=1,sticky="news") 

		self.grid_rowconfigure(0,weight=2)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(7,weight=2)

	def go_add(self):
		Screen.current = 1
		Screen.switch_frame()

	def go_edit(self):
		#Screen.current = 2
		#Screen.switch_frame()
		pop_up = tk.Tk()
		pop_up.title("Edit Selection")
		editSelect = EditSelectionMenu(master=pop_up)
		editSelect.grid(row=0,column=0,sticky="news")

	def go_search(self):
		Screen.current = 3
		screens[Screen.current].reset()
		Screen.switch_frame()        

	def go_remove(self):
		#Screen.current = 4
		#Screen.switch_frame()    
		pop_up = tk.Tk()
		pop_up.title("Remove Game")
		removeSelect = RemoveSelectionMenu(master=pop_up)
		removeSelect.grid(row=0,column=0,sticky="news")

	def go_save(self):
		print("Saved")
		datafile = open("game_lib.pickle","wb")
		pickle.dump(games,datafile)
		datafile.close()
		mb.showinfo(message="Saved Entrys to File.")

class SearchMenu(Screen):

	prefix = [
            "Genre",
        "Title",
        "Company",
        "Publisher",
        "Console",
        "Release Year",
        "Rating",
        "Multi/Single player",
        "Price",
        "Beaten",
        "Date Purchase",
        "Notes"
    ]    

	def __init__(self,master=None):
		Screen.__init__(self,master)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)

		self.lbl_title = tk.Label(self,text="Search", font=TITLE_FONT)
		self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")

		self.lbl_search_by = tk.Label(self,text="Search by:")
		self.lbl_search_by.grid(row=1,column=0,sticky="sw")

		self.options = [
	        "Select Option",
	    "Genre",
	    "Title",
	    "Company",
	    "Publisher",
	    "Console",
	    "Release Year",
	    "Rating",
	    "Multi/Single player",
	    "Price",
	    "Beaten",
	    "Date Purchase"
	]
		self.tkvar_search_by = tk.StringVar(self)
		self.tkvar_search_by.set(self.options[0])

		self.dbx_search_by = tk.OptionMenu(self,self.tkvar_search_by,*self.options)
		self.dbx_search_by.grid(row=2,column=0,sticky="new")           

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

		self.btn_back = tk.Button(self,text="Back",font=BUTTON_FONT,command=self.go_back)
		self.btn_back.grid(row=6,column=0,sticky="news")

		self.btn_reset = tk.Button(self,text="Reset",font=BUTTON_FONT,command=self.reset)
		self.btn_reset.grid(row=6,column=1,sticky="news")

		self.btn_submit = tk.Button(self,text="Submit",font=BUTTON_FONT,command=self.submit)
		self.btn_submit.grid(row=6,column=2,sticky="news")

	def go_back(self):
		Screen.current = 0
		Screen.switch_frame() 

	def reset(self):
		#self.frm_filters.tkvar_title.set(False)
		self.frm_filters.reset()
		self.ent_search_for.delete(0,tk.END)
		self.scr_search_results.delete(0.0,tk.END)
		for key in games.keys():
			self.display_game(games[key])

	def submit(self):
		print("Yield Results")
		#Delete previous info
		self.scr_search_results.delete(0.0,tk.END)

		#Get search_index
		search_index = -1
		for i in range(0,len(self.options)+1):
			if self.options[i] == self.tkvar_search_by.get():
				search_index = i-1
				break

		search_for = self.ent_search_for.get()
		for key in games.keys():
			game = games[key]
			if(search_index == -1):
				self.display_game(game)
			else:
				if search_for.lower() in game[search_index].lower():    
					self.display_game(game)

	#Display the given game using the given filters.
	def display_game(self,game):      
		if self.frm_filters.tkvar_genre.get() == True:
			msg = "Genre:\t\t"+game[0]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_title.get() == True:
			msg = "Title:\t\t"+game[1]+"\n"
			self.scr_search_results.insert(tk.END,msg)  

		if self.frm_filters.tkvar_company.get() == True:
			msg = "Company:\t\t"+game[2]+"\n"
			self.scr_search_results.insert(tk.END,msg)        

		if self.frm_filters.tkvar_publisher.get() == True:
			msg = "Publisher:\t\t"+game[3]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_console.get() == True:
			msg = "Console:\t\t"+game[4]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_release_year.get() == True:
			msg = "Release Year:\t\t"+game[5]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_rating.get() == True:
			msg = "Rating:\t\t"+game[6]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_single_multi.get() == True:
			msg = "Single/Multi:\t\t"+game[7]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_price.get() == True:
			msg = "Price:\t\t"+game[8]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_beaten.get() == True:
			msg = "Beaten:\t\t"+game[9]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_date_purchased.get() == True:
			msg = "Date Purchased:\t"+game[10]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		if self.frm_filters.tkvar_notes.get() == True:
			msg = "Notes:\t\t"+game[11]+"\n"
			self.scr_search_results.insert(tk.END,msg)

		# Looped Print (ALT)
		# Add filters parameter and pass self.frm_filters.get_filters() or call it in this function
		#-------------------------------------------------------------------------------------------
		#for j in range(len(filters)):
		#    if filters[j]:
		#        self.scr_search_results.insert(tk.END,SearchMenu.prefix[j]+": "+game[j]+"\n")
		self.scr_search_results.insert(tk.END,"-"*67+"\n")


class PrintFilters(tk.Frame):

	def __init__(self,master):
		tk.Frame.__init__(self,master)

		self.tkvar_title = tk.BooleanVar(self)
		self.tkvar_title.set(True)

		self.chk_title = tk.Checkbutton(self,text="Title",variable=self.tkvar_title)
		self.chk_title.grid(row=0,column=0,sticky="nsw")

		self.tkvar_genre = tk.BooleanVar(self)
		self.tkvar_genre.set(True)        

		self.chk_genre = tk.Checkbutton(self,text="Genre",variable=self.tkvar_genre)
		self.chk_genre.grid(row=0,column=1,sticky="nsw")  

		self.tkvar_company = tk.BooleanVar(self)
		self.tkvar_company.set(True)        

		self.chk_company = tk.Checkbutton(self,text="Company",variable=self.tkvar_company)
		self.chk_company.grid(row=0,column=2,sticky="nsw")        

		self.tkvar_publisher = tk.BooleanVar(self)
		self.tkvar_publisher.set(True)        

		self.chk_publisher = tk.Checkbutton(self,text="Publisher",variable=self.tkvar_publisher)
		self.chk_publisher.grid(row=1,column=0,sticky="nsw")        

		self.tkvar_release_year = tk.BooleanVar(self)
		self.tkvar_release_year.set(True)             

		self.chk_release_year = tk.Checkbutton(self,text="Release Year",variable=self.tkvar_release_year)
		self.chk_release_year.grid(row=1,column=1,sticky="nsw")        

		self.tkvar_console = tk.BooleanVar(self)
		self.tkvar_console.set(True)         

		self.chk_console = tk.Checkbutton(self,text="Console",variable=self.tkvar_console)
		self.chk_console.grid(row=1,column=2,sticky="nsw")        

		self.tkvar_rating = tk.BooleanVar(self)
		self.tkvar_rating.set(True)         

		self.chk_rating = tk.Checkbutton(self,text="Rating",variable=self.tkvar_rating)
		self.chk_rating.grid(row=2,column=0,sticky="nsw")

		self.tkvar_single_multi = tk.BooleanVar(self)
		self.tkvar_single_multi.set(True)         

		self.chk_single_multi = tk.Checkbutton(self,text="Single/Multi Player",variable=self.tkvar_single_multi)
		self.chk_single_multi.grid(row=2,column=1,sticky="nsw")         

		self.tkvar_price = tk.BooleanVar(self)
		self.tkvar_price.set(True)        

		self.chk_price = tk.Checkbutton(self,text="Price",variable=self.tkvar_price)
		self.chk_price.grid(row=2,column=2,sticky="nsw")

		self.tkvar_beaten = tk.BooleanVar(self)
		self.tkvar_beaten.set(True)        

		self.chk_beaten = tk.Checkbutton(self,text="Beaten?",variable=self.tkvar_beaten)
		self.chk_beaten.grid(row=3,column=0,sticky="nsw")         

		self.tkvar_date_purchased = tk.BooleanVar(self)
		self.tkvar_date_purchased.set(True)        

		self.chk_purchase_date = tk.Checkbutton(self,text="Date Purchase",variable=self.tkvar_date_purchased)
		self.chk_purchase_date.grid(row=3,column=1,sticky="nsw")

		self.tkvar_notes = tk.BooleanVar(self)
		self.tkvar_notes.set(True)        

		self.chk_notes = tk.Checkbutton(self,text="Notes",variable=self.tkvar_notes)
		self.chk_notes.grid(row=3,column=2,sticky="nsw") 

	def reset(self):
		self.tkvar_beaten.set(True)
		self.tkvar_company.set(True)
		self.tkvar_console.set(True)
		self.tkvar_date_purchased.set(True)
		self.tkvar_genre.set(True)
		self.tkvar_notes.set(True)
		self.tkvar_price.set(True)
		self.tkvar_publisher.set(True)
		self.tkvar_rating.set(True)
		self.tkvar_release_year.set(True)
		self.tkvar_single_multi.set(True)
		self.tkvar_title.set(True)

	def get_filters(self):
		return [
	        self.tkvar_genre.get(),
	    self.tkvar_title.get(),
	    self.tkvar_company.get(),
	    self.tkvar_publisher.get(),
	    self.tkvar_console.get(),
	    self.tkvar_release_year.get(),
	    self.tkvar_rating.get(),
	    self.tkvar_single_multi.get(),
	    self.tkvar_price.get(),
	    self.tkvar_date_purchased.get(),
	    self.tkvar_beaten.get(),
	    self.tkvar_notes.get()
	]

'''class FileSaved(Screen):

    def __init__(self):
        Screen.__init__(self)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.lbl_title = tk.Label(self,text="File Saved", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")

        self.btn_okay = tk.Button(self,text="Ok",command=self.go_ok)
        self.btn_okay.grid(row=1,column=1)

    def go_ok(self):
        Screen.current = 0
        Screen.switch_frame()     '''

class EditSelectionMenu(tk.Frame):

	def __init__(self,master=None):
		tk.Frame.__init__(self,master)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)

		self.lbl_title = tk.Label(self,text="Which title to edit?", font=TITLE_FONT)
		self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")

		self.options = ["Select a Title"]

		for key in games.keys():
			self.options.append(games[key][1])

		self.tkvar_title = tk.StringVar(self)
		self.tkvar_title.set(self.options[0])

		self.dbx_title = tk.OptionMenu(self,self.tkvar_title,*self.options)
		self.dbx_title.grid(row=1,column=0,columnspan=3,sticky="news")

		self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT,command=self.go_cancel)
		self.btn_cancel.grid(row=2,column=0,sticky="news")

		self.btn_select = tk.Button(self,text="Select",font=BUTTON_FONT,command=self.select)
		self.btn_select.grid(row=2,column=2,sticky="news")   

	def go_cancel(self):
		Screen.current = 0
		Screen.switch_frame()
		self.master.destroy()

	def select(self):
		#Check if the selection has not been made.
		title = self.tkvar_title.get()
		if(title == self.options[0]):
			pass
		else:
			#Update the next screen before switching the frame.
			Screen.current = 2
			for i in range(len(self.options)):
				if self.options[i] == title:
					screens[Screen.current].edit_key = i
					break
			screens[Screen.current].update()
			Screen.switch_frame()

			#Destroy the master
			self.master.destroy()


class EditEntryMenu(Screen):

	def __init__(self,master=None):
		Screen.__init__(self,master)

		self.edit_key = 0

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

		self.options = ["Please select an option.","Multi","Single","Both"]

		self.tkvar_multi_single = tk.StringVar(self)
		self.tkvar_multi_single.set(self.options[0])

		self.drb_multi_single = tk.OptionMenu(self,self.tkvar_multi_single,*self.options)
		self.drb_multi_single.grid(row=4,column=3,sticky="news")   

		self.lbl_price = tk.Label(self,text="Price: ")
		self.lbl_price.grid(row=5,column=0,sticky="nes")

		self.ent_price = tk.Entry(self)
		self.ent_price.grid(row=5,column=1,sticky="nws")           

		self.lbl_date_purchased = tk.Label(self,text="Date Purchased: ")
		self.lbl_date_purchased.grid(row=5,column=2,sticky="nes")

		self.ent_date_purchased = tk.Entry(self)
		self.ent_date_purchased.grid(row=5,column=3,sticky="nws")           

		self.tkvar_beaten = tk.BooleanVar(self)
		self.tkvar_beaten.set(False)

		self.chk_beaten = tk.Checkbutton(self,text="Beaten?",variable=self.tkvar_beaten)
		self.chk_beaten.grid(row=6,column=3,sticky="nws")

		self.lbl_notes = tk.Label(self,text="Notes:")
		self.lbl_notes.grid(row=7,column=0,sticky="ne")

		self.scr_notes = ScrolledText(self,width=40,height=8)
		self.scr_notes.grid(row=7,column=1,columnspan=3,rowspan=2,sticky="news")

		self.grid_rowconfigure(7,weight=1)

		self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT,command=self.go_cancel)
		self.btn_cancel.grid(row=9,column=1,sticky="news")

		self.btn_reset = tk.Button(self,text="Reset",font=BUTTON_FONT,command=self.reset)
		self.btn_reset.grid(row=9,column=2,sticky="news")        

		self.btn_confirm = tk.Button(self,text="Confirm",font=BUTTON_FONT,command=self.confirm)
		self.btn_confirm.grid(row=9,column=3,sticky="news")


	def update(self):
		game = games[self.edit_key]
		self.ent_title.delete(0,"end")
		self.ent_title.insert(0,game[1])

		self.ent_genre.delete(0,"end")
		self.ent_genre.insert(0,game[0])

		self.ent_company.delete(0,"end")
		self.ent_company.insert(0,game[2])

		self.ent_publisher.delete(0,"end")
		self.ent_publisher.insert(0,game[3])

		self.ent_console.delete(0,"end")
		self.ent_console.insert(0,game[4])

		self.ent_release_year.delete(0,"end")
		self.ent_release_year.insert(0,game[5])

		self.ent_rating.delete(0,"end")
		self.ent_rating.insert(0,game[6])

		player_mode = game[7]
		if not player_mode in self.options:
			player_mode = self.options[0]
		self.tkvar_multi_single.set(player_mode)

		self.ent_price.delete(0,"end")
		self.ent_price.insert(0,game[8])

		#Check for boolean data contained in is_beaten (game[9]) set data accordingly.
		is_beaten = game[9]
		is_beaten = str(is_beaten).lower() in ["true","yes","1"]
		self.tkvar_beaten.set(is_beaten)

		self.ent_date_purchased.delete(0,"end")
		self.ent_date_purchased.insert(0,game[10])

		self.scr_notes.delete(0.0,"end")
		self.scr_notes.insert(0.0,game[11])

	def go_cancel(self):
		Screen.current = 0
		Screen.switch_frame() 

	def reset(self):
		self.update()    

	def confirm(self):
		if not self.submit_edit(): # If the submit_edit function returns False then it failed to update the entry.
			return
		Screen.current = 0
		Screen.switch_frame()   

	def submit_edit(self):
		if(self.ent_title.get() == ""):
			popup = tk.Tk()
			popup.title("Must have Title!")
			msg = "Entry must have Title!"
			error_message = ErrorMessage(popup,msg)
			error_message.grid(row=0,column=0,sticky="news")
			return False		
		
		entry = []

		#Create a new entry and populate it with user input.
		entry.append(self.ent_genre.get())          #0
		entry.append(self.ent_title.get())          #1
		entry.append(self.ent_company.get())        #2
		entry.append(self.ent_publisher.get())      #3
		entry.append(self.ent_console.get())        #4
		entry.append(self.ent_release_year.get())   #5
		entry.append(self.ent_rating.get())         #6

		#Check for default option if found save an empty string.
		if not(self.tkvar_multi_single.get() == self.options[0]):
			entry.append(self.tkvar_multi_single.get()) #7
		else:
			entry.append("")                        #7(Alt) 

		entry.append(self.ent_price.get())          #8
		entry.append(str(self.tkvar_beaten.get()))  #9
		entry.append(self.ent_date_purchased.get()) #10
		entry.append(self.scr_notes.get(0.0,tk.END))#11

		games[self.edit_key] = entry
		self.edit_key = 0
		
		return True

class AddEntryMenu(Screen):

	def __init__(self,master=None):
		Screen.__init__(self,master)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)
		self.grid_columnconfigure(3, weight=1)  
		self.grid_columnconfigure(4, weight=1) 

		self.lbl_title = tk.Label(self,text="Add Game", font=TITLE_FONT)
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

		self.options = ["Please select an option.","Multi","Single","Both"]

		self.tkvar_multi_single = tk.StringVar(self)
		self.tkvar_multi_single.set(self.options[0])

		self.drb_multi_single = tk.OptionMenu(self,self.tkvar_multi_single,*self.options)
		self.drb_multi_single.grid(row=4,column=3,sticky="news")   

		self.lbl_price = tk.Label(self,text="Price: ")
		self.lbl_price.grid(row=5,column=0,sticky="nes")

		self.ent_price = tk.Entry(self)
		self.ent_price.grid(row=5,column=1,sticky="nws")           

		self.lbl_date_purchased = tk.Label(self,text="Date Purchased: ")
		self.lbl_date_purchased.grid(row=5,column=2,sticky="nes")

		self.ent_date_purchased = tk.Entry(self)
		self.ent_date_purchased.grid(row=5,column=3,sticky="nws")           

		self.tkvar_beaten = tk.BooleanVar(self)
		self.tkvar_beaten.set(False)

		self.chk_beaten = tk.Checkbutton(self,text="Beaten?",variable=self.tkvar_beaten)
		self.chk_beaten.grid(row=6,column=3,sticky="nws")

		self.lbl_notes = tk.Label(self,text="Notes:")
		self.lbl_notes.grid(row=7,column=0,sticky="ne")

		self.scr_notes = ScrolledText(self,width=40,height=8)
		self.scr_notes.grid(row=7,column=1,columnspan=3,rowspan=2,sticky="news")

		self.grid_rowconfigure(7,weight=1)


		self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT,command=self.go_cancel)
		self.btn_cancel.grid(row=9,column=1,sticky="news")

		self.btn_reset = tk.Button(self,text="Reset",font=BUTTON_FONT,command=self.reset)
		self.btn_reset.grid(row=9,column=2,sticky="news")        

		self.btn_confirm = tk.Button(self,text="Confirm",font=BUTTON_FONT,command=self.go_confirm)
		self.btn_confirm.grid(row=9,column=3,sticky="news")

	def go_cancel(self):
		self.reset()
		Screen.current = 0
		Screen.switch_frame() 

	def reset(self):
		self.ent_title.delete(0,"end")
		self.ent_genre.delete(0,"end")
		self.ent_company.delete(0,"end")
		self.ent_publisher.delete(0,"end")
		self.ent_console.delete(0,"end")
		self.ent_release_year.delete(0,"end")
		self.ent_rating.delete(0,"end")
		self.tkvar_multi_single.set(self.options[0])
		self.ent_price.delete(0,"end")
		self.tkvar_beaten.set(False)
		self.ent_date_purchased.delete(0,"end")
		self.scr_notes.delete(0.0,"end")        

	def go_confirm(self):
		if not self.create_entry():
			return
		self.reset()
		Screen.current = 0
		Screen.switch_frame()
		mb.showinfo(message="Entry has been added.")

	def create_entry(self):
		entry = []

		if(self.ent_title.get()==""):
			pop_up = tk.Tk()
			pop_up.title("Error")
			msg = "Error, select a title."
			frm_error = ErrorMessage(pop_up,msg)
			frm_error.grid(row=0,column=0)
			return

		#Create a new entry and populate it with user input.
		entry.append(self.ent_genre.get())          #0
		entry.append(self.ent_title.get())          #1
		entry.append(self.ent_company.get())        #2
		entry.append(self.ent_publisher.get())      #3
		entry.append(self.ent_console.get())        #4
		entry.append(self.ent_release_year.get())   #5
		entry.append(self.ent_rating.get())         #6

		#Check for default option if found save an empty string.
		if not(self.tkvar_multi_single.get() == self.options[0]):
			entry.append(self.tkvar_multi_single.get()) #7
		else:
			entry.append("")                        #7(Alt) 

		entry.append(self.ent_price.get())          #8
		entry.append(str(self.tkvar_beaten.get()))  #9
		entry.append(self.ent_date_purchased.get()) #10
		entry.append(self.scr_notes.get(0.0,tk.END))#11

		games[len(games)+1] = entry 
		return True

class RemoveSelectionMenu(tk.Frame):

	def __init__(self,master=None):
		tk.Frame.__init__(self,master)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)

		self.lbl_title = tk.Label(self,text="Which title to remove?", font=TITLE_FONT)
		self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")

		self.options = ["Please select a title."]

		for key in games.keys():
			self.options.append(games[key][1])

		self.tkvar_title = tk.StringVar(self)
		self.tkvar_title.set(self.options[0])

		self.dbx_title = tk.OptionMenu(self,self.tkvar_title,*self.options)
		self.dbx_title.grid(row=1,column=0,columnspan=3,sticky="news")

		self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT,command=self.go_back)
		self.btn_cancel.grid(row=2,column=0,sticky="news")

		self.btn_select = tk.Button(self,text="Select",font=BUTTON_FONT,command=self.go_select)
		self.btn_select.grid(row=2,column=2,sticky="news") 

	def go_back(self):
		Screen.current = 0
		Screen.switch_frame()
		self.master.destroy()

	def go_select(self):
		if not(self.tkvar_title.get() == self.options[0]):
			Screen.current = 4
			for key in games.keys():
				if games[key][1] == self.tkvar_title.get():
					screens[Screen.current].remove_key = key
					break
			screens[Screen.current].update()
			Screen.switch_frame()
			self.master.destroy()


class RemoveConfirmMenu(Screen):

	def __init__(self,master=None):
		Screen.__init__(self,master)

		self.remove_key = 0

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)

		self.lbl_title = tk.Label(self,text="These games are marked for Removal?", font=TITLE_FONT)
		self.lbl_title.grid(row=0,column=0,columnspan=3,sticky="news")

		self.scr_marked_entrys = ScrolledText(self,width=40,height=8)
		self.scr_marked_entrys.grid(row=1,column=0,columnspan=3,sticky="news")

		self.grid_rowconfigure(1,weight=1)

		self.btn_cancel = tk.Button(self,text="Cancel",font=BUTTON_FONT,command=self.go_back)
		self.btn_cancel.grid(row=2,column=0,sticky="news")

		self.btn_confirm = tk.Button(self,text="Confirm?",font=BUTTON_FONT,command=self.go_confirm)
		self.btn_confirm.grid(row=2,column=2,sticky="news") 

	def go_back(self):
		Screen.current = 0
		Screen.switch_frame() 

	def remove_and_compact(self):
		selected_key = self.remove_key
		while selected_key+1 in games:
			games[selected_key] = games[selected_key+1]
			selected_key+=1
		games.pop(selected_key)

	def go_confirm(self):
		self.remove_and_compact()
		Screen.current = 0
		Screen.switch_frame()

	def update(self):
		screens[Screen.current].scr_marked_entrys.delete(0.0,tk.END)
		for i in range(len(games[self.remove_key])):
			screens[Screen.current].scr_marked_entrys.insert(tk.END,SearchMenu.prefix[i]+": "+games[self.remove_key][i]+"\n")
		#screens[Screen.current].scr_marked_entrys.insert(tk.END,games[key])        

class ErrorMessage(tk.Frame):

	def __init__(self,parent,msg='generic'):
		tk.Frame.__init__(self,master=parent)
		self.parent = parent;

		self.lbl_continue = tk.Label(self,text=msg)
		self.lbl_continue.grid(row=0,column=0,columnspan=3,sticky="news")

		self.btn_ok = tk.Button(self,text="OK",command=self.master.destroy)
		self.btn_ok.grid(row=1,column=1)

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)

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

	screens = [MainMenu(),AddEntryMenu(),EditEntryMenu(),SearchMenu(),RemoveConfirmMenu()]

	screens[0].grid(row=0,column=0,sticky="news")
	screens[1].grid(row=0,column=0,sticky="news")
	screens[2].grid(row=0,column=0,sticky="news")
	screens[3].grid(row=0,column=0,sticky="news")
	screens[4].grid(row=0,column=0,sticky="news")

	screens[0].tkraise()

	root.mainloop()