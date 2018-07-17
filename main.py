import tkinter
import math
from decimal import Decimal

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.winfo_toplevel().title("Math Program")
        root.resizable(0, 0)
        self.pack()
        self.headerFrame = tkinter.Frame()
        self.headerFrame.pack()
        self.create_widgets()
        self.calcFrame = tkinter.Frame()
        self.calcFrame.pack()
        self.answerFrame = tkinter.Frame()
        self.answerFrame.pack()
        self.build_exp()

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def create_widgets(self):
        expButton = tkinter.Button(self.headerFrame, text="Calculate Exponent", command=self.build_exp)
        fibButton = tkinter.Button(self.headerFrame, text="Calculate Fib Number", command=self.build_fib)
        angButton = tkinter.Button(self.headerFrame, text="Calculate Angle", command=self.build_ang)
        fracButton = tkinter.Button(self.headerFrame, text="Fraction Reducer", command=self.build_frac)
        expButton.grid(row=0)
        fibButton.grid(row=0, column=1)
        angButton.grid(row=0, column=2)
        fracButton.grid(row=0, column=3)

    def build_exp(self):
        self.clearFrame(self.calcFrame)
        self.clearFrame(self.answerFrame)
        L1 = tkinter.Label(self.calcFrame, text = "Base number")
        self.baseNum = tkinter.Entry(self.calcFrame, width="10")
        L2 = tkinter.Label(self.calcFrame, text = "Exponent")
        self.expNum = tkinter.Entry(self.calcFrame, width="10")
        calcExp = tkinter.Button(self.calcFrame, text="Exponentiate", command=self.calculateExpMethod)
        self.product = tkinter.Label(self.answerFrame, wraplength=300, justify="left")
        L1.grid(row=1)
        self.baseNum.grid(row=1, column=1)
        L2.grid(row=2)
        self.expNum.grid(row=2, column=1)
        calcExp.grid(row=3)
        self.product.grid(row=4)

    def build_fib(self):
        self.clearFrame(self.calcFrame)
        self.clearFrame(self.answerFrame)
        L1 = tkinter.Label(self.calcFrame, text="Index of Fibonacci")
        self.fibNum = tkinter.Entry(self.calcFrame, width="10")
        calcFib = tkinter.Button(self.calcFrame, text="Find Fibonacci", command=self.calculateFib)
        self.final = tkinter.Label(self.answerFrame, wraplength=300, justify="left")
        L1.grid(row=1)
        self.fibNum.grid(row=1, column=1)
        calcFib.grid(row=2)
        self.final.grid(row=3)

    def build_ang(self):
        self.clearFrame(self.calcFrame)
        self.clearFrame(self.answerFrame)
        self.v = tkinter.IntVar()
        self.r = tkinter.IntVar()
        self.degRadio = tkinter.Radiobutton(self.calcFrame, text="Degrees", value=1, width=10, variable=self.r)
        self.radRadio = tkinter.Radiobutton(self.calcFrame, text="Radians", value=2, width=10, variable=self.r)
        L1 = tkinter.Label(self.calcFrame, text="Angle")
        self.angNum = tkinter.Entry(self.calcFrame, width="5")
        self.sinRadio = tkinter.Radiobutton(self.calcFrame, text="Sin", value=1, width=10, variable=self.v)
        self.cosRadio = tkinter.Radiobutton(self.calcFrame, text="Cos", value=2, width=10, variable=self.v)
        self.tanRadio = tkinter.Radiobutton(self.calcFrame, text="Tan", value=3, width=10, variable=self.v)
        self.v.set(1)
        self.r.set(1)
        calcAngle = tkinter.Button(self.calcFrame, text="Calculate", command=self.calculateAng)
        self.answer = tkinter.Label(self.answerFrame, wraplength=300, justify="left")
        L1.grid(row = 1)
        self.angNum.grid(row=1, column=1)
        self.degRadio.grid(row=2, column=0)
        self.radRadio.grid(row=2, column=1)
        self.sinRadio.grid(row=3, column=0)
        self.cosRadio.grid(row=3, column=1)
        self.tanRadio.grid(row=3, column=2)
        calcAngle.grid(row=4)
        self.answer.grid(row=5)

    def build_frac(self):
        self.clearFrame(self.calcFrame)
        self.clearFrame(self.answerFrame)
        L1 = tkinter.Label(self.calcFrame, text="Numerator")
        L2 = tkinter.Label(self.calcFrame, text="Denominator")
        self.numerator = tkinter.Entry(self.calcFrame, width=5)
        self.denominator = tkinter.Entry(self.calcFrame, width=5)
        calcReduce = tkinter.Button(self.calcFrame, text="Reduce", command=self.calculateReduce)
        self.reduceFinal = tkinter.Label(self.answerFrame, wraplength=300, justify="left")
        L1.grid(row=1)
        self.numerator.grid(row=1, column=1)
        L2.grid(row=2)
        self.denominator.grid(row=2, column=1)
        calcReduce.grid(row=3)
        self.reduceFinal.grid(row=4)

    def calculateExpMethod(self):
        self.product["text"] = "Answer: " + str("{:,}".format((int(self.baseNum.get())**int(self.expNum.get()))))

    def calculateFib(self):
        n = int(self.fibNum.get())
        answer = self.fib(n)
        self.final["text"] = "Answer: " + str("{:,}".format(answer))

    def calculateAng(self):
        degOrRad = " radians"
        passMath = self.readMath(self.angNum.get())
        if(self.r.get() == 1):
            passMath = math.radians(passMath)
            degOrRad = " degrees"
        if self.v.get() == 1:
            final = Decimal(math.sin(passMath)).quantize(Decimal('1e-4'))
            self.answer["text"] = "Sine of " + self.angNum.get() + degOrRad + ": " + str(final)
        if self.v.get() == 2:
            final = Decimal(math.cos(passMath)).quantize(Decimal('1e-4'))
            self.answer["text"] = "Cosine of " + self.angNum.get() + degOrRad + ": " + str(final)
        if self.v.get() == 3:
            final = Decimal(math.tan(passMath)).quantize(Decimal('1e-4'))
            self.answer["text"] = "Tangent of " + self.angNum.get() + degOrRad + ": " + str(final)
        

    def fib(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            return self.fib(n - 2) + self.fib(n - 1)

    def readMath(self, passMath):
        passMath = passMath.lower()
        for r in (('pi', 'math.pi'), ('^', '**'), ('sqrt', 'math.sqrt'), ('e', 'math.e')):
            passMath = passMath.replace(*r)
        return  eval(passMath)

    def calculateReduce(self):
        num = int(self.numerator.get())
        denom = int(self.denominator.get())
        for i in range(2, denom+1):
            while num%i == 0 and denom%i == 0:
                num = num/i
                denom = denom/i
        num = round(num)
        denom = round(denom)
        self.reduceFinal["text"] = "Reduced: " + str("{:,}".format(num)) + '/' + str("{:,}".format(denom))

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()