import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

load_dotenv()

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.smtp_address = os.getenv("DAY40_SMTP")
        self.email = os.getenv("DAY40_EMAIL")
        self.email_password = os.getenv("DAY40_APP_PASSWORD")
        self.twilio_virtual_number = os.getenv("DAY40_TWILIO_VIRTUAL_NUMBER")
        self.twilio_verified_number = os.getenv("DAY40_TWILIO_VERIFIED_NUMBER")
        self.whatsapp_number = os.getenv("DAY40_TWILIO_WHATSAPP_NUMBER")

        self.client = Client(
            os.getenv("DAY40_TWILIO_ACCOUNT_SID"),
            os.getenv("DAY40_TWILIO_AUTH_TOKEN")
        )
        self.connection = smtplib.SMTP(os.getenv("DAY40_SMTP"))

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.getenv("DAY40_TWILIO_VIRTUAL_NUMBER"),
            body=message_body,
            to=os.getenv("DAY40_TWILIO_VERIFIED_NUMBER")
        )
        print(message.status)
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.getenv("DAY40_TWILIO_WHATSAPP_NUMBER")}',
            body=message_body,
            to=f'whatsapp:{os.getenv("DAY40_TWILIO_VERIFIED_NUMBER")}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )