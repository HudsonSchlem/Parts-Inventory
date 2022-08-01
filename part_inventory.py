
from ctypes import resize
from sqlite3 import Row
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from turtle import width
from db import Database
from PIL import ImageTk, Image
    
#-----------------------------------------------------------

#Linking Database

db = Database('store.db')

#Declaring functions

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if part_text.get() == '' or specs_text.get() == '' or quantity_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(quantity_text.get(), part_text.get(), specs_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (quantity_text.get(), part_text.get(), specs_text.get(), price_text.get()))
    
    clear_text()
    populate_list()

def selected_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        quantity_entry.delete(0, END)
        quantity_entry.insert(END, selected_item[1])
        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[2])
        specs_entry.delete(0, END)
        specs_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], part_text.get(), specs_text.get(),
    quantity_text.get(), price_text.get())
    populate_list()

def clear_text():
    part_entry.delete(0, END)
    specs_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)

#-----------------------------------------------------------

#Window
main = Tk()
main.title('PC Part Inventory')
main.geometry('950x750')
main.configure(bg='#A5E384')

#-----------------------------------------------------------

#Welcome messagebox to continue or quit
result = messagebox.askyesno(
    title='Welcome!', 
    message='Would you like to continue to your Inventory?', 
    detail = 'Click NO to quit.')

if not result:
    exit()



#-----------------------------------------------------------
#Added spaces in the beginning of the text so it lines up to the entry boxes evenly to make it look nicer.

#Brand/Part Name label for user input.
part_text = StringVar()
part_label = Label(main, text='         BRAND/PART NAME:', bg='#A5E384' , font=('Helvetica', 20, 'bold'), pady=20)
part_label.grid(row=1, column=0, sticky=W)
part_entry = Entry(main, textvariable=part_text)
part_entry.grid(row=1, column=1, pady=20)

#Specification of the item ( This allows for the user to separate the part name from the specifications of the product.)
specs_text = StringVar()
specs_label = Label(main, text='  SPECIFICATIONS:', bg='#A5E384', font=('Helvetica', 20, 'bold'), pady=20)
specs_label.grid(row=1, column=2, sticky=W)
specs_entry = Entry(main, textvariable=specs_text)
specs_entry.grid(row=1, column=3, pady=20)

#quantity (Which specifies the quantity the product.)
quantity_text = StringVar()
quantity_label = Label(main, text='                         QUANTITY:', bg='#A5E384', font=('Helvetica', 20, 'bold'), pady=20)
quantity_label.grid(row=3, column=0, sticky=W)
quantity_entry = Entry(main, textvariable=quantity_text)
quantity_entry.grid(row=3, column=1, pady=20)

#Price (Shows the price at which is was bought for or can be sold for.)
price_text = StringVar()
price_label = Label(main, text='                    PRICE:', bg='#A5E384', font=('Helvetica', 20, 'bold'), pady=20)
price_label.grid(row=3, column=2, sticky=W)
price_entry = Entry(main, textvariable=price_text)
price_entry.grid(row=3, column=3, pady=20)

#-----------------------------------------------------------

#Added in this code for the Manual window. This was the only way to insert another GUI since TK only allows 1 mainloop

def openNewWindow():
     
    # I added a TopLevel widget to open the second GUI for the manual_button (Took me forever to look this up lol)
    newWindow = Toplevel(main)
    newWindow.title("Manual")
    newWindow.geometry("=750x500")
    newWindow.configure(bg='#CEDAD5')
    
    #Here I will list the manual step by step (I was going to use \n to break but it was annoying)
    
    label_1= Label(newWindow, text ="Welcome!", bg='#CEDAD5' , font=('Helvetica', 17, 'bold')).pack()
    label_2 = Label(newWindow, text ="", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_3 = Label(newWindow, text="Step 1: Enter the Brand/Part name for example: AMD, NVIDIA, INTEL...", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_4 = Label(newWindow, text="Step 2: Enter the Specifications for example: 8GB DDr4, 8 Core, 4.2GHz...", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_5 = Label(newWindow, text="Step 3: Enter the Quantity of the item you would like to add for example: 1,200,3000...", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_6 = Label(newWindow, text="Step 4: Enter the Price of item you would like to add for example: $250, $4, $50000...", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_7 = Label(newWindow, text="Step 5: After inserting all of the top, press ADD ITEM to insert it into your inventory!", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_8 = Label(newWindow, text="", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_9 = Label(newWindow, text="", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_10 = Label(newWindow, text="If you would like to Remove part, click on the part in the inventory, then click REMOVE.", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_11 = Label(newWindow, text="", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_12 = Label(newWindow, text="If you would like to Update part, click on the part in the inventory, then click UPDATE.", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_13= Label(newWindow, text="", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_14= Label(newWindow, text="If you would like to Clear all text, click CLEAR to erase all entry text.", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_15= Label(newWindow, text="", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_16= Label(newWindow, text="", bg='#CEDAD5', font=('Helvetica', 12)).pack()
    label_17= Label(newWindow, text="ENJOY!", bg='#CEDAD5', font=('Helvetica', 12, 'bold')).pack()
    label_18= Label(newWindow, text="", bg='#CEDAD5', font=('Helvetica', 12)).pack()
#-----------------------------------------------------------

#This section is for the library directory for the inputed data from the user to be displayed.

#Parts List (ListBox for the future database)
parts_list = Listbox(main, height=15, width=115, border=2)
parts_list.grid(row=6, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Scrollbar for the future database
scrollbar = Scrollbar(main)
scrollbar.grid(row=6, column=3)

#Attach scrollbox to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#BIND SELECT
parts_list.bind('<<ListboxSelect>>', selected_item)

#-----------------------------------------------------------

#Adding Image under manual button and to the far right (Due to not creating Canvas's I can't make the images PNG...)

my_img = PhotoImage(file="manual.png")

label_image = Label(main, image=my_img).grid(row= 15, column=1)

my_img2 = PhotoImage(file="inventoryimg.png")

label_image2 = Label(main, image=my_img2).grid(row= 15, column=3)

#-----------------------------------------------------------

#Five Buttons for Adding, Removing, Updating, Clearing, and the Manual at the bottom.
add_button = Button(main, text='Add Part', width=12, command=add_item)
add_button.grid(row=5, column=0, pady=20)

remove_button = Button(main, text='Remove Part', width=12, command=remove_item)
remove_button.grid(row=5, column=1)

update_button = Button(main, text='Update Part', width=12, command=update_item)
update_button.grid(row=5, column=2)

clear_button = Button(main, text='Clear', width=12, command=clear_text)
clear_button.grid(row=5, column=3)

manual_button = Button(main, text ="CLICK HERE TO GET STARTED!", command = openNewWindow)
manual_button.grid(row=12, column=1, pady = 10, sticky=S)

#-----------------------------------------------------------


#Populate Data for the database
populate_list()

#Mainloop that starts the application.
main.mainloop()