# PyTorTest
Simple request test for Tor service using Python

## Usage

### Requirements

This project was tested with Python 3.9.

You can install Python 3.9 with Anaconda.

After installing Python, please install requirement packages with following command.

    pip install -r requirements.txt

### Arguments

There are some arguments for Tor information.

| Argument | Description |
| :---: | :---: |
| --tor_server_ip | tor server ip address |
| --service_port | tor service port |
| --control_port | tor control port |
| --control_password | tor control password |
| --test_url | tor test url |

### Usage Example

You can use this project like this:

    python tor_test.py --tor_server_ip='localhost' --service_port=9050 --control_port=9051 --control_password='my-tor-password' --test_url='https://www.stackoverflow.com'
