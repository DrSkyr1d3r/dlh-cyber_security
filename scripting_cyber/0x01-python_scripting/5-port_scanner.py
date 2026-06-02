#!/usr/bin/env python3
import socket


def check_port(host, port):
    """
    Script that checks if a specific port is open on a host

    Args:
        host address and the port to be checked

    Returns:
        True if the port is open else False
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0
