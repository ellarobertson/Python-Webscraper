from tkinter import *
import requests
from bs4 import BeautifulSoup


'''Everything below here is to connect to the DB'''

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

'''Finished connecting to DB, db variable is our db reference'''

db = firestore.client()

class ScraperGUI:
    def __init__(self, master):

        self.master = master
        master.title("Amazon Price Webscraper")

        root.geometry("700x200")
        root.resizable(False, False)

        self.frame = Frame(root)
        self.frame.pack( side = BOTTOM, pady = (0, 20) )

        self.label = Label(master, text="Enter the web address of an item to track")
        self.label.pack(pady = (25,0))

        self.input = Entry(master)
        self.input.pack()
        self.input.config(width = 80)

        self.print_button = Button(self.frame, text="Print Input", command=self.store_input)
        self.print_button.pack( side = LEFT, padx = (0, 10))

        self.close_button = Button(self.frame, text="Close", command=master.quit)
        self.close_button.pack( side = LEFT )

        self.item_label = Label(master, text= "Title")
        self.item_label.pack(pady = (10,0))

        self.price_label = Label(master, text= "Current Price: (input an item)")
        self.price_label.pack(pady = (10,0))


    def store_input(self):
        user_link = self.input.get()
        self.clear_text()
        db.collection(u'links').add({
            u'link': user_link
        })
        self.get_html(user_link)

    def clear_text(self):
        self.input.delete(0, 'end')

    def print_all_links(self):
        docs = db.collection(u'links').get()
        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))

    def get_html(self, link):
        try:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            price = soup.find_all(id="priceblock_ourprice")[0].string
            title = soup.find_all(id="productTitle")[0].string
            self.item_label['text'] = "Title :)"
            self.price_label['text'] = "Current price: " + price
        except:
            print("That was not a good link! Try again.")


root = Tk()
my_gui = ScraperGUI(root)
root.mainloop()
