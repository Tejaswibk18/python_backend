from models.email_notification import EmailNotification
from models.sms_notification import SMSNotification

class NotificationService:

    def send_email(self, message):
        email = EmailNotification(message)
        email.send()

    def send_sms(self, message):
        sms = SMSNotification(message)
        sms.send()