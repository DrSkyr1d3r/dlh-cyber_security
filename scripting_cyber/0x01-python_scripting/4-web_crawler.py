#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_website(start_url, max_depth=2):
    """
    Web crawler

    Args:
        Base url to start the crawl and max depth (default is 2)

    Returns:
        A set of url of the same domain that were successfully visited
    """
    visited = set()
    domain = urlparse(start_url).netloc

    def crawl(url, depth):
        if depth < 0:
            return
        if url in visited:
            return
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException:
            return
        visited.add(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                full_link = urljoin(start_url, href)
                if domain == urlparse(full_link).netloc:
                    crawl(full_link, depth - 1)
    crawl(start_url, max_depth)
    return visited
