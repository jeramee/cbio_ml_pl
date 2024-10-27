# cbioportal.py

import pandas as pd
import requests

class CbioportalObj:
    def __init__(self, serverURL, outputString="output", outputDF=pd.DataFrame()):
        self.serverURL = serverURL
        self.outputString = outputString
        self.outputDF = outputDF
        
    def specifyQuery(self, s):
        # Method to add a query to the server URL
        self.serverURL = self.serverURL + s

class CbioportalDF(CbioportalObj):
    def fetch_data(self, query):
        response = requests.get(f"{self.serverURL}/{query}", headers={"Content-Type": "application/json"})
        if response.ok:
            print("Data fetched successfully")
            return pd.DataFrame(response.json())
        else:
            print("Error fetching data")
            return pd.DataFrame()

    def get_clinical_data(self):
        self.outputDF = self.fetch_data("clinical-data")
        return self.outputDF  # Ensure data is returned for controller

    def get_mutations_data(self):
        self.outputDF = self.fetch_data("mutations")

    def get_cancer_type_data(self):
        self.outputDF = self.fetch_data("cancer_type")

    def get_gene_panel_data(self):
        self.outputDF = self.fetch_data("gene_panel")

    def get_case_list_data(self):
        self.outputDF = self.fetch_data("case_list")

    def getOutputDF(self):
        return self.outputDF
