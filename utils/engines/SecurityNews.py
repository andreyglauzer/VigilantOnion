#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"
import requests
import json
import re
import logging
import re
import urllib.parse
from random import choice
import time
from bs4 import BeautifulSoup


class CyberSecurityNews:
    def __init__(self):
        self.logger = logging.getLogger('Class:CyberSecurityNews')
        self.session = requests.session()

        self.desktop_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0']

    @property
    def random_headers(self):
        return {
            'User-Agent': choice(self.desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

    @property
    def start(self):
        self.headers = self.random_headers
        self.logger.info("Starting the process "
                         + "of collecting CyberSecurityNews urls "
                         + "through the addresses provided.")
        time.sleep(2)
        request = self.session.get(
            "https://pastebin.com/u/cybersecuritynews/1",  headers=self.headers)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, features="lxml")

            pages_to_pages = []
            for raw in soup.find('div', {'class': 'pagination'}).findAll('a'):
                pages_to_pages.append(raw.get_text())

            cont = 2
            pages_urls = ["https://pastebin.com/u/cybersecuritynews/1"]
            while cont <= int(pages_to_pages[-2]):
                cont += 1
                pages_urls.append(
                    f"https://pastebin.com/u/cybersecuritynews/{cont-1}")

            raw_urls = []
            for get_urls in pages_urls:
                self.logger.info('Connecting in {}'.format(get_urls))

                request = self.session.get(get_urls,  headers=self.headers)
                if request.status_code == 200:
                    soup = BeautifulSoup(request.content, features="lxml")
                    for raw in soup.find('table', {'class': 'maintable'}).findAll('a'):
                        if 'archive' in raw['href']:
                            pass
                        else:
                            raw_urls.append(
                                f"https://pastebin.com/raw{raw['href']}")

            itens = []
            onionurl = []
            self.logger.info('Performing replaces and regex. WAIT...')
            for raw in raw_urls:
                print(raw)
                request = self.session.get(raw, headers=self.headers)
                soup = BeautifulSoup(request.content, features="lxml")
                raw_text = soup.find('body').get_text() \
                    .replace('\xad', ' ') \
                    .replace("http://", ' ') \
                    .replace("https://", ' ') \
                    .replace('.onion', '.onion ') \
                    .replace("\\/", "/")
                regex_match_onions = re.findall("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,62}\.onion",
                                                raw_text, re.DOTALL)
                onionurl.extend(regex_match_onions)

            return onionurl
