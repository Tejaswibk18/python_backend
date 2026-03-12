from models.notification import Notification

class SMSNotification(Notification):

    def send(self):
        print("Sending SMS:", self.message)