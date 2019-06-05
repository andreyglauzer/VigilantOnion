#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

import requests
import json
import time
import re
import logging
from random import choice
from bs4 import BeautifulSoup
from datetime import datetime
from Observer.modules.database import DataBase

class DanwinAPI:
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

		self.argument = '.onion'
		self.source = 'danwin'

		compare_sorce = self.database.compare_source(source=self.source)

		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		logging.basicConfig(level=logging.INFO)
		self.logger = logging.getLogger('Class:Danwin')

		self.url = 'https://onions.danwin1210.me/onions.php?cat=19&pg=0&lang=en'

		self.desktop_agents = [
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
		]


	@property
	def random_headers(self):
		return {
			'User-Agent': choice(self.desktop_agents),
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
			}

	@property
	def start(self):
		self.database.replaces()
		self.cookies()
		self.scraper()

	def cookies(self):

		self.logger.info(' Iniciando Scrap no Danwin.')

		with requests.Session() as self.session:
			self.headers = self.random_headers
			try:
				request = self.session.get(self.url, headers=self.headers)

				if request.status_code == 200:

					soup = BeautifulSoup(request.content, features="lxml")
					self.itens = []
					for raw in soup.find('table', {'id': 'maintable'}).findAll('a'):
						self.itens.append(raw['href'])
				else:
					danwin.start
			except(requests.exceptions.ConnectionError,
						requests.exceptions.ChunkedEncodingError,
						requests.exceptions.ReadTimeout,
						requests.exceptions.InvalidURL) as e:
				self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))
				pass


	def scraper(self):
		self.logger.info(' Realizando os replaces e Regex.. AGUARDE.')

		regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")
		for lines in self.itens:
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
