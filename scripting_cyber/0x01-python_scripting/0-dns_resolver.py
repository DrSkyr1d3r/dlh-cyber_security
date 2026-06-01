#!/usr/bin/env python3
import socket


def resolve_domain_to_ipv4(domain_name):
    """
    Resolve a domain to its IP address.

    Args:
        domain (str): Domain name to resolve

    Returns:
        str: IP address or None
    """
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None
    except Exception as e:
        return f"Unexpected Error : {e}"
