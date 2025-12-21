import os
from dotenv import load_dotenv
import requests
import datetime

load_dotenv()

x_app_id = os.getenv("DAY38-X-APP-ID")
x_app_key = os.getenv("DAY38-X-APP-KEY")
weight = os.getenv("DAY38_WEIGHT")
height = os.getenv("DAY38_HEIGHT")
age = os.getenv("DAY38_AGE")
sheety_token = os.getenv("DAY38_SHEETY_TOKEN")
sheety_endpoint = os.getenv("DAY38_SHEETY_ENDPOINT")

x_app_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

excercises = input("Tell me which excercises you did: ")

user_params = {
    "query": excercises,
    "weight_kg": int(weight),
    "height_cm": float(height),
    "age": int(age),
    "gender": "male"
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": x_app_id,
    "x-app-key": x_app_key
}

response = requests.post(url=x_app_endpoint, json=user_params, headers=headers)
data = response.json()
print(data)

now = datetime.datetime.now()

post_config = {
    "workout": {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": data["exercises"][0]["name"],
        "duration": str(data["exercises"][0]["duration_min"]),
        "calories": data["exercises"][0]["nf_calories"]
    }
}

headers = {
    "Authorization": f"Bearer {sheety_token}"
}

response = requests.post(url=sheety_endpoint, json=post_config, headers=headers)
print(response.text)