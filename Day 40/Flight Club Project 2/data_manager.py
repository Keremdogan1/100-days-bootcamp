import os
import requests
from dotenv import load_dotenv
import base64
from pprint import pprint
from requests.auth import HTTPBasicAuth

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("DAY40_PRICES_ENDPOINT")


class DataManager:

    def __init__(self):
        self._user = os.getenv("DAY40_SHEETY_USERNAME")
        self._password = os.getenv("DAY40_SHEETY_PASSWORD")
        self.prices_endpoint = os.getenv("DAY40_PRICES_ENDPOINT")
        self.users_endpoint = os.getenv("DAY40_USERS_ENDPOINT")

        self._authorization = HTTPBasicAuth(self._user, self._password)

        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._headers)
        data = response.json()

        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        pprint(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data