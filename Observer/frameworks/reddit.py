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
from bs4 import BeautifulSoup

class Reddit:
	def __init__(self):
		self.session = requests.session()
		self.logger = logging.getLogger('Class:RedditAPI')
		self.source = 'Reddit'

		self.url = 'https://api.pushshift.io/reddit/search/comment/?subreddit=onions&limit=1000000'
		self.desktop_agents = [
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0']

	@property
	def random_headers(self):
		return {
			'User-Agent': choice(self.desktop_agents),
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
			}

	@property
	def start(self):
		self.reddit_json()

	def reddit_json(self):
		self.logger.info(' Obtendo o json da API')
		try:
			request = self.session.get(self.url,  headers=self.random_headers)

			loaded_json = json.loads(request.content)

			self.logger.info(' Filtrando as URLS que possuem no texto a palavra .onion')
			for data in loaded_json['data']:
				reddit_url = 'https://www.reddit.com{permanet}'.format(permanet=data['permalink'])
				try:
					request = self.session.get(reddit_url,  headers=self.random_headers)
					soup = BeautifulSoup(request.content, features="lxml")

					for raw in soup.findAll('a', {'rel':'nofollow'}):
						if 'https://' in raw['href']:
							raw_text = self.raw(url=raw['href'])

							self.logger.info(' Aplicando REGEX. Aguarde...')
							regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")

							for lines in raw_text.split('\n'):
								rurls = lines \
									.replace('\xad', '') \
									.replace('\n', '') \
									.replace("http://", '') \
									.replace("https://", '') \
									.replace(r'\s', '') \
									.replace('\t', '')

								xurl = regex.match(rurls)
								print(rurls)
								if xurl is not None:
									print('\n\n\n\n\n',xurl.group(), '\n\n\n\n')

				except(requests.exceptions.ConnectionError,
							requests.exceptions.ChunkedEncodingError,
							requests.exceptions.ReadTimeout,
							requests.exceptions.InvalidURL) as e:
					self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))

		except(requests.exceptions.ConnectionError,
					requests.exceptions.ChunkedEncodingError,
					requests.exceptions.ReadTimeout,
					requests.exceptions.InvalidURL) as e:
			self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))
			exit(0)

	def raw(self, url):
		try:
			if url is not None:
				request = self.session.get(url,  headers=self.random_headers)
				self.logger.debug(' Conectando em {url} - {status}'.format(url=url, status= request.status_code))

				if request.status_code == 200:

					soup = BeautifulSoup(request.content, features="lxml")
					#text =  soup_page.findAll(text=True)
					for s in soup(['script', 'style']):
						s.decompose()

					return ' '.join(soup.stripped_strings)

		except (requests.exceptions.ConnectionError,
					requests.exceptions.ChunkedEncodingError,
					requests.exceptions.ReadTimeout,
					requests.exceptions.TooManyRedirects) as e:
			pass


reddit = Reddit()
reddit.start
