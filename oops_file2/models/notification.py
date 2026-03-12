class Notification:

    def __init__(self, message):
        self.message = message

    def send(self):
        print("Sending notification:", self.message)  
                                                                                      