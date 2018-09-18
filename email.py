import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class EmailMsg:

    def __init__(self, oldPrice, newPrice, itemTitle, recipient):
        self.un = "amazonpricetrackerproj@gmail.com"
        self.pw = "******"
        connectToServer()
        sendMessage(self, recipient, oldPrice, newPrice, itemTitle)

    def connectToServer(self):
        server = smtplib.SMTP(‘smtp.gmail.com’, 587)
        server.starttls()

    def sendMessage(self, recipient, oldPrice, newPrice, itemTitle):
        msg = MIMEMultipart()
        msg[‘From’] = self.un
        msg[‘To’] = recipient
        msg[‘Subject’] = 'New Price for ' + itemTitle + '!'
        message = 'Hello, /n the price for' + itemTitle + 'has changed from' + oldPrice +  'to'  + newPrice.
