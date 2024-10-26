# test_informatics_controller.py
import pytest
from cbioportal_interface.cbioportal import CbioportalDF
from cbioportal_interface.informatics_controller import InformaticsController

def test_process_data():
    cbio_df = CbioportalDF("https://example_cbioportal/api")
    controller = InformaticsController(cbio_df)
    controller.process_data()
    processed_data = controller.get_processed_data()
    assert 'clinical_data' in processed_data, "Clinical data processing missing"
