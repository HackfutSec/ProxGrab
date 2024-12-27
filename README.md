# ProxGrab

ProxGrab is a tool that allows you to fetch public HTTP, SOCKS4, and SOCKS5 proxies from an API, verify their validity, and save them to a file for later use. This project is primarily designed for security researchers and online anonymity professionals.

## Features

- **Proxy Retrieval**: Download public proxies of various types (HTTP, SOCKS4, SOCKS5).
- **Validity Check**: Verify if the proxies are accessible before saving them.
- **IP Information**: Get geographical information (country, city) associated with each proxy.
- **Save Valid Proxies**: Save valid proxies to a text file with a unique name if needed.
- **User Interface**: Simple command-line interface with selection options for proxy type and country.

## Installation

### Prerequisites

1. **Python 3.6+**: The script is written in Python and requires Python 3.6 or later.
2. **Python Libraries**: Install the required libraries via pip:

```bash
pip install requests prettytable
```

### Clone the Repository

Clone this GitHub repository to your local machine:

```bash
git clone https://github.com/HackfutSec/ProxGrab.git
cd ProxGrab
```

## Usage

1. **Run the Script**: Once you have cloned the repository and installed dependencies, you can run the script by executing the following command:

```bash
python proxgrab.py
```

2. **Select Proxy Type**: The tool will prompt you to choose the type of proxy you want to grab:
    - **1 - HTTP**
    - **2 - SOCKS4**
    - **3 - SOCKS5**

3. **Select Country**: Then, you’ll be asked to choose a country code (e.g., "1" for the United States, "2" for Canada, etc.).

4. **Enter Number of Proxies**: The tool will then ask how many proxies you want to retrieve. You can specify a number of proxies to fetch.

5. **Save Valid Proxies**: After fetching and verifying the proxies, they will be saved to a text file. If the file already exists, a numeric suffix will be added to create a unique filename.

## Example Output

Here’s an example of what the output may look like:

```
[!] Select the type of proxy you want:

1 - HTTP
2 - SOCKS4
3 - SOCKS5
4 - Quit

[!] Enter your choice (1-4): 1

[!] Select the country code for proxies:

1 - US
2 - CA
3 - GB
...

[!] Enter your country choice (1-32): 1

[!] How many proxies do you want to grab: 10

[!] Grabbers: 10 HTTP proxies from US...
Fetching proxies...
[!] Proxies Table:
+-------------+-------+---------+---------+--------------+---------------------+
| IP          | Port  | Country | City    | Status       | Fetch Time (s)      |
+-------------+-------+---------+---------+--------------+---------------------+
| 192.168.1.1 | 8080  | US      | New York| Reachable    | 1.23                |
| 192.168.2.1 | 1080  | US      | Los Angeles| Not Reachable| 1.23               |
+-------------+-------+---------+---------+--------------+---------------------+

[!] Hostnames Table:
+-------------+-------------+-------+--------------+
| IP          | Hostname    | Port  | Status       |
+-------------+-------------+-------+--------------+
| 192.168.1.1 | proxy1.com  | 8080  | Reachable    |
| 192.168.2.1 | Unknown     | 1080  | Not Reachable|
+-------------+-------------+-------+--------------+

[!] Valid proxies saved in HTTP_US_Proxy.txt
```

## Disclaimer

**[Warning]** The use of this tool for malicious or illegal activities is strictly prohibited. The author of this project will not be held responsible for any misuse of this tool.

## License

This project is licensed under the **MIT License**.
