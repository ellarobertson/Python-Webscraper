from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Amazon Price Webscraper-6da255beb776.json'

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'price-webscraper',
})

db = firestore.client()

class ScaperGUI:
    def __init__(self, master):
        self.print_all_links()
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
        user_link = self.input.get()
        db.collection(u'links').add({
            u'link': user_link
        })
    def print_all_links(self):
        docs = db.collection(u'links').get()
        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
