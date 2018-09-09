from tkinter import *

class ScaperGUI:
    def __init__(self, master):
        self.master = master
        master.title("Amazon Price Webscraper")

        root.geometry("700x200")
        root.resizable(False, False)

        self.frame = Frame(root)
        self.frame.pack( side = BOTTOM, pady = (0, 80) )

        self.label = Label(master, text="Enter the web address of an item to track")
        self.label.pack(pady = (25,0))

        self.input = Entry(master)
        self.input.pack()
        self.input.config(width = 80)

        self.print_button = Button(self.frame, text="Print Input", command=self.print_input)
        self.print_button.pack( side = LEFT, padx = (0, 10))

        self.close_button = Button(self.frame, text="Close", command=master.quit)
        self.close_button.pack( side = LEFT )

    def print_input(self):
        print(self.input.get())

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
