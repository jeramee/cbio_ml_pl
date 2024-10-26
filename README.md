# cbio_ml_pl

cbio machine learning pipeline

`cbio_ml_pl` is a machine learning pipeline framework designed for seamless integration with cBioPortal data. This interface module enables cancer genomics data to be fetched, processed, and prepared for machine learning applications as part of a larger Informatics Controller system. The `cbio_ml_pl` interface is modular, allowing it to integrate easily into broader pipelines while handling cBioPortal-specific data processing.

## Features

- **Modular cBioPortal Interface**: Simplified classes to fetch data from cBioPortal (e.g., clinical data, mutations, cancer types, gene panels, case lists).
- **Data Preprocessing**: ML preprocessing functionalities for data normalization, standardization, and feature selection.
- **Socket-Based Integration**: Designed for easy data export and pipeline integration, supporting various ML frameworks.
- **Flexible and Extensible**: Can be easily customized for different data types, preprocessing steps, and machine learning tasks.

## Installation

Clone the repository:

```bash
git clone https://github.com/jeramee/cbio_ml_pl.git
cd cbio_ml_pl
```

# Usage

### Setting up the cBioPortal Interface

Define the cBioPortal server URL and use the provided classes to fetch specific data.

```python
from cbioportal_interface.cbioportal import CbioportalDF
from cbioportal_interface.informatics_controller import InformaticsController

server_url = "https://your_cbioportal_server/api"
cbioportal_df = CbioportalDF(serverURL=server_url)
informatics_controller = InformaticsController(cbioportal_df)
informatics_controller.process_data()
data_for_ml = informatics_controller.get_processed_data()
```

### Preprocessing Data

Perform normalization and standardization on the data to prepare it for ML.

```python

from ml_preprocessing.preprocess import PreprocessML

preprocessor = PreprocessML(data_for_ml['clinical_data'])
normalized_data = preprocessor.normalize_data(columns=['age', 'height', 'weight'])
```

### Socket-Based Data Export

Export data for ML pipeline integration.

```python

from cbioportal_interface.cbioportal_socket import CbioPortalSocket

cbio_socket = CbioPortalSocket(server_url)
cbio_socket.export_for_ml("clinical_data_for_ml.csv")
```

### Project Structure

```bash

cbio_ml_pl/
│
├── cbioportal_interface/             # cBioPortal Interface
│   ├── cbioportal.py                 # Interface classes for data retrieval
│   ├── informatics_controller.py     # Data processing for ML compatibility
│   └── cbioportal_socket.py          # Socket-based export module
│
├── ml_preprocessing/                 # ML Preprocessing modules
│   ├── preprocess.py                 # Preprocessing functions
│
├── tests/                            # Unit tests
│   ├── test_cbioportal.py
│   └── test_informatics_controller.py
│
├── examples/                         # Example usage
│   └── example_usage.py
│
├── LICENSE                           # License information
└── README.md                         # Project documentation
```

Setting up with Conda

For ease of environment setup and dependency management, you can use Conda to create an isolated environment for cbio_ml_pl.

### Create a new Conda environment:

```bash

conda create -n cbio_ml_pl_env python=3.8
```

### Activate the environment:

```bash

conda activate cbio_ml_pl_env
```

### Install dependencies:

If you have a requirements.txt file, use:

```bash

pip install -r requirements.txt
```

### Alternatively, if you also have a conda_requirements.yml file, you can install using:

```bash

conda env update --file conda_requirements.yml --name cbio_ml_pl_env
```

### Verify Installation:

After installation, run the tests to ensure everything is set up correctly:

```bash

    pytest tests/
```

### License

This project is licensed under the MIT License.