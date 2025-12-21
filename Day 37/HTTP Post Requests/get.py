import os
import requests
import json
from datetime import *
from dotenv import load_dotenv

load_dotenv()

pixela_token = os.getenv("DAY37_PIXELA_TOKEN")
pixela_username = os.getenv("DAY37_PIXELA_USERNAME")
graph_id = "graph1"

headers = {"X-USER-TOKEN": pixela_token}

# Başlangıç tarihi: 21 Aralık 2025
start_date = datetime(2025, 12, 21)
# Bitiş tarihi: bugünün tarihi
end_date = datetime.now()

# Tüm günleri dolaş
for i in range((end_date - start_date).days + 1):
    day = start_date + timedelta(days=i)
    date_str_api = day.strftime("%Y%m%d")       # Pixela için gerekli format
    date_str_print = day.strftime("%d/%m/%Y")   # Ekrana yazdırmak için istediğin format

    url = f"https://pixe.la/v1/users/{pixela_username}/graphs/{graph_id}/{date_str_api}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "optionalData" in data and data["optionalData"]:
            print(f"Date: {date_str_print}")
            try:
                opt = json.loads(data["optionalData"])
                print(json.dumps(opt, indent=2, ensure_ascii=False))
            except Exception:
                print("Raw optionalData:", data["optionalData"])
            print("-" * 40)