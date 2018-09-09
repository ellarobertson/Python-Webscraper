from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Amazon Price Webscraper")

        self.frame = Frame(root)
        self.frame.pack( side = BOTTOM )

        self.label = Label(master, text="Enter the web address of an item to track")
        self.label.pack()

        self.input = Entry(master)
        self.input.pack()

        self.print_button = Button(self.frame, text="Print Input", command=self.print_input)
        self.print_button.pack( side = LEFT)

        self.close_button = Button(self.frame, text="Close", command=master.quit)
        self.close_button.pack( side = LEFT )

    def print_input(self):
        print(self.input.get())

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
