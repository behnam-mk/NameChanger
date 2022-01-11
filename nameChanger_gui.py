#!/usr/bin/python3

from tkinter import *
import os
from tkinter import messagebox

def browse_cmd():
    from tkinter import filedialog
    list_box.delete(0,END)
    lastmessage["text"] = " "
    label2["text"] = " "
    myPath = filedialog.askdirectory(parent=root, title='Choose your active directory')
    entryText.set(myPath)

    list = os.listdir(myPath) 
    number_files = len(list)
    myString = "You have <" + str(number_files) + "> file(s) and folder(s) in your active directory."
    files_count.set( myString )
    label2['borderwidth'] = 1
    label2['highlightthickness'] = 0
    label2['relief'] = "ridge"
    label2['bg'] = "#05445e"



def about_us():
    top = Toplevel()
    top.geometry("400x175")
    Tk_Width = 400
    Tk_Height = 175

    #calculate coordination of screen and window form
    x_Left = int(root.winfo_screenwidth()/2 - Tk_Width/2)
    y_Top = int(root.winfo_screenheight()/2 - Tk_Height/2)
    
    # Write following format for center screen
    top.geometry("+{}+{}".format(x_Left, y_Top))

    top.resizable(width = False, height = False)
    top.title("About us ...")

    main_frame = Frame(top, bg = "#050a30")
    main_frame.pack()
    about_lbl0 = Label(main_frame, text = "This is an useful App for rename entire files and folders exist inside a directory with your specific format that is imposible with Windows Explorer.", justify = CENTER, wraplength=Tk_Width-15, fg="#75e6da", bg = "#050a30")
    about_lbl0.pack(padx = 10, pady = 15)
    about_lbl2 = Label(main_frame, text = "This Program is designed by Behnam.M.K", justify = CENTER, wraplength=Tk_Width-15, font = "arial 13 bold", fg="#75e6da", bg = "#050a30")
    about_lbl2.pack(padx = 10, pady = 5)
    about_lbl1 = Label(main_frame, text = "License: GPL v3.0", justify = CENTER, font="arial 8 bold", fg="#75e6da", bg = "#050a30")
    about_lbl1.pack(padx = 10, pady = 2)
    about_lbl3 = Label(main_frame, text = "Tnx to Python ❤ ", justify = CENTER, font="arial 9", fg="white", bg = "#050a30")
    about_lbl3.pack(padx = 10, pady = 14)
    
    top.mainloop() 

def rename_cmd():
    list_box.delete(0,END)
    myPath = active_dir.get()
    index = index_entry.get()
    answer = postfix_entry.get()
    for count, filename in enumerate(os.listdir(myPath)):
        myPath = myPath + "/"
  
        src = myPath + filename
  
        fileExtension = " "
  
        if os.path.isfile(src):
            fileExtension = filename[filename.rfind('.'):]
            filename = filename[:filename.rfind('.')]

        dst = str(index) + "_" + filename + answer + fileExtension
        dst2 = myPath + dst
  
        os.rename(src, dst2)

        index = int(index) + 1
        myStr = "( " + str(count+1) + " ) : " + dst
        list_box.insert(END,myStr)

    lastmessage["text"] = "All Done!"
    lastmessage["font"] = "arial 14 bold"
    lastmessage["fg"] = "#1dc690"

root = Tk()

root.geometry("600x450")
Tk_Width = 600
Tk_Height = 450

#calculate coordination of screen and window form
x_Left = int(root.winfo_screenwidth()/2 - Tk_Width/2)
y_Top = int(root.winfo_screenheight()/2 - Tk_Height/2)
 
# Write following format for center screen
root.geometry("+{}+{}".format(x_Left, y_Top))

root.resizable(width = True, height = False)
root.title("NameChanger mini App")

# create a toplevel menu
menubar = Menu(root, fg="white", bg = "#050a30", relief='solid')

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0, fg="white", bg = "#050a30", relief='solid')
filemenu.add_command(label="Open", command=browse_cmd)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0, fg="white", bg = "#050a30", relief='solid')
helpmenu.add_command(label="About", command=about_us)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu = menubar)


above_frame = Frame(root, bg="#274472")
above_frame.pack( side = TOP )

Label(above_frame,text="Select your active directory:", fg = "#c3e0e5", bg="#274472").pack(side=LEFT,padx=5,pady=10)

entryText = StringVar()
active_dir = Entry(above_frame, width = 40, textvariable=entryText, bg="#b1d4e0", bd=0, highlightthickness=0, relief='ridge')
active_dir.pack(side=LEFT,padx=5,pady=13)
#img = PhotoImage(file="./rsz_br.png")
btn_browse = Button(above_frame, text = "Browse", comman = browse_cmd, fg="#75e6da", bg = "#050a30", relief='solid')
#btn_browse.config(image=img)
btn_browse.pack(side=LEFT,padx=5,pady=10)

middle_frame = Frame(root, bg="#274472", pady=5)
middle_frame.pack(side = TOP)

files_count = StringVar()
label2 = Label(middle_frame,textvariable = files_count, font = "arial 13 bold", bg="#274472", fg="#75e6da", borderwidth=0, relief="flat", padx=8, pady=8)
label2.pack()

canvas_win = Canvas(middle_frame, width=600, height=43, bg="#274472", bd=0, highlightthickness=0, relief='ridge')
canvas_win.create_line(0,30,600,30, fill="#c3e0e5")
canvas_win.pack()

box_frame = Frame(middle_frame, bg="#274472")
box_frame.pack(pady = 5)

Label(box_frame, text="Index starts from: ", fg = "#c3e0e5", bg="#274472").pack(side=LEFT)
indexvariable = StringVar()
postfixvariable = StringVar()
index_entry = Entry(box_frame, width = 10, textvariable=indexvariable, bg="#b1d4e0", bd=0, highlightthickness=0, relief='ridge')
index_entry.pack(side=LEFT)
Label(box_frame, text="    ", bg="#274472").pack(side=LEFT)
Label(box_frame, text="Postfix to add to files name: ", fg = "#c3e0e5", bg="#274472").pack(side=LEFT, pady=1)
postfix_entry = Entry(box_frame, width = 20, textvariable=postfixvariable, bg="#b1d4e0", bd=0, highlightthickness=0, relief='ridge')
postfix_entry.pack(side=LEFT)

renam_btn = Button(middle_frame,text = "Rename All!", font="arial 12 bold", comman = rename_cmd, fg="#75e6da", bg = "#050a30", relief='solid').pack(pady = 10)

canvas_win2 = Canvas(middle_frame, width=600, height=25, bg="#274472", bd=0, highlightthickness=0, relief='ridge')
canvas_win2.create_line(0,15,600,15, fill="#c3e0e5")
canvas_win2.pack()

bottom_frame = Frame(root, bg="#274472")
bottom_frame.pack( side = TOP )

lastmessage = Label(bottom_frame,text=" ", bg="#274472", font = "arial 9", fg="#1dc690")
lastmessage.pack(side=TOP)

scrollbar = Scrollbar(bottom_frame)
scrollbar.pack( side = RIGHT ,fill = BOTH ,pady = 17)

list_box = Listbox(bottom_frame, yscrollcommand = scrollbar.set, width=100, bg = "#050a30", fg="#c3e0e5", bd=0, highlightthickness=0, relief='ridge')
list_box.pack(pady = 17)

root.mainloop()
