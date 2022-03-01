import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get(TWILIO_SID)
TWILIO_AUTH_TOKEN = os.environ.get(TWILIO_TOKEN)
FROM_NUM = os.environ.get(TWILIO_NUM)
TO_NUM = os.environ.get(MY_NUM)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    #Create a client object for twilio when initializing the class in main.py
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages.create(
                body=message,
                from_=FROM_NUM,
                to=TO_NUM
            )
        print(message.sid)
