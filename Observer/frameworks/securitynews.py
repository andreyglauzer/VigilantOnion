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
from Observer.modules.database import DataBase

class CyberSecurityNews:
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
		self.logger = logging.getLogger('Class:CyberSecurityNews')

		# TODO: QuickStart
		logging.basicConfig(level=logging.INFO)
		self.source = 'CyberSecurityNews-Pastebin'


		compare_sorce = self.database.compare_source(source=self.source)
		self.session = requests.session()

		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		# TODO: Arquivo de configuração
		self.argument = '.onion'
		self.url = 'https://pastebin.com/u/cybersecuritynews/1'

		self.desktop_agents = [
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0']


	# Seleciona um agent aleatório de acordo com a lista.
	@property
	def random_headers(self):
		return {
			'User-Agent': choice(self.desktop_agents),
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
			}

	@property
	def start(self):
		self.database.replaces()
		self.pages()


	def pages(self):

		self.headers = self.random_headers
		self.logger.info(' Conectando em {}'.format(self.url))

		time.sleep(2)
		request = self.session.get(self.url,  headers=self.headers)
		if request.status_code == 200:
			soup = BeautifulSoup(request.content, features="lxml")

			pages_to_pages = []
			for raw in soup.find('div', {'class': 'pagination'}).findAll('a'):
				pages_to_pages.append(raw.get_text())


			cont = 2
			pages_urls = [self.url]
			while cont <= int(pages_to_pages[-2]):
				cont +=1
				pages_urls.append("https://pastebin.com/u/cybersecuritynews/{}".format(cont-1))

			raw_urls = []
			for get_urls in pages_urls:
				self.logger.info(' Conectando em {}'.format(get_urls))

				request = self.session.get(get_urls,  headers=self.headers)
				if request.status_code == 200:
					soup = BeautifulSoup(request.content, features="lxml")
					for raw in soup.find('table', {'class':'maintable'}).findAll('a'):
						if 'archive' in raw['href']:
							pass
						else:
							raw_urls.append("https://pastebin.com/raw{}".format(raw['href']))

			itens = []
			self.logger.info(' Realizando os replaces e regex. AGUARDE...')
			for raw in raw_urls:

				request = self.session.get(raw, headers=self.headers)
				self.soup = BeautifulSoup(request.content, features="lxml")
				for pre in self.soup.findAll('body'):
					list = pre.get_text().split('\n')
					itens.extend(list)

				regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")

				for lines in itens:
					rurls = lines \
						.replace('\xad', '') \
						.replace('\n', '') \
						.replace("http://", '') \
						.replace("https://", '') \
						.replace(r'\s', '') \
						.replace('\t', '')

					url = regex.match(rurls)

					if url is not None:
						self.database.saveonion(
							url=url.group(),
							source=self.source)
