# test_cbioportal.py
import pytest
from cbioportal_interface.cbioportal import CbioportalDF

def test_clinical_data_fetch():
    cbio = CbioportalDF("https://example_cbioportal/api")
    cbio.get_clinical_data()
    assert not cbio.getOutputDF().empty, "Clinical data fetch failed"
