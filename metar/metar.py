import requests
import json

#API
url = "https://aviationweather.gov/api/data/metar"
params = {
    "ids": "KLAX,KJFK,KLBF",
    "format": "json",
    "hours": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    with open("metar_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("METAR data saved to metar_data.json")
else:
    print("Failed to fetch data:", response.status_code)





