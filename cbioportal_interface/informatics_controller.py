# informatics_controller.py

class InformaticsController:
    def __init__(self, cbioportal_df):
        self.cbioportal_df = cbioportal_df
        self.data_store = {}

    def process_data(self):
        # Centralize data processing here for ML
        self.data_store['clinical_data'] = self.cbioportal_df.get_clinical_data()
        self.data_store['mutations'] = self.cbioportal_df.get_mutations_data()
        self.data_store['cancer_type'] = self.cbioportal_df.get_cancer_type_data()
        self.data_store['gene_panel'] = self.cbioportal_df.get_gene_panel_data()
        self.data_store['case_list'] = self.cbioportal_df.get_case_list_data()

    def get_processed_data(self):
        return self.data_store
