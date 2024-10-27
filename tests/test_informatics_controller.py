# test_informatics_controller.py

import sys
import os

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from cbioportal_interface.cbioportal import CbioportalDF  # For test_cbioportal.py
from cbioportal_interface.informatics_controller import InformaticsController  # For test_informatics_controller.py

import pytest
from unittest.mock import patch
from cbioportal_interface.cbioportal import CbioportalDF
from cbioportal_interface.informatics_controller import InformaticsController

def test_process_data():
    with patch("cbioportal_interface.cbioportal.requests.get") as mock_get:
        # Mock responses for each API endpoint
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{"patient_id": "P1", "age": 60}]

        cbio_df = CbioportalDF("https://example_cbioportal/api")
        controller = InformaticsController(cbio_df)
        controller.process_data()

        # Assert data in controller
        data = controller.get_processed_data()
        assert "clinical_data" in data
        assert not data["clinical_data"].empty
        assert data["clinical_data"].iloc[0]["patient_id"] == "P1"
