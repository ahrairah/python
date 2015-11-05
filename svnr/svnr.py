from tkinter import *


class Application():
    def __init__(self, master=None):
        Tk.frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = Tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = Tk.Tk()
app = Application(master=root)
app.mainloop()
