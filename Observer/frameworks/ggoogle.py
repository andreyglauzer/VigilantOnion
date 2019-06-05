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
import os
import json
import pprint
from random import choice
from googleapiclient.discovery import build
from Observer.modules.database import DataBase

class GoogleAPI:
	def __init__(
		self,
		host_db=None,
		user_db=None,
		password_db=None,
		database=None,
		api_key=None,
		cse_id=None,):

		self.host_db = host_db
		self.user_db = user_db
		self.password_db = password_db
		self.database_name = database
		self.api_key = api_key
		self.cse_id = cse_id

		self.database = DataBase(
			host_db = self.host_db,
			user_db = self.user_db,
			password_db = self.password_db,
			database = self.database_name,
		)
		self.logger = logging.getLogger('Class:GoogleAPI')
		self.source = 'Google'

		compare_sorce = self.database.compare_source(source=self.source)
		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		self.session = requests.session()

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
		self.urls()

	def google_search(self, search_term, **kwargs):
		service = build("customsearch", "v1", developerKey=self.api_key, cache_discovery=False)
		try:
			res = service.cse().list(q=search_term, cx=self.cse_id, **kwargs).execute()
			next_response = service.cse().list(
				q=search_term,
				cx=self.cse_id,
				num=10,
				start=3,
				).execute()
			return res
		except:
			return None

	def text(self, url=None):
		if url is not None:
			try:
				request_pages = self.session.get('{}'.format(url), headers=self.random_headers, timeout=500)
				if request_pages.status_code == 200:
					soup = BeautifulSoup(request_pages.content, features="lxml")
					for s in soup(['script', 'style']):
						s.decompose()
					return ' '.join(soup.stripped_strings)
			except (requests.exceptions.MissingSchema,
						requests.exceptions.ConnectionError) as e:
				return None

	def urls(self):

		search = self.google_search('intext:.onion', num=10, start=1)
		if search is not None:
			number_pages_search = int(search['queries']['request'][0]['totalResults'])//10

			cont = 1
			urls = []
			while cont <= number_pages_search:
				cont += 1
				search = self.google_search('intext:.onion', num=10, start=cont)

				if search is not None:
					for result in search:
						if 'items' in result:
							texts = []
							for results in search[result]:
								texts.append(self.text(url=results['formattedUrl']))

				if texts is not None:
					regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")
					for lines in texts:
						if lines is not None:
							for split_lines in lines.split(r' '):
								replace_urls = split_lines \
									.replace('\xad', '') \
									.replace('\n', '') \
									.replace("http://", '') \
									.replace("https://", '') \
									.replace(r'\s', '') \
									.replace('\t', '')
								url = regex.match(replace_urls)
								if url is not None:
									self.database.saveonion(
										url=url.group(),
										source=self.source)
