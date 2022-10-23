from tkinter.font import BOLD
import tkinter.ttk as ttk
import tkinter as tk
import encryption

def loginScreen():

    def checkPassword(en=None):
        passTxt = entryPassword.get()
        if(encryption.passwordAuthenticate(passTxt)):
            # Destroy login window
            loginWindow.destroy()
            # Load Main window, sending password
            mainScreen(passTxt)
        else:
            print("invalid")
            lblLoginHeader["text"] = "Invalid Password"
            entryPassword.delete(0,tk.END)

    loginWindow = tk.Tk()
    loginWindow.resizable(False,False)
    loginWindow.title('Login')
    loginWindow.wm_iconbitmap('logo.ico')
    loginWindow.attributes('-topmost',True)
    screenWidth = loginWindow.winfo_screenwidth()
    screenHeight = loginWindow.winfo_screenheight()
    loginWindow.geometry('%dx%d+%d+%d' % (250,150,screenWidth/2-125,screenHeight/2-75))

    # Login Window Elements
    frmLogin = ttk.Frame(master=loginWindow,width=250,height=150,border=10)
    frmLogin.pack_propagate(False)

    lblLoginHeader = ttk.Label(master=frmLogin,text="Please Login",font=('Arial',15))
    lblLoginHeader.pack(pady=30)
    
    lblPassEnter = ttk.Label(master=frmLogin,text="Password:")
    lblPassEnter.pack(side=tk.LEFT)

    entryPassword = ttk.Entry(master=frmLogin,show='*')
    entryPassword.pack(side=tk.LEFT)
    entryPassword.focus()

    btnSubmit = ttk.Button(master=frmLogin,text="->",command=checkPassword)
    btnSubmit.pack(side=tk.LEFT)

    loginWindow.bind('<Return>',checkPassword)
    frmLogin.pack()
    loginWindow.mainloop()

def mainScreen(password):
    mainWindow = tk.Tk()

    windowWidth = 600
    windowHeight = 400

    mainWindow.resizable(False,True)
    mainWindow.title('Task List')
    mainWindow.wm_iconbitmap('logo.ico')
    screenWidth = mainWindow.winfo_screenwidth()
    screenHeight = mainWindow.winfo_screenheight()
    mainWindow.geometry('%dx%d+%d+%d' % (windowWidth,windowHeight,screenWidth-windowWidth-15,screenHeight-windowHeight-80))

    # Main Window Elements
    frmHeader = ttk.Frame(master=mainWindow,width=600,height=90)
    frmMain = ttk.Frame(master=mainWindow,width=600,height=400)
    frmHeader.pack_propagate(False)

    editImage = tk.PhotoImage(file="editImage.png",)
    editImage = editImage.subsample(3,3)

    lblHeader = ttk.Label(master=frmHeader, text="\nHello, Aaron.",font=('Arial',25))
    lblHeader.pack(anchor=tk.NW)
    separator = tk.Frame(master=frmHeader,background='Black',height=1,bd=0)
    separator.pack(fill='x')

    frmMain.columnconfigure(1,minsize=285)
    frmMain.columnconfigure(2,minsize=120)
    frmMain.columnconfigure(3,minsize=50)

    lblTaskName = ttk.Label(master=frmMain,text="Task",font=('Arial',10,'bold'))
    lblTaskName.grid(row=1,column=1,sticky='ew')

    lblTaskStatus = ttk.Label(master=frmMain,text="Status",font=('Arial',10,'bold'))
    lblTaskStatus.grid(row=1,column=2,sticky='ew')

    lblTaskEdit = ttk.Label(master=frmMain,text="Edit",font=('Arial',10,'bold'))
    lblTaskEdit.grid(row=1,column=3,sticky='ew')

    lblTaskDelete = ttk.Label(master=frmMain,text="Delete",font=('Arial',10,'bold'))
    lblTaskDelete.grid(row=1,column=4,sticky='ew')

    for _row in range(2,5,2):
        for col in range(1,3):
            lblContent = tk.Label(master=frmMain,text="content",height=2,borderwidth=1,relief=tk.GROOVE)
            lblContent.grid(row=_row,column=col,sticky='ew')
        
        btnEdit = ttk.Button(master=frmMain,text="edit",image=editImage,)
        btnEdit.grid(row=_row,column=3,sticky='ew')

    scrollbar = ttk.Scrollbar(master=mainWindow,orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

    frmHeader.pack(padx=50)
    frmMain.pack(padx=50,anchor=tk.NW)

    mainWindow.mainloop()

loginScreen()