from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import sqlite3
import os

from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass

# ------------------ BASE PATH SETUP ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
BILL_DIR = os.path.join(BASE_DIR, "bill")

os.makedirs(BILL_DIR, exist_ok=True)
# ---------------------------------------------------

class IMS:
    def __init__(self, root, user_role):
        self.root = root
        self.user_role = user_role
        self.root.geometry("1350x700+110+80")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # ------------- title --------------
        self.title(self.root)
        # ------------ logout button -----------
        self.logout_button(self.root)
        # ------------ clock -----------------
        self.clock(self.root)
        # ---------------- left menu ---------------
        self.left_menu(self.root)
        # ----------- content ----------------
        self.content(self.root)
        # ------------ footer -----------------
        self.footer(self.root)
    
    # --------- appearance functions -----------

    def title(self, root):
        self.icon_title = PhotoImage(file=os.path.join(IMAGE_DIR, "logo1.png"))
        title_label = Label(
            self.root,
            text="Inventory Management System",
            image=self.icon_title,
            compound=LEFT,
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white",
            anchor="w",
            padx=20
        ).place(x=0, y=0, relwidth=1, height=70)

    def logout_button(self, root):
        button_logout = Button(
            self.root, text="Logout",
            font=("times new roman", 15, "bold"),
            bg="yellow", cursor="hand2", command=self.logout
        ).place(x=1150, y=10, height=50, width=150)

    def clock(self, root):
        self.label_clock = Label(
            self.root,
            text="Welcome to Inventory Management System\t\t Date: DD:MM:YYYY\t\t Time: HH:MM:SS",
            font=("times new roman", 15),
            bg="#4d636d", fg="white"
        )
        self.label_clock.place(x=0, y=70, relwidth=1, height=30)

    def left_menu(self, root):
        self.menu_logo = Image.open(os.path.join(IMAGE_DIR, "menu_im.png"))
        self.menu_logo = self.menu_logo.resize((200, 200))
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        left_menu_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        left_menu_frame.place(x=0, y=102, width=200, height=565)

        label_menu_logo = Label(left_menu_frame, image=self.menu_logo)
        label_menu_logo.pack(side=TOP, fill=X)

        label_menu = Label(
            left_menu_frame, text="Menu",
            font=("times new roman", 20),
            bg="#009688"
        ).pack(side=TOP, fill=X)

        self.icon_side = PhotoImage(file=os.path.join(IMAGE_DIR, "side.png"))

        button_employee = Button(
            left_menu_frame, text="Employee", command=self.employee,
            image=self.icon_side, compound=LEFT,
            padx=5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd=3, cursor="hand2"
        ).pack(side=TOP, fill=X)

        button_supplier = Button(
            left_menu_frame, text="Supplier", command=self.supplier,
            image=self.icon_side, compound=LEFT,
            padx=5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd=3, cursor="hand2"
        ).pack(side=TOP, fill=X)

        button_category = Button(
            left_menu_frame, text="Category", command=self.category,
            image=self.icon_side, compound=LEFT,
            padx=5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd=3, cursor="hand2"
        ).pack(side=TOP, fill=X)

        button_product = Button(
            left_menu_frame, text="Products", command=self.product,
            image=self.icon_side, compound=LEFT,
            padx=5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd=3, cursor="hand2"
        ).pack(side=TOP, fill=X)

        button_sales = Button(
            left_menu_frame, text="Sales", command=self.sales,
            image=self.icon_side, compound=LEFT,
            padx=5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd=3, cursor="hand2"
        ).pack(side=TOP, fill=X)

        button_exit = Button(
            left_menu_frame, text="Exit",
            image=self.icon_side, compound=LEFT,
            padx=5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd=3, cursor="hand2",
            command=self.root.destroy
        ).pack(side=TOP, fill=X)

    def content(self, root):
        self.label_employee = Label(
            self.root, text="Total Employee\n{ 0 }",
            bd=5, relief=RIDGE, bg="#33bbf9",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_employee.place(x=300, y=120, height=150, width=300)

        self.label_supplier = Label(
            self.root, text="Total Supplier\n{ 0 }",
            bd=5, relief=RIDGE, bg="#ff5722",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_supplier.place(x=650, y=120, height=150, width=300)

        self.label_category = Label(
            self.root, text="Total Category\n{ 0 }",
            bd=5, relief=RIDGE, bg="#009688",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_category.place(x=1000, y=120, height=150, width=300)

        self.label_product = Label(
            self.root, text="Total Product\n{ 0 }",
            bd=5, relief=RIDGE, bg="#607d8b",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_product.place(x=300, y=300, height=150, width=300)

        self.label_sales = Label(
            self.root, text="Total Sales\n{ 0 }",
            bd=5, relief=RIDGE, bg="#ffc107",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_sales.place(x=650, y=300, height=150, width=300)

    def footer(self, root):
        label_footer = Label(
            self.root,
            text="IMS-Inventory Management System",
            font=("times new roman", 12),
            bg="#4d636d", fg="white"
        ).pack(side=BOTTOM, fill=X)
        self.update_content()
    
    # -------------- functions ----------------
    def employee(self):
        if self.user_role != "Admin":
            messagebox.showerror("Access Denied", "You do not have permission to access the Employee section.", parent=self.root)
            return
        else:
            self.new_win = Toplevel(self.root)
            self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_content(self):
        cur, con = self.connect_database()

        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.label_product.config(text=f"Total Product\n[ {len(product)} ]")

            cur.execute("select * from category")
            category = cur.fetchall()
            self.label_category.config(text=f"Total Category\n[ {len(category)} ]")

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.label_employee.config(text=f"Total Employee\n[ {len(employee)} ]")

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.label_supplier.config(text=f"Total Supplier\n[ {len(supplier)} ]")

            bill = len(os.listdir(BILL_DIR))
            self.label_sales.config(text=f"Total Sales\n[ {bill} ]")

            time_str = time.strftime("%I:%M:%S")
            date_str = time.strftime("%d-%m-%Y")
            self.label_clock.config(
                text=f"Welcome to Inventory Management System\t\t Date: {date_str}\t\t Time: {time_str}"
            )

            self.label_clock.after(200, self.update_content)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def connect_database(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        return cur, con

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Do you want to logout?", parent=self.root)
        if confirm:
            self.root.destroy()
            from login import loginClass  
            root = Tk()
            loginClass(root)
            root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
