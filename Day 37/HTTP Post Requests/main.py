import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv()

pixela_token = os.getenv("DAY37_PIXELA_TOKEN")
pixela_username = os.getenv("DAY37_PIXELA_USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

""" response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text) """ # Created a pixela account

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Read Pages",
    "unit": "page",
    "type": "int",
    "color": "ajisai",
    "timezone": "Asia/Istanbul"
}

headers = {
    "X-USER-TOKEN": pixela_token
}

""" response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text) """ # Create a graph

post_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()
date = today.strftime("%Y%m%d")

page = input("How many pages did you read today? : ")

with open("last_optional_data.json", "r") as file:
    content = json.load(file)

print(f"\nYour last data:\n{content}\n")

optionalData = {
    "Book Number": input("Which number book are you reading? : "),
    "Book Name": input("What is the name of this book? : "),
    "Starting Date": input("When did you started to this book? (dd/mm/yyyy) : "),
    "Finishing Date": input("When did you finished this book? (dd/mm/yyyy) or - : "),
    "Note": input("Do you have a note about today's reading? : ")   
}

with open("last_optional_data.json", "w") as file:
    json.dump(optionalData, file)

print("\nJSON file is updated!\n")

post_config = {
    "date": date,
    "quantity": page,
    "optionalData": json.dumps(optionalData)
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)

""" put_endpoint = f"{post_endpoint}/{date}"

put = {
    "quantity": "32"
}
response = requests.put(url=put_endpoint, json=put, headers=headers)
print(response.text) """
