#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

import requests
from bs4 import BeautifulSoup
import logging
import re


class DiscoverDarkWebService:
    def __init__(
            self,
            port_proxy=None,
            type_proxy=None,
            server_proxy=None,):

        self.desktop_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0']
        self.logger = logging.getLogger('Class:DiscoverDarkWebService')
        self.session = requests.session()

        self.proxies = {
            "http": f"{type_proxy}://{server_proxy}:{port_proxy}",
        }

    @property
    def start(self):
        url = 'http://3bbaaaccczcbdddz.onion/discover'
        self.logger.info(f'Conectando em {url}')
        try:
            request = self.session.get(url, proxies=self.proxies, timeout=1000)
            soup = BeautifulSoup(request.content, features="lxml")

            onionurl = []
            for raw in soup.find('table', {'class': 'table'}).findAll('a'):

                onionurl.append(raw['href'].replace('/search?q=', ''))

            return onionurl

        except(requests.exceptions.ConnectionError,
               requests.exceptions.ChunkedEncodingError,
               requests.exceptions.ReadTimeout,
               requests.exceptions.InvalidURL) as e:
            self.logger.error(
                f'I was unable to connect to the url, because an error occurred.\n{e}')
            return None
