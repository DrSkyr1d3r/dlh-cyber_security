#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def download_page(url):
    """
        Download the website

        Args:
            url for the page to be downloaded

        Return:
            The formatted html content of the url
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser').prettify()
        return soup
    except requests.exceptions.RequestException:
        pass
