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
    frmHeader = ttk.Frame(master=mainWindow,width=600,height=100)
    frmMain = ttk.Frame(master=mainWindow,width=600,height=400)
    frmHeader.pack_propagate(False)

    lblHeader = ttk.Label(master=frmHeader, text="\nHello, Aaron.",font=('Arial',25))
    lblHeader.pack(anchor=tk.NW)
    separator = tk.Frame(master=frmHeader,background='Black',height=1,bd=0)
    separator.pack(fill='x')

    for i in range(5):
        for j in range(3):
            entryTemp = ttk.Entry(master=frmMain)
            entryTemp.insert(tk.END,"test")
            entryTemp.grid(row=i,column=j,sticky='ew')

    frmHeader.pack(padx=50)
    frmMain.pack(padx=50,anchor=tk.NW)

    mainWindow.mainloop()

loginScreen()