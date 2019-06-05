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

class TORCH:
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

		self.source = 'TORCH'
		logging.basicConfig(level=logging.INFO)

		compare_sorce = self.database.compare_source(source=self.source)

		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		self.logger = logging.getLogger('Class:TORCH')
		self.session = requests.session()

		self.proxies = {
			'http': 'socks5h://localhost:9050',

		}

		self.url = 'http://xmh57jrzrnw6insl.onion'

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
		self.pages()

	def pages(self):

		keywords = [
			'forum',
			'press',
			'search',
			'introduction',
			'arabic',
			'chinese',
			'french',
			'german',
			'italian',
			'japanese',
			'polish',
			'portuguese',
			'russians',
			'Spanish',
			'hardcore',
			'softcore',
			'erotica',
			'fetish',
			'violence',
			'escorts',
			'porn',
			'domains',
			'file',
			'pastebin',
			'proxies',
			'web',
			'blog',
			'books',
			'bbs',
			'chans',
			'wiki',
			'social',
			'Social',
			'activism',
			'paranormal',
			'politics',
			'religion',
			'whistleblowing',
			'development',
			'c++',
			'c#',
			'python',
			'HTML',
			'ruby',
			'jupyter',
			'java',
			'javascript',
			'java',
			'hacker',
			'blackbox',
			'read',
			'blackhat',
			'cracked',
			'wordlist',
			'word',
			'hacked',
			'blueteam',
			'Phishing',
			'Malware',
			'Lamer',
			'Cracker',
			'Defacer',
			'Spyware',
			'Scammers',
			'DDOS',
			'SQL',
			'sql',
			'Botnet',
			'Exploit',
			'Script',
			'zero',
			'0day',
			'zeroday',
			'Cybersecurity',
			'Cyber',
			'Hacktivism',
			'Hacktivist',
			'Keylogger',
			'Blacklist',
			'ai',
			'bitcoin',
			'Equifax',
			'Nessus',
			'openvas',
			'securitycenter',
			'Truecrypt',
			'ClamAV',
			'OSSEC',
			'paloalto',
			'BackTrack',
			'OSSIM',
			'IPCop',
			'Okta',
			'sonicwall',
			'pfsense',
			'Metasploit',
			'OpenSSH',
			'Wireshark',
			'NStealth',
			'drugs',
			'drug-shop',
			'Acid',
			'Asteroid',
			'Berry',
			'Poker',
			'games',
			'Multiplayer',
			'Play',
			'activism',
			'Casino',
			'.mp3',
			'.mp4',
			'Video',
			'Filme',
			'Movie',
			'channel',
			'message',
			'conclusion',
			'termination',
			'heading',
			'headline',
			'english',
			'mandarin',
			'hindustani',
			'arabic',
			'malay',
			'bengali',
			'sex',
			'sexy',
			'sexo',
			'sexual',
			'LGBT',
			'Abuse',
			'local',
			'ebook',
			'ebooks',
			'social',
			'christianity',
			'islam',
			'nonreligious',
			'secular',
			'secular',
			'agnostic',
			'atheist',
			'hinduism',
			'buddhism',
			'spiritism',
			'judaism',
			'primal-indigenous',
			'php',
			'visual',
			'C++',
			'delphi',
			'pascal',
			'cobol',
			'Cyberark',
			'Firewall',
			'antivirus',
			'marijuana',
			'weed',
			'cocaine',
			'heroin',
			'cannabis',
			'crack',
			'ecstasy',
			'amphetamines',
			'lsd',
			'singleplayer',
			'TV',
			'television',
			'radio',

		]

		self.headers = self.random_headers
		self.logger.info(' Conectando em {}'.format(self.url))

		urls = []
		self.logger.info(' Gerando URLS')
		for term in keywords:
			cont = 0
			while cont <= 9:
				cont +=1
				url_page = "{url}/4a1f6b371c/search.cgi?cmd=Search!&fmt=url&form=extended&GroupBySite=no&m=all&np={number}&ps=50&q={term}&sp=1&sy=1&type=&ul=&wf=2221&wm=wrd" \
					.format(
						url=self.url,
						number=cont,
						term=term)

				urls.append(url_page)

		self.logger.info(' Conectando nas paginas, e coletando URLS. AGUARDE...')
		for number_pages in urls:
			self.logger.debug(' Conectando em {}'.format(number_pages))
			try:
				request = self.session.get(number_pages, proxies=self.proxies, timeout=1000)

				if request.status_code == 200:
					soup = BeautifulSoup(request.content, features="lxml")

					regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")

					for dt in soup.findAll('dt'):
						for dt_a in dt.findAll('a'):
							rurls = dt_a.get_text() \
				                .replace('\xad', '') \
				                .replace('\n', '') \
				                .replace("http://", '') \
				                .replace("https://", '') \
				                .replace(r'\s', '') \
				                .replace('\t', '')

							full_url = regex.match(rurls)

							if full_url is not None:
								self.database.saveonion(
									url=full_url.group(),
									source=self.source)

			except(requests.exceptions.ConnectionError,
						requests.exceptions.ChunkedEncodingError,
						requests.exceptions.ReadTimeout,
						requests.exceptions.InvalidURL) as e:
				self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))
				pass
