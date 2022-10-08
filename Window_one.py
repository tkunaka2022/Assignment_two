import tkinter.ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry

global root
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
root.resizable(False, False)


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
label = Label(
    root,
    text='INFO CALCULATOR',
    font=("Impact", 20)
)

label.place(x=180,y=40)


# SEPERATOR LINE
separator = tkinter.ttk.Separator(
    root,
    orient='horizontal'
)
separator.pack(fill="x",pady=100)

# LABEL FOR PERIOD
label_period = Label(
    root,
    text='PERIOD ( FROM )',
    font=("Arial Bold", 10),
)

label_period.place(x=200, y=120)


# DATE PICKER
calender = DateEntry(
    root,
    width= 15,
    background= "magenta3",
    foreground= "white",
    font=("Arial ", 15)
)

calender.place(x=30,y=150)

label_To = Label(
    root,
    text='TO',
    font=("Arial Bold", 10),
)

label_To.place(x=240, y=150)

calender = DateEntry(
    root,
    width= 15,
    background= "magenta3",
    foreground= "white",
    font=("Arial ", 15)
)

calender.place(x=280,y=150)

def next():
    root.withdraw()
    global data_page
    data_page = Toplevel()

    window_width = 500
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    data_page.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(False, False)

    my_menubar = Menu(root)
    data_page.config(menu=my_menubar)

    file_menu = Menu(my_menubar)
    my_menubar.add_cascade(
        label="Home",
        menu=file_menu
    )

    my_menubar.add_cascade(
        label="About",
        menu=file_menu
    )

    data_page.title('Info calculator')
    back = Button(
        data_page,
        text="Back",
        command=go_back
    )
    back.pack()


# NAVIGATING TO THE NEXT WINDOW
def go_back():
    data_page.withdraw()
    root.deiconify()


# SEARCH BUTTON
Search = Button(
    root,
    text="Search",
    font=("Arial ", 15),
    background='green',
    command=next,
    width=20,height=2,foreground='white'
)

Search.place(x=140, y=250)


root.mainloop()