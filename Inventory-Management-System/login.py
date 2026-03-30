from dashboard import IMS   
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from module_selector import ModuleSelector
import sqlite3

class loginClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        self.root.focus_force()

        # ----------- variables -----------
        self.var_email = StringVar()
        self.var_password = StringVar()

        # ----------- title -----------
        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="#010c48", fg="white").place(x=0, y=0, relwidth=1, height=70)

        # ----------- login frame -----------
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=400, y=150, width=500, height=350)

        title_login = Label(login_frame, text="Login Here", font=("times new roman", 30, "bold"), bg="white").place(x=0, y=20, relwidth=1)

        label_email = Label(login_frame, text="Email Address", font=("times new roman", 15), bg="white").place(x=50, y=100)
        txt_email = Entry(login_frame, textvariable=self.var_email, font=("times new roman", 15), bg="lightyellow").place(x=50, y=130, width=350)

        label_password = Label(login_frame, text="Password", font=("times new roman", 15), bg="white").place(x=50, y=170)
        txt_password = Entry(login_frame, textvariable=self.var_password, show='*', font=("times new roman", 15), bg="lightyellow").place(x=50, y=200, width=350)

        button_login = Button(login_frame, text="Login", command=self.login_function, font=("times new roman", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=50, y=250, width=350)
        
        # ----------- functions -----------
    def login_function(self):
        if self.var_email.get() == "" or self.var_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            cursor, conn = self.connect_database()
            cursor.execute("SELECT * FROM employee WHERE email=? AND pass=?", (self.var_email.get(), self.var_password.get()))
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
            else:
                messagebox.showinfo("Success", "Welcome to Inventory Management System", parent=self.root)
                self.root.destroy()
                conn.close()
                self.user_role = row[8]  
                
            root = Tk()
            ModuleSelector(root, self.user_role)
            root.mainloop()
            
    
    def clear(self):
        self.var_email.set("")
        self.var_password.set("")

    def connect_database(self):
        try:
            self.conn = sqlite3.connect("ims.db")
            self.cursor = self.conn.cursor()
            return self.cursor, self.conn
        except Exception as ex:
            messagebox.showerror("Error", f"Error connecting to database: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = loginClass(root)
    root.mainloop()

        