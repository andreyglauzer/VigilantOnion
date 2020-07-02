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


class Pastebin:
    def __init__(self, ids=None):
        self.logger = logging.getLogger('Class:Pastebin')
        self.session = requests.session()
        self.ids = ids
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
                         + "of collecting pastebin urls "
                         + "through the addresses provided.")
        itens = []
        urls_onion = []
        for raw in self.ids.split(','):
            request = self.session.get(
                f"https://pastebin.com/raw/{raw}", headers=self.headers)
            soup = BeautifulSoup(request.content, features="lxml")
            raw_text = soup.find('body').get_text() \
                .replace('\xad', ' ') \
                .replace("http://", ' ') \
                .replace("https://", ' ') \
                .replace('.onion', '.onion ') \
                .replace("\\/", "/")
            regex_match_onions = re.findall("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,62}\.onion",
                                            raw_text, re.DOTALL)
            urls_onion.extend(regex_match_onions)
        return urls_onion
