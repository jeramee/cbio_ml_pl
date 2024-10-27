# mongo_setup.py

import requests
from pymongo import MongoClient
from config import BASE_URL

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["cbioportal_data"]


# Define collections
samples_collection = db["samples"]

# Define collections
studies_collection = db["studies"]
clinical_data_collection = db["clinical_data"]
mutations_collection = db["mutations"]
genomic_profiles_collection = db["genomic_profiles"]  # New collection for genomic profiles

# Fetch studies data from the API
def fetch_studies(projection="SUMMARY"):
    url = f"{BASE_URL}/studies"
    params = {"projection": projection}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching studies: {response.status_code}")
        return []

# Fetch clinical data for a specific study
def fetch_clinical_data(study_id, clinical_data_type="SAMPLE", projection="SUMMARY"):
    url = f"{BASE_URL}/studies/{study_id}/clinical-data"
    params = {"clinicalDataType": clinical_data_type, "projection": projection}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching clinical data: {response.status_code}")
        return []

# Fetch mutation data for a specific molecular profile and sample list
def fetch_mutation_data(molecular_profile_id, sample_list_id, projection="SUMMARY"):
    url = f"{BASE_URL}/molecular-profiles/{molecular_profile_id}/mutations"
    params = {"sampleListId": sample_list_id, "projection": projection}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching mutation data: {response.status_code}")
        return []

# Fetch genomic profile data (assuming a similar endpoint exists)
def fetch_genomic_profiles(study_id, projection="SUMMARY"):
    url = f"{BASE_URL}/studies/{study_id}/genomic-profiles"
    params = {"projection": projection}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching genomic profiles: {response.status_code}")
        return []

# Insert studies into MongoDB
studies_data = fetch_studies()
if studies_data:
    studies_collection.insert_many(studies_data)
    print(f"Inserted {len(studies_data)} records into 'studies' collection.")

# Example study_id to fetch clinical and mutation data
study_id = "acc_tcga"  # Replace with a valid study_id from the API
molecular_profile_id = "acc_tcga_mutations"
sample_list_id = "acc_tcga_all"

# Insert clinical data into MongoDB
clinical_data = fetch_clinical_data(study_id)
if clinical_data:
    clinical_data_collection.insert_many(clinical_data)
    print(f"Inserted {len(clinical_data)} records into 'clinical_data' collection.")

# Insert mutation data into MongoDB
mutation_data = fetch_mutation_data(molecular_profile_id, sample_list_id)
if mutation_data:
    mutations_collection.insert_many(mutation_data)
    print(f"Inserted {len(mutation_data)} records into 'mutations' collection.")

# Insert genomic profiles into MongoDB
genomic_profiles_data = fetch_genomic_profiles(study_id)
if genomic_profiles_data:
    genomic_profiles_collection.insert_many(genomic_profiles_data)
    print(f"Inserted {len(genomic_profiles_data)} records into 'genomic_profiles' collection.")

