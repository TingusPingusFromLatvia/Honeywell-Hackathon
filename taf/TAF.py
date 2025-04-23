import requests
import json
import os
from datetime import datetime

def fetch_taf_data(icao_code, save_path='taf_data.json'):
    url = f"https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/{icao_code.upper()}.TXT"

    try:
        response = requests.get(url)
        response.raise_for_status()

        taf_text = response.text.strip()
        taf_entry = {
            "icao": icao_code.upper(),
            "fetched_at": datetime.utcnow().isoformat() + "Z",
            "taf": taf_text
        }

        if os.path.exists(save_path):
            with open(save_path, 'r') as f:
                existing_data = json.load(f)
            if isinstance(existing_data, list):
                existing_data.append(taf_entry)
            else:
                existing_data = [existing_data, taf_entry]
        else:
            existing_data = [taf_entry]

        with open(save_path, 'w') as f:
            json.dump(existing_data, f, indent=4)

        print(f"TAF data for {icao_code.upper()} appended to {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching TAF data: {e}")

#store data
fetch_taf_data("KLAX", "TAF_data.json")
fetch_taf_data("KJFK", "TAF_data.json")
fetch_taf_data("KLBF", "TAF_data.json")
