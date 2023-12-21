


from tkinter import *       
def login_form():            
    global login_window      
    login_window = Tk()      
    login_window.title ("Login Form")      
    login_window.geometry('400x300')       
    Label(login_window,text='Please Enter username and passowrd below').pack()
    Label(login_window,text='Enter Username').pack()    
    Entry(login_window).pack()
    Label(login_window,text='Enter Password').pack()
    Entry(login_window,show='*').pack()
    Button(login_window,text='Login').pack()
    login_window.mainloop()     
login_form()    
