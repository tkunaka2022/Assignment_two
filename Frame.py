import tkinter.ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry

root =Tk()
root.title("Info Calculator")

# CREATING THE FIRST WINDOW

window_width = 500
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)


root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# CREATING THE MENU BAR

my_menubar = Menu(root)
root.config(menu=my_menubar)

file_menu = Menu(my_menubar)
my_menubar.add_cascade(
    label="Home",
    menu=file_menu
)

my_menubar.add_cascade(
    label="About",
    menu=file_menu
)


# LABEL FOR APPLICATION NAME
label = tkinter.ttk.Label(
    root,
    text='INFO CALCULATOR',
    font=("Impact", 20)
)

label.pack(ipadx=10, ipady=10)

#SEPERATOR LINE
separator = tkinter.ttk.Separator(root, orient='horizontal')
separator.pack(ipadx=200)

# LABEL FOR PERIOD
label = tkinter.ttk.Label(
    root,
    text='PERIOD ( FROM )',
    font=("Arial Bold", 10)
)

label.pack(ipadx=10, ipady=10)

# DATE PICKER
calender = DateEntry(
    root,
    width= 15,
    background= "magenta3",
    foreground= "white",
    font=("Arial ", 15)
)

calender.pack(ipady=10,ipadx=2)


root.mainloop()