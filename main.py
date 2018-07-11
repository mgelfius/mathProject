import tkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.resize = tkinter.Button(self)
        self.resize["text"] = "This window is so tiny pls click to make it usable"
        self.resize["command"] = self.resizeToUsableSize
        self.resize.pack(side="left")

        self.quit = tkinter.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def resizeToUsableSize(self):
        root.geometry("500x500")
        self.resize["text"] = "Alright you can make it small again if you want"
        self.resize["command"] = self.makeItSmall

    def makeItSmall(self):
        root.geometry("300x90")
        self.resize["text"] = "This window is so tiny pls click to make it usable"
        self.resize["command"] = self.resizeToUsableSize

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()