import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu  
from tkinter import messagebox as mbox  
err = tk.Tk()  
#Add a Title  
err.title("ERROR ERROR")  
#Label  
ttk.Label(err, text="Error Messsage BoxApp").grid(column=0,row=0,padx=20,pady=30)  
#Create a Menu Bar  
menuBar=Menu(err)  
err.config(menu=menuBar)  
#Display a Error Message Box  
def _msgBox():  
   mbox.showerror('Python Error Message','Error: You are Clicked ErrorMessage')  
   #Create Error Message Menu  
   infoMenu=Menu(menuBar, tearoff=0)  
   infoMenu.add_command(label="Error", command=_msgBox)  
   menuBar.add_cascade(label="Message", menu=infoMenu)  
   #Calling Main()  
   err.mainloop()  