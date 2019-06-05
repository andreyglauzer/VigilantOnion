#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

import os
import re
import json
import errno
import signal
import logging
import requests
import collections
import time
import tempfile
from random import choice
from functools import wraps
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from Observer.modules.database import DataBase
from Observer.modules.alert import Telegram


class TorConnect:
	def __init__(
		self,
		alone=None,
		host_db=None,
		user_db=None,
		password_db=None,
		database=None,
		telegram_chat_id=None,
		telegram_token=None,
		order=None,
		number=None,
		list=None,
		list_file=None,
		ignoredate=None):

		self.ignoredate = ignoredate
		self.number = number
		self.order = order
		self.list = list
		self.list_file = list_file
		self.host_db = host_db
		self.user_db = user_db
		self.password_db = password_db
		self.telegram_chat_id = telegram_chat_id
		self.telegram_token = telegram_token
		self.database_name = database
		self.database = DataBase(
			host_db = self.host_db,
			user_db = self.user_db,
			password_db = self.password_db,
			database = self.database_name,
		)

		self.logger = logging.getLogger('Class:TorConnect')
		self.telegram = Telegram()
		self.date = datetime.now()

		self.session = requests.session()

		self.desktop_agents = [
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0']

		self.proxies = {
			'http': 'socks5h://localhost:9050',
		}

		self.alone = alone

	@property
	def headers(self):

		return {
			'User-Agent': choice(self.desktop_agents),
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
			}

	@property
	def start(self):
		self.selection()


	def selection(self):

		lastsevendays = datetime.strptime(
			time.strftime(
				'%Y-%m-%dT%H:%M:%S',
				time.localtime()
			),'%Y-%m-%dT%H:%M:%S') - timedelta(days=7)

		lastfourteendays = datetime.strptime(
			time.strftime(
				'%Y-%m-%dT%H:%M:%S',
				time.localtime()
			),'%Y-%m-%dT%H:%M:%S') - timedelta(days=14)

		if self.list is not None:
			with open(self.list_file , 'r') as outputfile:
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
						externalURL = xurl.group()
						self.logger.debug(' Comparando a URL digitada com o que está no banco de dados.')
						compare_url = self.database.compare_url(url=externalURL)

						if compare_url:
							self.logger.debug(' A url {url} já existe no banco de dados.'.format(url=externalURL))
						else:
							self.database.save_url(url=externalURL, source=1)

						for id, source_id, url, status, created_in, last_date in self.database.select_alone(alone=externalURL):
							if self.ignoredate:
								self.crawler(
									id=id,
									url=url)
							else:
								if status == 1:
									self.logger.info(' A url {url} com o status de ONLINE já foi vista.'.format(url=url))
									if last_date is not None:
										if last_date <= lastfourteendays:
											self.logger.info(' Já faz mais de duas semanas que a url {url} com o status de ONLINE foi vista pela ultima vez, uma nova verificação será feita.'.format(url=url))
											self.crawler(
												id=id,
												url=url)
										else:
											self.crawler(
												id=id,
												url=url)
								elif status == 0:
									if last_date is not None:
										if last_date <= lastsevendays:
											self.logger.info(' Já faz mais de duas semanas que a url {url} com o status de OFFILINE foi vista pela ultima vez, uma nova verificação será feita.'.format(url=url))
											self.crawler(
											 	id=id,
											 	url=url)

								else:
									self.logger.info(' A url {url} nunca foi vista, uma tentativa será feita agora..'.format(url=url))
									self.crawler(
										id=id,
										url=url)

		elif self.order:
			self.logger.info(' Você selecionou a opção para ordenar pela coluna {number}.'.format(number=self.number))
			for id, source_id, url, status, created_in, last_date in self.database.select()[int(self.number)::int(self.number)]:
				if status == 1:
					self.logger.info(' A url {url} já foi vista, será verificado a ultima vez que a mesma foi visitada.'.format(url=url))
					if last_date is not None:
						if last_date <= lastfourteendays:
							self.logger.info(' Já faz mais de duas semanas que a url {url} com o status de ONLINE foi vista pela ultima vez, uma nova verificação será feita.'.format(url=url))
							self.crawler(
								id=id,
								url=url)
						else:
							self.crawler(
								id=id,
								url=url)
				elif status == 0:
					if last_date is not None:
						if last_date <= lastsevendays:
							self.logger.info(' Já faz mais de duas semanas que a url {url} com o status de OFFILINE foi vista pela ultima vez, uma nova verificação será feita.'.format(url=url))
							self.crawler(
							 	id=id,
							 	url=url)
				else:
					self.logger.info(' A url {url} nunca foi vista, uma tentativa será feita agora..'.format(url=url))
					self.crawler(
						id=id,
						url=url)

		elif self.alone is not None:
			self.logger.info(' Você selecionou o CRAWLER para apenas uma URL.')
			if '.onion' in self.alone:

				if len(self.alone.split(',')) == 1:

					self.logger.debug(' Comparando a URL digitada com o que está no banco de dados.')
					compare_url = self.database.compare_url(url=self.alone)

					if compare_url:
						self.logger.debug(' A url {url} já existe no banco de dados.'.format(url=self.alone))
					else:
						self.database.save_url(url=self.alone, source=1)

					for id, source_id, url, status, created_in, last_date in self.database.select_alone(alone=self.alone):
						self.crawler(
							id=id,
							url=url)
				else:
					self.logger.info(' Parece que você colocou mais de uma URL, será realizado CRAWLER, uma de cada vez.')
					for alones in self.alone.split(','):
						self.logger.debug(' Comparando a URL digitada com o que está no banco de dados.')
						compare_url = self.database.compare_url(url=alones)

						if compare_url:
							self.logger.debug(' A url {url} já existe no banco de dados.'.format(url=alones))
						else:
							self.database.save_url(url=alones, source=1)

						for id, source_id, url, status, created_in, last_date in self.database.select_alone(alone=alones):
							self.crawler(
								id=id,
								url=url)

			else:
				self.logger.error(' OPSS... Isso que você digitou não é uma url da rede TOR.\n\n\n')

		else:
			self.logger.info(' Você selecionou o Crawçer padrão, seguindo pela ordem do ID.')
			for id, source_id, url, status, created_in, last_date in self.database.select():
				if status == 1:
					if last_date <= lastfourteendays:
						self.logger.info(' Já faz mais de duas semanas que a url {url} com o status de ONLINE foi vista pela ultima vez, uma nova verificação será feita.'.format(url=url))
						self.crawler(
							id=id,
							url=url)
				elif status == 0:
					if last_date <= lastfourteendays:
						self.logger.info(' Já faz mais de duas semanas que a url {url} com o status de OFFILINE foi vista pela ultima vez, uma nova verificação será feita.'.format(url=url))
						self.crawler(
							id=id,
							url=url)

				else:
					self.logger.info(' A url {url} nunca foi vista, uma tentativa será feita agora..'.format(url=url))
					self.crawler(
						id=id,
						url=url)

	def moreurls(self, url=None, default=None):
		self.logger.info(' Conectando em {}. Aguarde...'.format(url))
		fullmoreurl = None
		if url is not None:
			replace_url = url.replace('http://', '').replace('\n', '').replace('\s', '')
			try:
				request = self.session.get('http://{}'.format(replace_url), proxies=self.proxies, headers=self.headers, timeout=500)
				if request.status_code == 200:
					pages = []
					soup = BeautifulSoup(request.content, features="lxml")

					try:
						for raw in soup.find('body').findAll():
							mosturl = str(raw.get('href'))

							if raw.get('href') is not None:
								if 'http://' in mosturl:
									if '.onion' in mosturl:
										if url in mosturl:
											fullmoreurl = mosturl.replace('http://', '')
								elif 'https://' in mosturl:
									if '.onion' in mosturl:
										if url in mosturl:
											fullmoreurl = mosturl.replace('https://', '')
								else:
									if ' ' in mosturl:
										pass
									elif "'" in mosturl:
										pass
									elif '"' in mosturl:
										pass
									elif '(' in mosturl:
										pass
									else:
										if '..' in mosturl:
											if default is not None:
												fullmoreurl = '{0}/{1}'.format(default, mosturl) \
												.replace('//', '/')
											else:
												fullmoreurl = '{0}/{1}'.format(url, mosturl) \
												.replace('//', '/')
										else:

											if default is not None:
												fullmoreurl = '{0}/{1}'.format(default, mosturl) \
												.replace('//', '/')
											else:
												fullmoreurl = '{0}/{1}'.format(url, mosturl) \
												.replace('//', '/')

								if fullmoreurl is not None:
									pages.append(fullmoreurl)
					except AttributeError as e:
						self.logger.error(' OPSS... Parece que não tem texto nenhum nessa página.\n{e}'.format(e=e))
						pass

					return pages

				else:
					self.logger.error(' Não consegui conectar na url')



			except(requests.exceptions.ConnectionError,
						requests.exceptions.ChunkedEncodingError,
						requests.exceptions.ReadTimeout,
						requests.exceptions.InvalidURL) as e:
				self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))

	def crawler_text(self, url=None):

		try:
			if url is not None:
				request_pages = self.session.get(
					'http://{}'.format(url),
					proxies=self.proxies,
					headers=self.headers,
					timeout=500)

				self.logger.debug(' Conectando em {url} - {status}'.format(url=url, status= request_pages.status_code))

				if request_pages.status_code == 200:

					soup = BeautifulSoup(request_pages.content, features="lxml")
					#text =  soup_page.findAll(text=True)
					for s in soup(['script', 'style']):
						s.decompose()

					return ' '.join(soup.stripped_strings)
		except (requests.exceptions.ConnectionError,
					requests.exceptions.ChunkedEncodingError,
					requests.exceptions.ReadTimeout,
					requests.exceptions.TooManyRedirects) as e:
			pass


	class TimeoutError(Exception):
	    pass

	def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
	    def decorator(func):
	        def _handle_timeout(signum, frame):
	            raise TimeoutError(error_message)

	        def wrapper(*args, **kwargs):
	            signal.signal(signal.SIGALRM, _handle_timeout)
	            signal.alarm(seconds)
	            try:
	                result = func(*args, **kwargs)
	            finally:
	                signal.alarm(0)
	            return result

	        return wraps(func)(wrapper)

	    return decorator

	@timeout(30)
	def screenshot(self, namescreenshot=None, url=None):
		try:
			os.system("google-chrome --headless --no-sandbox --disable-gpu --proxy-server=socks://127.0.0.1:9050 --screenshot=VigilantOnion/media/sites/cover/{namescreenshot}.png http://{url}".format(namescreenshot=namescreenshot, url=url))
		except TimeoutError:
			self.logger.error(' Não foi possível realizar o screenshot da url {url}.'.format(url=url))


	def crawler(self, id, url):
		text = []
		key = None
		type = None
		status = 0

		self.logger.info(' Iniciando o Crawler na url {url}...'.format(url=url))

		if url is not None:
			self.startscritp = time.time()
			namescreenshot = url.replace('.', '')
			self.logger.debug(' Tentando conexão na url {url}, para os proximos passos.'.format(url=url))

			try:

				request_pages = self.session.get('http://{}'.format(url), proxies=self.proxies,  headers=self.headers, timeout=100)

				if request_pages.status_code == 200:
					self.logger.info(' Fazendo uma screenshot da pagina inicial da url {url}.'.format(url=url))

					self.screenshot(namescreenshot=namescreenshot, url=url)

					if self.moreurls(url=url) is not None:
						for pages in self.moreurls(url=url):
							url_pages = pages \
								.replace('\xad', '') \
								.replace('\n', '') \
								.replace("http://", '') \
								.replace("https://", '') \
								.replace(r'\s', '') \
								.replace('\t', '') \
								.replace('//', '/')

							try:
								request_pages_more = self.session.get(
										'http://{}'.format(url_pages),
										proxies=self.proxies,
										headers=self.headers,
										timeout=100)

								if request_pages_more.status_code == 200:
									if self.database.compare_more(url=url_pages):
										self.logger.debug(' A url {url} já está no banco de dados.'.format(url=url_pages))
									else:
										self.database.save_more(url=url_pages, status=1)

										if self.database.check_url_more_id(url_id=id, more_id=self.database.return_id_more(url=url_pages)[0][0]):
											self.logger.debug(' A url {url} já está no banco de dados.'.format(url=url_pages))
										else:
											self.database.save_url_more_id(url_id=id, more_id=self.database.return_id_more(url=url_pages)[0][0])

									check_sub_pages = self.moreurls(url=url_pages, default=url)

									if check_sub_pages is not None:
										for sub_pages in check_sub_pages:
											url_pages_more = sub_pages \
												.replace('\xad', '') \
												.replace('\n', '') \
												.replace("http://", '') \
												.replace("https://", '') \
												.replace(r'\s', '') \
												.replace('\t', '') \
												.replace('//', '/')
											try:
												request_pages_more = self.session.get(
														'http://{}'.format(url_pages_more),
														proxies=self.proxies,
														headers=self.headers,
														timeout=100)

												if request_pages_more.status_code == 200:
													if self.database.compare_more(url=url_pages_more):
														self.logger.debug(' A url {url} já está no banco de dados.'.format(url=url_pages_more))
													else:
														self.database.save_more(url=url_pages_more, status=1)
														if self.database.check_url_more_id(url_id=id, more_id=self.database.return_id_more(url=url_pages_more)[0][0]):
															self.logger.debug(' A url {url} já está no banco de dados.'.format(url=url_pages_more))
														else:
															self.database.save_url_more_id(url_id=id, more_id=self.database.return_id_more(url=url_pages_more)[0][0])
												else:
													self.logger.error(' Por Algum motivo, não consegui conectar na URL {url}'.format(url=url_pages_more))
											except (requests.exceptions.ConnectionError,
														requests.exceptions.ChunkedEncodingError,
														requests.exceptions.ReadTimeout,
														requests.exceptions.InvalidURL) as e:
												self.logger.error(' Um erro ocorreu.\n\n{error}\n.'.format(error=e))
												pass

							except (requests.exceptions.ConnectionError,
										requests.exceptions.ChunkedEncodingError,
										requests.exceptions.ReadTimeout,
										requests.exceptions.InvalidURL) as e:
								self.logger.error(' Um erro ocorreu.\n\n{error}\n'.format(error=e))
								pass

					self.logger.info(' Obtendo todas as informações, das páginas salvas.')
					if self.database.return_id_urls_more(id=id):
						for id_pages in self.database.return_id_urls_more(id=id):
							pagination = self.database.return_url_more(id=id_pages[0])
							filelog = "/tmp/{}".format(url.replace('onion', 'lonion'))

							if not os.path.exists(filelog):
								arquivo = open(filelog, 'w', encoding="utf8")
								arquivo.close()

							text_crawler = str(self.crawler_text(url=pagination[0][0]))
							if text_crawler is not None:
								arquivo = open(filelog, 'r', encoding="utf8")
								conteudo = arquivo.readlines()
								conteudo.append(text_crawler)
								arquivo = open(filelog, 'w', encoding="utf8")
								arquivo.writelines(conteudo)
								arquivo.close()

						counter_category = collections.Counter()
						with open(filelog, 'r' ) as a:
							self.logger.info(' Definindo a categoria do site.')
							for linha in a:
								linha = linha.split('\n')
								for id_categorie, term in self.database.return_categorie_term():
									if term.lower() in str(linha).lower():
										type = id_categorie
										counter_category[term] +=1

							self.logger.info(' Procurando por keywords.')
							for linha in a:
								linha = linha.split('\n')
								for id_keyword, company, term in self.database.return_keyword():
									if term.lower() in str(linha).lower():
										key = id_keyword
										self.database.save_search_keyword(url_id=id, company_id=company)
										break

						if key is not None:
							fim = time.time()
							self.database.save_categorie(id=id, status=1, type=type)
							alert = "KEYWORD:\n\nNew keyword:\nSite:{url}\nStatus: 200\nkeyword:{key}\nTime:{time}\n".format(
								url=url,
								key=key,
								time=int(fim-self.startscritp),
							)
							self.telegram.send(alert)

						if type is not None:
							fim = time.time()
							cover = "sites/cover/{namescreenshot}.png".format(namescreenshot=namescreenshot)
							name_type = max(counter_category.most_common())

							save_type = self.database.return_keyword_id(term=name_type[0])[0][0]

							self.database.save_categorie(id=id, status=1, type=int(save_type), cover=cover)

							alert = "New site with 200 return found:\nSite:{url}\nStatus: 200\nType:{type}\nTime:{time}\n".format(
								url=url,
								type=int(save_type),
								time=int(fim-self.startscritp),
							)
							self.telegram.send(alert)
							os.remove(filelog)

						else:
							fim = time.time()
							cover = "sites/cover/{namescreenshot}.png".format(namescreenshot=namescreenshot)
							self.database.save_categorie(id=id, status=1, type=1, cover=cover)
							alert = "New site with 200 return found:\nSite:{url}\nStatus: 200\nType:{type}\nTime:{time}\n".format(
								url=url,
								type=1,
								time=int(fim-self.startscritp),
							)
							self.telegram.send(alert)
							os.remove(filelog)
					else:
						fim = time.time()
						cover = "sites/cover/{namescreenshot}.png".format(namescreenshot=namescreenshot)
						self.database.save_categorie(id=id, status=1, type=1, cover=cover)
						alert = "New site with 200 return found:\nSite:{url}\nStatus: 200\nType:{type}\nTime:{time}\n".format(
							url=url,
							type=1,
							time=int(fim-self.startscritp),
						)
						self.telegram.send(alert)


				else:
					self.logger.error(' Por Algum motivo, não consegui conectar na URL, vou salvar como offline, para uma nova tentativa ser realizada, no proximo loop.')
					self.database.save_categorie_404(id=id, status=0)

			except (requests.exceptions.ConnectionError,
						requests.exceptions.ChunkedEncodingError,
						requests.exceptions.ReadTimeout,
						requests.exceptions.InvalidURL) as e:
				self.logger.error(' Um erro ocorreu.\n\n{error}\nPor conta desse erro vou salvar no banco de dados como offline.'.format(error=e))
				self.database.save_categorie_404(id=id, status=0)


		else:
			self.logger.debug(' Alguma URL entrou como None, melhor dar uma olhada no banco de dados.\n Talvez executar a limpeza funcione.')
