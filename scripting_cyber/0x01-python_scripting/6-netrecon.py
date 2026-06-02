#!/usr/bin/env python3
import requests
import socket
import dns.resolver
from bs4 import BeautifulSoup


def dns_recon(domain):
    """
    Function to resolve domain name to ip
    and to retrive the mx records"

     Args:
        domain name to resolve

    Returns
        None
    """
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")
        mx = dns.resolver.resolve(domain, "MX")
        print(f"MX Records:")
        for item in mx:
            print(f"\t{item}")
    except socket.gaierror:
        print("DNS resolution failed")
    except Exception as e:
        print(e)


def web_recon(domain):
    """
    function for web recon

    Args:
        domain name to recon
    Returns:
        None
    """
    if not domain.startswith(("http://", "https://")):
        domain = "https://" + domain
    try:
        response = requests.get(domain)
        print(f"\nStatus Code: {response.status_code}")
        print(f"\nImportant Headers:")
        print(f"\t Server: {response.headers['Server']}")
        print(f"\t Content-Type: {response.headers['Content-Type']}")
        count = 0
        soup = BeautifulSoup(response.text, 'html.parser')
        count = len(soup.find_all('a'))
        print(f"\nTotal Links Found: {count}\n")
    except Exception as e:
        print(e)


def port_scan(domain):
    """
    Function to check if the ports 80 and 443 are open
    """
    print(f"\nScanning common ports on {domain}...")
    print("Open ports:")
    for port in [80, 443]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((domain, port))
        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSE"
        print(f"\tPort {port}: {status}")
        sock.close()
    print(f"\n")
