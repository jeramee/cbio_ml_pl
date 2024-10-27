# fetch_clinical_data.py

import requests
from config import BASE_URL

def fetch_clinical_data(study_id, clinical_data_type="SAMPLE", projection="SUMMARY"):
    url = f"{BASE_URL}/studies/{study_id}/clinical-data"
    params = {
        "clinicalDataType": clinical_data_type,
        "projection": projection
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Fetch clinical data
clinical_data = fetch_clinical_data("acc_tcga")
print(clinical_data)
