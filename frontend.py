#"""
#A program that stores following data:
#Titel, Author, Year, ISBN
#
#User Can :
#
#View all record
#search an entry
#delete entry
#update entry
#add entry
#close program
#"""


from tkinter import *
import backend

window = Tk()
window.title('BOOK Store')

def view_command():
    list1.delete(0,END)
    for row in backend.view_all():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search_all(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.add_entry(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple= list1.get(index)

        Entry_Author.delete(0,END)
        Entry_Author.insert(END,selected_tuple[2])
        Entry_Title.delete(0,END)
        Entry_Title.insert(END,selected_tuple[1])
        Entry_year.delete(0,END)
        Entry_year.insert(END,selected_tuple[3])
        Entry_ISBN.delete(0,END)
        Entry_ISBN.insert(END,selected_tuple[4])
    except IndexError:
        view_command()



def delete_command():
    backend.delete_all(selected_tuple[0])

def update_command():
    backend.update_data(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())



# Creating 4 lsbles for the entry boxes
l1 = Label(window, text= 'Title').grid(row=0, column= 0)
l2= Label(window, text= 'Author').grid(row=0, column=2 )
l3= Label(window, text= 'Year').grid(row=1, column=0 )
l4= Label(window, text= 'ISBN').grid(row=1, column=2 )

#creating entry boses for lables
title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()
Entry_Title= Entry(window, textvariable= title_text)
Entry_Title.grid(row=0 , column=1 )
Entry_Author= Entry(window, textvariable= author_text)
Entry_Author.grid(row=0, column=3 )
Entry_year= Entry(window, textvariable= year_text)
Entry_year.grid(row=1, column=1 )
Entry_ISBN= Entry(window, textvariable= isbn_text)
Entry_ISBN.grid(row=1 , column=3)


#creating scroolbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column= 2, rowspan=6)

# creating list box
list1= Listbox(window, height=6, width=30 )
list1.grid(row=2,column=0, columnspan=2, rowspan=6, padx=5)

# setting scrool bar with list and vice versa... we are telling listbox about scrool bar and telling scrool bar about list

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command = list1.yview)

# to get slected row from cursor
list1.bind('<<ListboxSelect>>',get_selected_row)
#When the user selects an item, either with a mouse click or with the arrow keys, 
# a virtual <ListboxSelect> event is generated. You can bind to it to a callback function:


#Buttons width to make buttons same size 
b1= Button(window,text = 'View All', width= 12, command=view_command).grid(row=2,column=3 , padx=5)
b2= Button(window,text = 'Search Entry', width= 12, command=search_command).grid(row=3,column=3 , padx=5)
b1= Button(window,text = 'Add Entry', width= 12, command= add_command).grid(row=4,column=3 , padx=5)
b1= Button(window,text = 'Update', width= 12, command=update_command).grid(row=5,column=3 , padx=5)
b1= Button(window,text = 'Delete', width= 12, command=delete_command).grid(row=6,column=3 , padx=5)
b1= Button(window,text = 'Close', width= 12, command= window.quit).grid(row=7,column=3 , padx=5)


window.mainloop()