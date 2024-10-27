# cbioportal_socket.py

from cbioportal import CbioportalDF
import pandas as pd

class CbioPortalSocket:
    def __init__(self, server_url):
        self.cbioportal = CbioportalDF(server_url)
        
    def get_case_data(self, query_string):
        self.cbioportal.specifyQuery(query_string)
        self.cbioportal.get_case_list_data()
        return self.cbioportal.getOutputDF()  # Return DataFrame for ML consumption

    def export_for_ml(self, file_path):
        df = self.get_case_data()
        df.to_csv(file_path, index=False)
        print(f"Data exported to {file_path} for ML pipeline integration")
