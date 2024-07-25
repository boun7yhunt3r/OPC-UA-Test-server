# OPC UA Test Server

This repository contains a simple OPC UA test server implemented in Python. The server is built using the `opcua` library, which allows for the creation and management of an OPC UA server.

### Features

- **OPC UA Server**: A fully functional OPC UA server that can be used for testing and development purposes.
- **Easy Configuration**: Simple setup and configuration for quick deployment.
- **Extensible**: Can be easily extended to include more complex OPC UA functionalities.

### Prerequisites

Before running the server, ensure you have the following installed:

- Python 3.6 or higher
- `opcua` library

You can install the `opcua` library using pip:

```bash
pip install opcua
```
## Usage

### Clone the repository:

```bash
git clone https://github.com/yourusername/opcua_test_server.git
cd opcua_test_server
```
### Run the OPC UA test server:

```bash
python opcua_test_server.py
```
The server will start and listen on the default port. You can configure the server settings by editing the opcua_test_server.py script.

## Configuration
The server can be configured by modifying the opcua_test_server.py file. Key configuration options include:

- **Server endpoint URL**
- **Node structure**
- **Security settings**

## Contact
For any questions or feedback, please open an issue on this repository or contact the maintainer.
