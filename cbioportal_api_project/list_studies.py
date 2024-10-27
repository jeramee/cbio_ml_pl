# list_studies.py

import requests
from config import BASE_URL

def list_studies(projection="SUMMARY"):
    url = f"{BASE_URL}/studies"
    params = {"projection": projection}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# List all studies
studies = list_studies()
print(studies)
