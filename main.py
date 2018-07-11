import tkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #root.geometry("800x150")
        self.winfo_toplevel().title("Math Program")
        self.pack()
        self.create_widgets()
        self.calcFrame = tkinter.Frame()
        self.calcFrame.pack()

    def create_widgets(self):
        headerFrame = tkinter.Frame()
        headerFrame.pack()
        expButton = tkinter.Button(headerFrame, text="Calculate Exponent", command=self.build_exp)
        fibButton = tkinter.Button(headerFrame, text="Calculate Fib Number", command=self.build_fib)
        expButton.grid(row=0)
        fibButton.grid(row=0, column=1)

    def build_exp(self):
        for widget in self.calcFrame.winfo_children():
            widget.destroy()
        L1 = tkinter.Label(self.calcFrame, text = "Base number")
        self.baseNum = tkinter.Entry(self.calcFrame, width="10")
        L2 = tkinter.Label(self.calcFrame, text = "Exponent")
        self.expNum = tkinter.Entry(self.calcFrame, width="10")
        calcExp = tkinter.Button(self.calcFrame, text="Exponentiate", command=self.calculateExpMethod)
        self.product = tkinter.Label(self.calcFrame)
        L1.grid(row=1)
        self.baseNum.grid(row=1, column=1)
        L2.grid(row=2)
        self.expNum.grid(row=2, column=1)
        calcExp.grid(row=3)
        self.product.grid(row=4)

    def build_fib(self):
        for widget in self.calcFrame.winfo_children():
            widget.destroy()
        L1 = tkinter.Label(self.calcFrame, text="Index of Fibonacci")
        self.fibNum = tkinter.Entry(self.calcFrame, width="10")
        calcFib = tkinter.Button(self.calcFrame, text="Find Fibonacci", command=self.calculateFib)
        self.final = tkinter.Label(self.calcFrame)
        L1.grid(row=1)
        self.fibNum.grid(row=1, column=1)
        calcFib.grid(row=2)
        self.final.grid(row=3)

    def calculateExpMethod(self):
        self.product["text"] = "Answer: " + str((int(self.baseNum.get())**int(self.expNum.get())))

    def calculateFib(self):
        n = int(self.fibNum.get())
        answer = self.fib(n)
        self.final["text"] = "Answer: " + str(answer)

    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            return self.fib(n - 2) + self.fib(n - 1)


root = tkinter.Tk()
app = Application(master=root)
app.mainloop()