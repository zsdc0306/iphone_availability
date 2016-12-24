from Tkinter import *
def showMessage(msgtype):
    text = ""
    if msgtype == MSG_ERROR:
        text = "Error in getting data, Check"
    elif msgtype == MSG_PICK:
        text = "Iphone 7 is available, Check Now"
    # show reminder message window
    root = Tk()
    # root.minsize(500, 200)
    # root.maxsize(1000, 400)
    root.withdraw()  # hide window
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight() - 100
    root.resizable(False, False)
    root.title("Warnging!!")
    frame = Frame(root, relief=RIDGE, borderwidth=3)
    frame.pack(fill=BOTH, expand=1)
    label = Label(frame, text=text,
                  font="Monotype\ Corsiva -20 bold")
    label.pack(fill=BOTH, expand=1)
    button = Button(frame, text="OK", font="Cooper -25 bold", fg="red", command=root.destroy)
    button.pack(side=BOTTOM)

    root.update_idletasks()
    root.deiconify()  # now the window size was calculated
    root.withdraw()
    root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10,
                                   (screenwidth - root.winfo_width()) / 2, (screenheight - root.winfo_height()) / 2))
    root.deiconify()
    root.mainloop()