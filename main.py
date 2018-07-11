import tkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        root.geometry("800x150")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Math Program")
        self.L1 = tkinter.Label(self, text = "Base number")
        self.baseNum = tkinter.Entry(self, width="10")
        self.L2 = tkinter.Label(self, text = "Exponent")
        self.expNum = tkinter.Entry(self, width="10")
        self.submit = tkinter.Button(self, text="Exponentiate", command=self.submitText)
        self.product = tkinter.Label(self)
        self.L1.grid(row=0)
        self.baseNum.grid(row=0, column=1)
        self.L2.grid(row=1)
        self.expNum.grid(row=1, column=1)
        self.submit.grid(row=2)
        self.product.grid(row=3)

    def submitText(self):
        self.product["text"] = "Answer: " + str((int(self.baseNum.get())**int(self.expNum.get())))


root = tkinter.Tk()
app = Application(master=root)
app.mainloop()