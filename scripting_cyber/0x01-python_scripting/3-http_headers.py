#!/usr/bin/env python3
import requests


def get_http_headers(url):
    """
    Function that retrieves HTTP response headers from a website

    Args:
        URL of the website

    Retuens:
        {'status_code': int, 'headers': dict}
    """
    headers = {}
    try:
        response = requests.get(url)
        for header, val in response.headers.items():
            headers[header] = val
        return {'status_code': response.status_code,
                'headers': headers}
    except requests.exceptions.RequestException:
        return None
