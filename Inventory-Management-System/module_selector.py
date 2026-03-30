# module_selector.py
from tkinter import *
from tkinter import messagebox

class ModuleSelector:
    def __init__(self, root, user_role):
        self.root = root
        self.user_role = user_role

        # ---------------- main window ----------------
        self.root.title("Select Module")
        self.root.geometry("1350x700+0+0") 
        self.root.config(bg="#fafafa")     
        self.root.focus_force()

        # ---------------- title ----------------
        title = Label(
            self.root,
            text="Select Module",
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=70)

        # ---------------- central frame ----------------
        frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        frame.place(x=400, y=150, width=500, height=350)

        title_label = Label(frame, text="Choose Module", font=("times new roman", 30, "bold"), bg="white")
        title_label.place(x=0, y=20, relwidth=1)

        # ---------------- buttons  ----------------
        btn_inventory = Button(
            frame, text="Inventory System",
            font=("times new roman", 15, "bold"),
            bg="#4caf50", fg="white",
            cursor="hand2",
            command=self.open_ims
        )
        btn_inventory.place(x=50, y=100, width=400, height=50)

        btn_billing = Button(
            frame, text="Billing System",
            font=("times new roman", 15, "bold"),
            bg="#2196f3", fg="white",
            cursor="hand2",
            command=self.open_billing
        )
        btn_billing.place(x=50, y=170, width=400, height=50)



    # ---------------- actions ----------------
    def open_ims(self):
        self.root.destroy()
        from dashboard import IMS
        root = Tk()
        IMS(root, self.user_role)
        root.mainloop()

    def open_billing(self):
        self.root.destroy()
        from billing import billClass
        root = Tk()
        billClass(root)
        root.mainloop()

