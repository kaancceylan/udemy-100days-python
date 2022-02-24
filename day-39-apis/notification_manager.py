from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'ACc96f2e19587a4fc3c3717681bba7d92c'
TWILIO_AUTH_TOKEN = 'd45b585cc43e1e2f3f28c9648e096c16'
TWILIO_NUMBER = '++19125518501'

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    #Create a client object for twilio when initializing the class in main.py
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages \
            .create(
                body=message,
                from_=TWILIO_NUMBER,
                to='+905306688124'
            )