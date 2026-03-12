from services.notification_service import NotificationService
from utils.logger import log

service = NotificationService()

log("Starting notification system")

service.send_email("Welcome to the platform")
service.send_sms("Your OTP is 1234")