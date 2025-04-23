import requests
import json
from datetime import datetime

def fetch_pireps():
    # API 
    url = "https://aviationweather.gov/api/data/pirep"

    params = {
        "format": "json",
        "hours": 1  # Fetch reports from the past 1 hour; change as needed
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        pireps_data = response.json()

        filename = f"pireps.json"

        with open(filename, 'w') as f:
            json.dump(pireps_data, f, indent=4)

        print(f"Saved {len(pireps_data)} PIREPs to {filename}")

    except requests.RequestException as e:
        print(f"Error fetching PIREPs: {e}")
    except json.JSONDecodeError:
        print("Failed to parse JSON from response.")

if __name__ == "__main__":
    fetch_pireps()
