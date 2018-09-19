import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailMsg:

    def __init__(self, oldPrice, newPrice, itemTitle, recipient):
        self.un = 'amazonpricetrackerproj@gmail.com'
        self.pw = 'Jordan333'
        print('Accessing email mssg class')
        self.sendMessage(recipient, oldPrice, newPrice, itemTitle)

    def sendMessage(self, recipient, oldPrice, newPrice, itemTitle):
        self.server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
        self.server.login(self.un, self.pw)
        msg = MIMEMultipart('alternative')
        msg['From'] = self.un
        msg['To'] = recipient
        msg['Subject'] = 'New Price for ' + str(itemTitle) + '!'
        message = 'Hello,\n\nThe price for ' + str(itemTitle) + ' has changed from $' + str(oldPrice) +  ' to $'  + str(newPrice) + '\n\nThanks,\nAmazon Price Tracker'
        msg.attach(MIMEText(message))
        self.server.sendmail(self.un, recipient, msg.as_string())
        self.server.quit()
