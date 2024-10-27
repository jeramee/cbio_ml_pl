# test_cbioportal.py

import sys
import os

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from cbioportal_interface.cbioportal import CbioportalDF  # For test_cbioportal.py
from cbioportal_interface.informatics_controller import InformaticsController  # For test_informatics_controller.py

import pytest
import pandas as pd
from unittest.mock import patch
from cbioportal_interface.cbioportal import CbioportalDF

def test_clinical_data_fetch():
    with patch("cbioportal_interface.cbioportal.requests.get") as mock_get:
        # Mock a successful response with sample data
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{"patient_id": "P1", "age": 60}]

        cbio = CbioportalDF("https://example_cbioportal/api")
        cbio.get_clinical_data()

        # Assert the DataFrame is populated as expected
        output_df = cbio.getOutputDF()
        assert not output_df.empty
        assert output_df.iloc[0]["patient_id"] == "P1"
