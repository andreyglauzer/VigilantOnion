#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

import re
import json
import logging
import requests
from bs4 import BeautifulSoup
from Observer.modules.database import DataBase


class Donion:
	def __init__(
		self,
		host_db=None,
		user_db=None,
		password_db=None,
		database=None):

		self.host_db = host_db
		self.user_db = user_db
		self.password_db = password_db
		self.database_name = database
		self.database = DataBase(
			host_db = self.host_db,
			user_db = self.user_db,
			password_db = self.password_db,
			database = self.database_name,
		)

		self.source = 'Donion'
		logging.basicConfig(level=logging.INFO)

		compare_sorce = self.database.compare_source(source=self.source)

		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		self.logger = logging.getLogger('Class:Donion')
		self.session = requests.session()

		self.proxies = {
			'http': 'socks5h://localhost:9050',

		}

	@property
	def start(self):
		self.database.replaces()
		self.donion_crawler()


	def donion_crawler(self):
		url = "http://donionsixbjtiohce24abfgsffo2l4tk26qx464zylumgejukfq2vead.onion/?format=text"

		self.logger.info(' Conectando em {url}'.format(url=url))

		try:
			request = self.session.get(url, proxies=self.proxies, timeout=1000)
			soup = BeautifulSoup(request.content, features="lxml")
			list_site = soup.find('p').get_text().split('\n')

			self.logger.info(' Aplicando REGEX. Aguarde...')
			regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")
			for lines in list_site:
				rurls = lines \
					.replace('\xad', '') \
					.replace('\n', '') \
					.replace("http://", '') \
					.replace("https://", '') \
					.replace(r'\s', '') \
					.replace('\t', '')

				xurl = regex.match(rurls)

				if xurl is not None:
					self.database.saveonion(
						url=xurl.group(),
						source=self.source)
		except(requests.exceptions.ConnectionError,
					requests.exceptions.ChunkedEncodingError,
					requests.exceptions.ReadTimeout,
					requests.exceptions.InvalidURL) as e:
			self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))
			pass
