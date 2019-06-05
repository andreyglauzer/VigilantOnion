#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

import logging
import re
from Observer.modules.database import DataBase


class ExternalListAPI:
	def __init__(
		self,
		file=None,
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

		self.source = 'Pastebin'
		logging.basicConfig(level=logging.INFO)

		compare_sorce = self.database.compare_source(source=self.source)

		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		self.logger = logging.getLogger('Class:ExternalListAPI')

		self.file = file

	@property
	def start(self):
		self.database.replaces()
		self.getExternal()

	def getExternal(self):
		self.logger.info(' Fazendo comparação da lista de URLS com o banco de dados. AGUARDE..')

		with open(self.file , 'r') as outputfile:
			self.logger.info(' Aplicando REGEX. Aguarde...')
			regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")

			for lines in outputfile.readlines():
				rurls = lines \
					.replace('\xad', '') \
			        .replace('\n', '') \
			        .replace("http://", '') \
			        .replace("https://", '') \
			        .replace(r'\s', '') \
			        .replace('\t', '')

				xurl = regex.match(rurls)

				if xurl is not None:
					compare_sorce = self.database.compare_source(source=self.source)
					compare_url = self.database.compare_url(url=xurl.group())

					if compare_url:
						self.logger.debug(' A url {url} já existe no banco de dados.'.format(url=xurl.group()))
					else:
						self.database.save_url(url=xurl.group(), source=compare_sorce[0][0])
