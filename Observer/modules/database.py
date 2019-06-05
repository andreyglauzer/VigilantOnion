#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

import sqlite3
import os
import logging
import datetime
import time
import MySQLdb


class DataBase:
	def __init__(
	self,
	host_db=None,
	user_db=None,
	password_db=None,
	database=None
	):

		self.host_db = host_db
		self.user_db = user_db
		self.password_db = password_db
		self.database = database

		self.logger = logging.getLogger('DataBase')
		self.created_in = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"

		self.database_connector = MySQLdb.connect(
			host=self.host_db,
			user=self.user_db,
			password=self.password_db,
			database=self.database,
		)

	def saveonion(
		self,
		source=None,
		url=None):

		if url is not None:
			self.logger.debug(' Salvando URL no banco de dados. Aguarde...')

			compare_sorce = self.compare_source(source=source)
			compare_url = self.compare_url(url=url)

			if compare_url:
				self.logger.debug(' A url {url} já existe no banco de dados.'.format(url=url))
			else:
				self.save_url(url=url, source=compare_sorce[0][0])


	def replaces(self):
		conn = self.database_connector.cursor()

		self.logger.info(' Removendo sujeiras do banco de dados, AGUARDE..')
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, '  ', ''), '\r', ''), '\s', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, '\n', ''), '\n', ''), '\n', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'irc://', ''), '\r', ''), '\s', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'http//', ''), '\r', ''), '\s', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'http://', ''), '\r', ''), '\s', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'https://', ''), '\r', ''), '\s', '');")

		#self.database_connector.close()

	def clear(self):
		conn = self.database_connector.cursor()

		self.logger.info(' Removendo sujeiras do banco de dados, AGUARDE..')
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, '  ', ''), '\r', ''), '\s', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, '\n', ''), '\n', ''), '\n', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'irc://', ''), '\r', ''), '\s', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'http//', ''), '\r', ''), '\s', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'http://', ''), '\r', ''), '\s', '');")
		conn.execute("UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'https://', ''), '\r', ''), '\s', '');")

		self.logger.info(' Deletando itens duplicados do banco de dados, AGUARDE..')
		#conn.execute("delete from dashboard_urlonion using dashboard_urlonion, dashboard_urlonion e1 where dashboard_urlonion.id > e1.id and dashboard_urlonion.url = e1.url;")

		self.database_connector.close()


	def compare_categories_terms_add(self, term, id):

		if term is not None:
			conn = self.database_connector.cursor()

			conn.execute("SELECT categorie_id, term FROM dashboard_categories WHERE term='{term}' AND categorie_id='{id}';" \
				.format(term=term, id=id))

			return conn.fetchall()

	def save_categorie_term_add(self, id, term):

		if id is not None:

			conn = self.database_connector.cursor()

			conn.execute("""
				INSERT INTO dashboard_categories (term, categorie_id)
				VALUES ('{term}', '{categorie_id}')
			""".format(term=term,categorie_id=id))

			self.database_connector.commit()
			#self.database_connector.close()


	def compare_categories_add(self, categorie):

		if categorie is not None:
			conn = self.database_connector.cursor()

			conn.execute("SELECT id FROM dashboard_namecategories WHERE categorie='{categorie}';" \
				.format(categorie=categorie))

			return conn.fetchall()


	def save_categorie_add(self, categorie=None):

		if categorie is not None:

			conn = self.database_connector.cursor()

			conn.execute("""
				INSERT INTO dashboard_namecategories (categorie)
				VALUES ('{categorie}')
			""".format(categorie=categorie,))

			self.database_connector.commit()
			#self.database_connector.close()


	def compare_source(self, source=None):

		if source is not None:
			self.logger.debug(' Verificando se já existe um Source com o Nome {}.'.format(source))

			conn = self.database_connector.cursor()

			conn.execute("SELECT id FROM dashboard_source WHERE source='{source}';" \
				.format(source=source))

			return conn.fetchall()

	def save_source(self, source=None):

		if source is not None:
			self.logger.debug(' O souce {} não existe no banco de dados, e o mesmo está sendo salvo.'.format(source))

			conn = self.database_connector.cursor()

			conn.execute("""
				INSERT INTO dashboard_source (source)
				VALUES ('{source}')
			""".format(source=source,))

			self.database_connector.commit()
			#self.database_connector.close()

	def compare_url(self, url=None):

		if url is not None:

			self.logger.debug(' Verificando se a url {} está no banco de dados.'.format(url))

			conn = self.database_connector.cursor()

			conn.execute("SELECT id FROM dashboard_urlonion WHERE url='{url}';" \
				.format(url=url))

			return conn.fetchall()

	def save_url(self, url=None, source=None):
		self.logger.debug(' Adicionando as informações no banco de dados.')

		conn = self.database_connector.cursor()

		conn.execute("""
			INSERT INTO dashboard_urlonion (source_id, url, created_in)
			VALUES ('{source}', '{url}', '{date}')
		""".format(source=source, url=url, date=self.created_in))

		self.database_connector.commit()
		#self.database_connector.close()

	def select(self):

		conn = self.database_connector.cursor()

		conn.execute("SELECT id, source_id, url, status, created_in, last_date FROM dashboard_urlonion;")

		return conn.fetchall()

	def select_order(self, number=None):

		if number is not None:
			conn = self.database_connector.cursor()

			conn.execute("SELECT id, source_id, url, status, created_in, last_date FROM dashboard_urlonion;")

			return conn.fetchall()

	def select_alone(self, alone):

		conn = self.database_connector.cursor()

		conn.execute("SELECT id, source_id, url, status, created_in, last_date FROM dashboard_urlonion WHERE url='{alone}';".format(alone=alone))

		return conn.fetchall()

	def compare_more(self,url=None):
		if url is not None:

			self.logger.debug(' Verificando se a url {} está no banco de dados.'.format(url))


			conn = self.database_connector.cursor()

			conn.execute("SELECT id, url_more, status_more FROM dashboard_moreurls WHERE url_more='{url}';" \
				.format(url=url))

			return conn.fetchall()

	def save_more(self, url=None, status=None):
		self.logger.debug(' Adicionando as informações no banco de dados.')


		conn = self.database_connector.cursor()

		conn.execute("""
			INSERT INTO dashboard_moreurls (url_more, status_more)
			VALUES ('{url}', '{status}')
		""".format(url=url, status=status))

		self.database_connector.commit()
		#self.database_connector.close()

	def return_id_more(self, url=None):

		if url is not None:

			self.logger.debug(' Verificando se a url {} está no banco de dados.'.format(url))


			conn = self.database_connector.cursor()

			conn.execute("SELECT id FROM dashboard_moreurls WHERE url_more='{url}';" \
				.format(url=url))

			return conn.fetchall()

	def save_url_more_id(self, url_id=None, more_id=None):

		if url_id is not None:
			self.logger.debug(' Adicionando as informações no banco de dados.')


			conn = self.database_connector.cursor()

			conn.execute("""
				INSERT INTO dashboard_urlonion_more (urlonion_id, moreurls_id)
				VALUES ('{url_id}', '{more_id}')
			""".format(url_id=url_id, more_id=more_id))

			self.database_connector.commit()
			#self.database_connector.close()

	def check_url_more_id(self,  url_id=None, more_id=None):

		if url_id is not None:

			self.logger.debug(' Verificando se a url {} está no banco de dados.'.format(url_id))


			conn = self.database_connector.cursor()

			conn.execute("SELECT id FROM dashboard_urlonion_more WHERE urlonion_id='{url}' AND moreurls_id='{more}';" \
				.format(url=url_id, more=more_id))

			return conn.fetchall()

	def return_categorie_term(self):

		self.logger.debug(' Solicitando os termos das categorias do banco de dados.')


		conn = self.database_connector.cursor()

		conn.execute("SELECT categorie_id, term FROM dashboard_categories;")

		return conn.fetchall()

	def return_id_urls_more(self, id=None):

		if id is not None:
			self.logger.debug(' Solicitando as suburls do site.')


			conn = self.database_connector.cursor()

			conn.execute("SELECT moreurls_id FROM dashboard_urlonion_more WHERE urlonion_id='{id}';".format(id=id))

			return conn.fetchall()

	def return_url_more(self, id):
		if id is not None:
			self.logger.debug(' Solicitando os termos das categorias do banco de dados.')

			conn = self.database_connector.cursor()

			conn.execute("SELECT url_more FROM dashboard_moreurls WHERE id='{id}';".format(id=id))

			return conn.fetchall()

	def return_keyword(self):
		self.logger.debug(' Solicitando os termos das categorias do banco de dados.')


		conn = self.database_connector.cursor()

		conn.execute("SELECT * FROM dashboard_companyterm")

		return conn.fetchall()

	def return_keyword_id(self, term):
		self.logger.debug(' Solicitando os termos das categorias do banco de dados.')


		conn = self.database_connector.cursor()

		conn.execute("SELECT categorie_id FROM dashboard_categories WHERE term='{term}'".format(term=term))

		return conn.fetchall()

	def save_search_keyword(self, url_id=None, company_id=None):

		if url_id is not None:
			self.logger.debug(' Adicionando as informações no banco de dados.')


			conn = self.database_connector.cursor()

			conn.execute("""
				INSERT INTO dashboard_urlonion_company (urlonion_id, companyterm_id)
				VALUES ('{url_id}', '{company_id}')
			""".format(url_id=url_id, company_id=company_id))

			self.database_connector.commit()
			#self.database_connector.close()

	def save_categorie(self, id, status, type, cover):

		self.logger.debug(' Adicionando as informações no banco de dados.')


		conn = self.database_connector.cursor()

		conn.execute("""
		UPDATE dashboard_urlonion
		SET status = '%s', last_date = '%s', categorie_id = '%s', cover= '%s'
		WHERE id = %s;
		""" % (status, self.created_in, type, cover, id))

		self.logger.info(' O status {status} para a URL {url}, foi atualizado com sucesso.\n\n'.format(url=id, status=status))

		self.database_connector.commit()
		#self.database_connector.close()

	def save_categorie_404(self, id, status):

		self.logger.debug(' Adicionando as informações no banco de dados.')


		conn = self.database_connector.cursor()

		conn.execute("""
		UPDATE dashboard_urlonion
		SET status = '%s', last_date= '%s'
		WHERE id = '%s'
		""" % (status, self.created_in, id))

		self.logger.info(' O status {status} para a URL {url}, foi atualizado com sucesso.\n\n'.format(url=id, status=status))

		self.database_connector.commit()
		#self.database_connector.close()
