import tkinter.ttk as ttk
import tkinter as tk

loginWindow = tk.Tk()
mainWindow = tk.Tk()

loginWindow.resizable(False,False)
mainWindow.resizable(False,False)
loginWindow.title('Login')
mainWindow.title('Task List')
loginWindow.attributes('-topmost',True)

screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

mainWindow.geometry('%dx%d+%d+%d' % (600,800,screenWidth/2,50))
loginWindow.geometry('%dx%d+%d+%d' % (250,150,screenWidth/2+175,375))

# Login Window Elements
frmLogin = ttk.Frame(master=loginWindow,width=250,height=150,border=10)
frmLogin.pack_propagate(False)

lblLoginHeader = ttk.Label(master=frmLogin,text="Please Login",font=('Arial',15)).pack(pady=30)
lblPassEnter = ttk.Label(master=frmLogin,text="Password:").pack(side=tk.LEFT)
entryPassword = ttk.Entry(master=frmLogin,show='*').pack(side=tk.LEFT)

frmLogin.pack()

# Main Window Elements
frmMain = ttk.Frame(master=mainWindow,width=600,height=800)
frmMain.pack_propagate(False)

lblHeader = ttk.Label(master=frmMain, text="Hello, Aaron.",font=('Arial',25)).pack(anchor=tk.NW)
separator = tk.Frame(master=frmMain,background='Black',height=1,bd=0).pack(fill='x')

frmMain.pack(padx=50,pady=50)

mainWindow.mainloop()