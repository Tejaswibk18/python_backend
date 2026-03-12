from models.notification import Notification

class EmailNotification(Notification):

    def send(self):
        print("Sending EMAIL:", self.message)