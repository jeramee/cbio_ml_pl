# fetch_mutation_data.py

import requests
from config import BASE_URL

def fetch_mutation_data(molecular_profile_id, sample_list_id, projection="SUMMARY"):
    url = f"{BASE_URL}/molecular-profiles/{molecular_profile_id}/mutations"
    params = {
        "sampleListId": sample_list_id,
        "projection": projection
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Fetch mutation data
mutation_data = fetch_mutation_data("acc_tcga_mutations", "acc_tcga_all")
print(mutation_data)
