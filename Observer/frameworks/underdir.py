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
from Observer.modules.database import DataBase


class UnderDir:
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

		self.source = 'UnderDir'
		logging.basicConfig(level=logging.INFO)

		compare_sorce = self.database.compare_source(source=self.source)

		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		self.logger = logging.getLogger('Class:UnderDir')
		self.session = requests.session()

		self.proxies = {
			'http': 'socks5h://localhost:9050',
		}

	@property
	def start(self):
		self.database.replaces()
		self.underdir()

	def underdir(self):

		url = 'http://underdj5ziov3ic7.onion'
		self.logger.info(' Conectando em {url}'.format(url=url))

		request = self.session.get(url, proxies=self.proxies, timeout=1000)
		soup = BeautifulSoup(request.content, features="lxml")

		for raw in soup.find('div', {'id': 'incore'}).findAll('div', {'class': 'fr_m'}):
			for category in raw.findAll('a'):
				url_list = "{url}{category}".format(category=category['href'], url=url)

				self.logger.info(' Realizando scraping em {url}'.format(url=url_list))

				request = self.session.get(url_list, proxies=self.proxies, timeout=1000)

				soup = BeautifulSoup(request.content, features='lxml')

				pages = []
				for raw in soup.find('div', {'class': 'pgn'}).findAll('a'):
					pages.append(raw.get_text())

				cont = 2
				urls = [url_list]
				while cont <= int(pages[-2]):
					cont += 1
					urls.append("{url}/pg/{number}".format(url=url_list,number=cont-1))



			for get in urls:

				self.logger.info(' Conectando em {url}.'.format(url=get))
				try:
					request = self.session.get(get, proxies=self.proxies, timeout=1000)

					if request.status_code == 200:
						soup = BeautifulSoup(request.content, features='lxml')
						itens = []
						for raw in soup.find('div', {'class': 'trr'}).findAll('a'):

							itens.append(raw['href'].replace('http://', ''))

						regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")
						for lines in itens:
							rurls = lines \
								.replace('\xad', '') \
								.replace('\n', '') \
								.replace("http://", '') \
								.replace("https://", '') \
								.replace(r'\s', '') \
								.replace('\t', '')

							urls = regex.match(rurls)

							if urls is not None:
								self.database.saveonion(
									url=urls.group(),
									source=self.source)

				except(requests.exceptions.ConnectionError,
							requests.exceptions.ChunkedEncodingError,
							requests.exceptions.ReadTimeout,
							requests.exceptions.InvalidURL) as e:
					self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))
					pass
