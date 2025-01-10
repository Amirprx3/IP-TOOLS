# IP-TOOLS V2

IP-TOOLS is a simple command-line toolset for network operations, including IP address lookup, port scanning, and WHOIS lookup. It is written in Python and designed for users who need basic tools for network exploration and diagnostics. The toolset is built with an interactive menu and animated text effects to enhance the user experience.

## Contents

- [Network Tools](#ip-tools)
  - [Features](#features)
  - [Installation](#installation)
- [IP-FINDER](#ip-finder)
- [PORT-SCANNER](#port-scanner)
- [CHECK-WHOIS](#check-whois)
- [Usage](#usage)


## Features

- **IP Finder**: Resolves a domain name to its corresponding IP address.
- **Port Scanner**: Scans a target IP for open ports, helping you check which services are available.
- **WHOIS Checker**: Retrieves WHOIS information for a domain, including details about its registrar, creation and expiration dates, and more.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Amirprx3/IP-TOOLS.git
   cd IP-TOOLS
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main program:
   ```bash
   python IP-TOOLS.py
   ```
2. The program will present you with a menu:
   * `1) IP-FINDER:` Find the IP address of a domain.
   * `2) PORT-SCANNER:` Scan the ports of a target IP.
   * `3) CHECK-WHOIS:` Retrieve WHOIS information for a domain.
3. Select an option by entering the corresponding number.

## Tool Details
### IP Finder
This tool allows you to input a domain name, and it will resolve it to its corresponding IP address using Python's `socket` module.

Example:
   ```python
   [+] Url: example.com
   IP: 93.184.216.34
   ```

### Port Scanner
This tool scans a specified target IP address for open ports in the range 1 to 65535. It uses the `socket` module to check each port's availability.

Example:
   ```python
   [+] Target IP: 93.184.216.34
   Scanning Target: 93.184.216.34
   Scanning started at: 14:32:10
   --------------------------------------------------
   [*] Port 80 is open
   [*] Port 443 is open
   ```

### Check whois
This tool performs a WHOIS lookup for a domain name and displays either all data or only the important fields (e.g., domain name, registrar, creation date, and status). It uses the `whois` Python library to retrieve the data.

Example:
   ```yaml
   Enter domain name for WHOIS lookup: example.com
   Display 'all data' or 'important data'? important data

   [+] Important WHOIS Information:

   domain_name: example.com
   creation_date: 1995-08-05 04:00:00
   expiration_date: 2025-08-04 04:00:00
   status: clientTransferProhibited
   registrar: Example Registrar
   ```

## Requirements
* Python 3.x
* **whois** library (installable via `pip install python-whois`)

## Contributing
Feel free to fork this repository, create a new branch, and submit pull requests for any improvements or bug fixes. Contributions are always welcome!

## License
This project is licensed under the MIT License.