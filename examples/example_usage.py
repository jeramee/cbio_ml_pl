# example_usage.py

from cbioportal_interface.cbioportal import CbioportalDF
from cbioportal_interface.informatics_controller import InformaticsController
from cbioportal_interface.cbioportal_socket import CbioPortalSocket
from ml_preprocessing.preprocess import PreprocessML

# Initialize server URL
server_url = "https://your_cbioportal_server/api"

# Fetch data using CbioportalDF and InformaticsController
cbioportal_df = CbioportalDF(serverURL=server_url)
informatics_controller = InformaticsController(cbioportal_df)
informatics_controller.process_data()

# Retrieve processed data
data_for_ml = informatics_controller.get_processed_data()

# Example preprocessing
preprocessor = PreprocessML(data_for_ml['clinical_data'])
normalized_data = preprocessor.normalize_data(columns=['age', 'height', 'weight'])  # Example columns

# Export data using CbioPortalSocket
cbio_socket = CbioPortalSocket(server_url)
cbio_socket.export_for_ml("clinical_data_for_ml.csv")
