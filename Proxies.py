import requests
import socket
import os
from datetime import datetime
from prettytable import PrettyTable
import time

# Function to fetch proxies from the API
def fetch_proxies(proxy_type, country_code, url, count):
    try:
        start_time = time.time()  # Start timer to measure fetch time
        response = requests.get(url.format(country_code))
        response.raise_for_status()  # Check if the HTTP response is valid
        proxies = response.text.splitlines()
        end_time = time.time()  # End timer
        fetch_duration = end_time - start_time
        return proxies[:count], fetch_duration
    except requests.exceptions.RequestException as e:
        print(f"\n[!] Error fetching {proxy_type} proxies: {e}")
        return [], 0

# Function to check if a proxy is valid
def check_proxy(proxy):
    try:
        ip, port = proxy.split(":")
        socket.create_connection((ip, int(port)), timeout=5)
        return True
    except Exception:
        return False

# Function to get information about the IP address
def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'fail':
            return "Anonymous", "Anonymous"
        return data['country'], data['city']
    except requests.exceptions.RequestException:
        return "Anonymous", "Anonymous"

# Function to get the hostname of an IP address
def get_hostname(ip):
    try:
        host, _, _ = socket.gethostbyaddr(ip)
        return host
    except (socket.herror, socket.gaierror):
        return "Unknown"

# Function to save proxies to a file with a unique name if necessary
def save_proxies_to_file(proxies, filename):
    # Check if the file already exists
    if os.path.exists(filename):
        base_filename, ext = os.path.splitext(filename)
        counter = 1
        # Search for a unique filename by adding a number suffix
        while os.path.exists(f"{base_filename}_{counter}{ext}"):
            counter += 1
        filename = f"{base_filename}_{counter}{ext}"

    # Save the proxies to the file
    with open(filename, 'w') as file:
        for proxy in proxies:
            file.write(f"{proxy}\n")
    print(f"\n[!] Valid proxies saved in {filename}")

# Display welcome message
def print_welcome_message():
    print("\033[1;36m" +
          "#Author  : Hackfut\n" +
          "#Contact : t.me/H4ckfutSec\n" +
          "#License : MIT\n" + 
          "[Warning] I am not responsible for the way you will use this program [Warning]\n\n" +

          "██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██╗░░░██╗████████╗\n" +
          "██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██║░░░██║╚══██╔══╝\n" +
          "███████║███████║██║░░╚═╝█████═╝░█████╗░░██║░░░██║░░░██║░░░\n" +
          "██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██║░░░██║░░░██║░░░\n" +
          "██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║░░░░░╚██████╔╝░░░██║░░░\n" +
          "╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░\033[0m")

# Main function
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_welcome_message()

    # Define proxy URLs
    proxy_urls = {
        "HTTP": "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country={}&ssl=all&anonymity=all",
        "SOCKS4": "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country={}",
        "SOCKS5": "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country={}"
    }

    # Country codes
    country_codes = {
        "1": "US", "2": "CA", "3": "GB", "4": "AU", "5": "DE", "6": "FR", "7": "IN", "8": "JP", "9": "BR",
        "10": "RU", "11": "IT", "12": "NL", "13": "ES", "14": "SE", "15": "CH", "16": "KR", "17": "PL", "18": "MX",
        "19": "ZA", "20": "SG", "21": "MY", "22": "PH", "23": "TH", "24": "ID", "25": "AR", "26": "ZA", "27": "EG",
        "28": "RO", "29": "UA", "30": "IL", "31": "PK", "32": "NG"
    }

    while True:
        print("\033[1;33m\n[!] Select the type of proxy you want:\033[0m\n")
        print("\033[1;33m1 - HTTP\033[0m")
        print("\033[1;33m2 - SOCKS4\033[0m")
        print("\033[1;33m3 - SOCKS5\033[0m")
        print("\033[1;33m4 - Quit\033[0m")

        proxy_type = input("\033[1;32m\n[!] Enter your choice (1-4): \033[0m")

        if proxy_type == "1":
            selected_type = "HTTP"
        elif proxy_type == "2":
            selected_type = "SOCKS4"
        elif proxy_type == "3":
            selected_type = "SOCKS5"
        elif proxy_type == "4":
            print("\n[!] Closing the program.")
            break
        else:
            print("\n[!] Invalid selection. Please enter a number between 1 and 4.")
            continue

        print("\033[1;33m\n[!] Select the country code for proxies:\033[0m\n")
        for key, value in country_codes.items():
            print(f"\033[1;37m{key} - {value}\033[0m")

        country_choice = input("\033[1;32m\n[!] Enter your country choice (1-32): \033[0m")
        country_code = country_codes.get(country_choice)

        if not country_code:
            print("\n[!] Invalid country selection. Please try again.")
            continue

        try:
            count = int(input("\033[1;32m\n[!]How many proxies do you want to grab: \033[0m"))
        except ValueError:
            print("\n[!] Please enter a valid number.")
            continue

        print(f"\033[1;32m\n[!] Grabbers: \033[1;31m{count} \033[1;33m{selected_type} \033[1;37mproxies from \033[0m{country_code}\033[0m...")
        proxies, fetch_duration = fetch_proxies(selected_type, country_code, proxy_urls[selected_type], count)

        if not proxies:
            print("\n[!] No proxies found. Please try again later.")
            continue

        reachable_proxies = []
        table = PrettyTable()

        # Define the columns for proxies table
        table.field_names = ["IP", "Port", "Country", "City", "Status", "Fetch Time (s)"]

        hostname_table = PrettyTable()
        # Define the columns for hostnames table
        hostname_table.field_names = ["IP", "Hostname", "Port", "Status"]

        for proxy in proxies:
            if check_proxy(proxy):
                ip, port = proxy.split(":")
                # Get the information about the IP
                country, city = get_ip_info(ip)
                hostname = get_hostname(ip)
                reachable_proxies.append(proxy)
                table.add_row([ip, port, country, city, "Reachable", f"{fetch_duration:.2f}"])
                # Add a row to the hostname table
                hostname_table.add_row([ip, hostname, port, "Reachable"])
            else:
                ip, port = proxy.split(":")
                # If the proxy is not reachable, mark it as "Not Reachable"
                table.add_row([ip, port, "Anonymous", "Anonymous", "Not Reachable", f"{fetch_duration:.2f}"])
                hostname_table.add_row([ip, "Unknown", port, "Not Reachable"])

        print("\n[!] Proxies Table:")
        print(table)
        print("\n[!] Hostnames Table:")
        print(hostname_table)

        if reachable_proxies:
            filename = f"{selected_type}_{country_code}_Proxy.txt"
            save_proxies_to_file(reachable_proxies, filename)
        else:
            print("\n[!] No reachable proxies found.")

if __name__ == "__main__":
    main()
