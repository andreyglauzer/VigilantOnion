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

class GistAPI:
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
		self.logger = logging.getLogger('Class:GistAPI')


		# TODO: QuickStart
		logging.basicConfig(level=logging.INFO)
		self.source = 'gist'


		compare_sorce = self.database.compare_source(source=self.source)

		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		# TODO: Arquivo de configuração
		self.argument = '.onion'
		self.url = 'https://gist.github.com/search?l=Text&q='

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
		#self.database.replaces()
		self.cookies()
		self.pagination()
		self.scraping()
		self.raw()

	def cookies(self):

		self.logger.info(' Iniciando Scrap no Gist.')

		with requests.Session() as self.session:
			self.headers = self.random_headers

			request = self.session.get(self.url+self.argument, headers=self.headers)

			if request.status_code == 200:
				pass
			else:
				GistAPI.start

	def pagination(self):
		# Converte o keyword para a leitura de URL.
		self.query = urllib.parse.quote(self.argument)
		full_url = self.url+self.argument

		self.logger.info(' Conectando em {}'.format(full_url))
		time.sleep(5)
		request = self.session.get(full_url,  headers=self.headers)
		self.soup = BeautifulSoup(request.content, features="lxml")

		pages = []
		self.urls = [full_url]
		# Verifica se existe mais de uma página no resultado de pesquisa.
		try:
			for pagination in self.soup.find('div', {'class':'pagination'}).findAll('a'):
				pages.append(pagination.get_text())
		except:
			pages = False

		# Se caso tiver mais de uma pagina de resultado, será criada uma lista com todos os resultados.
		if pages:
			cont = 2
			while cont <= int(pages[-2]):
				cont += 1
				full_url = 'https://gist.github.com/search?l=Text&p={pagination}&q={query}'.format(query=self.query, pagination=cont-1)
				self.urls.append(full_url)

	def scraping(self):
		# Inicia o scraping em URL por URL
		url = []
		for inurl in self.urls:

			self.logger.info(' Conectando em {}'.format(inurl))
			time.sleep(5)
			request = self.session.get(inurl,  headers=self.headers)

			if request.status_code == 200:
				soup = BeautifulSoup(request.content, features="lxml")
				for code in soup.findAll('div', {'class':'gist-snippet'}):
					if self.argument in code.get_text().lower():
						for raw in code.findAll('a', {'class':'link-overlay'}):
							try:
								url.append(raw['href'])
							except:
								pass
			self.urls_raw = []
			for get in url:
				self.logger.info(' Conectando em {}'.format(get))
				time.sleep(5)
				try:
					request = self.session.get(get,  headers=self.headers)

					if request.status_code == 200:
						soup = BeautifulSoup(request.content, features="lxml")

						for raw in soup.findAll('a', {'class':'btn btn-sm'}):
							try:
								gist_url = "{url}{gist}".format(url="https://gist.githubusercontent.com", gist=raw['href'])

								self.urls_raw.append(gist_url)

							except:
								pass
				except(requests.exceptions.ConnectionError,
							requests.exceptions.ChunkedEncodingError,
							requests.exceptions.ReadTimeout,
							requests.exceptions.InvalidURL) as e:
					self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))
					pass

	def raw(self):

		self.logger.info(' Realizando os replaces e regex. AGUARDE...')
		itens = []
		for raw in self.urls_raw:
			if '.txt' in raw.lower():
				time.sleep(5)
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
						.replace("https://", '')

					url = regex.match(rurls)

					if url is not None:
						self.database.saveonion(
							url=url.group(),
							source=self.source)
