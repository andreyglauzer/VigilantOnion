#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"
import re
import time
import logging
import requests
import urllib.parse
from bs4 import BeautifulSoup
from Observer.modules.database import DataBase


class FleshOnionsAPI:
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

		self.source = 'FlashOnions'
		logging.basicConfig(level=logging.INFO)

		compare_sorce = self.database.compare_source(source=self.source)

		if compare_sorce:
			pass
		else:
			self.database.save_source(source=self.source)

		self.logger = logging.getLogger('Class:FlashOnions')
		self.session = requests.session()

		self.proxies = {
			'http': 'socks5h://localhost:9050',

		}

	@property
	def start(self):
		self.database.replaces()
		self.flash_onion()

	def flash_onion(self):

		url = 'http://vps7nsnlz3n4ckiie5evi5oz2znes7p57gmrvundbmgat22luzd4z2id.onion/'
		self.logger.info(' Conectando em {url}'.format(url=url))
		try:
			request = self.session.get(url, proxies=self.proxies, timeout=1000)

			if request.status_code == 200:
				soup = BeautifulSoup(request.content, features="lxml")

				pages = []
				for number_pages in soup.find('div', {'class':'pagination'}).findAll('a'):
					pages.append(number_pages.get_text())

				cont = 0
				urls = []
				while cont <= int(pages[-1]):
					cont += 1
					urls.append("{url}?search_title_only=on&search=&rep=n%2Fa&page={number}".format(
						number=cont-1,
						url=url
						))
				onions = []
				for connect in urls:
					time.sleep(4)
					self.logger.info(' Conectando em {url}'.format(url=connect))
					request = self.session.get(url, proxies=self.proxies, timeout=1000)

					if request.status_code == 200:
						soup = BeautifulSoup(request.content, features="lxml")

						for raw in soup.find('table', {'class':'domain_list'}).findAll('a'):
							if 'http://' in raw['href']:
								onions.append(raw['href'])

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

				for term in keywords:
					time.sleep(2)
					query = urllib.parse.quote(term)

					search = "{url}/?rep=n%2Fa&search={term}&submit=Go+%3E%3E%3E".format(
						url=url,
						term=term)

					self.logger.info(' Conectando em {url}'.format(url=search))
					request = self.session.get(url, proxies=self.proxies, timeout=1000)

					if request.status_code == 200:
						soup = BeautifulSoup(request.content, features="lxml")

						for raw in soup.find('table', {'class':'domain_list'}).findAll('a'):
							if 'http://' in raw['href']:
								onions.append(raw['href'])

				self.logger.info(' Aplicando REGEX. Aguarde...')
				regex = re.compile("[A-Za-z0-9]{0,12}\.?[A-Za-z0-9]{12,50}\.onion")

				for lines in onions:
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

		except(requests.exceptions.ConnectionError,
					requests.exceptions.ChunkedEncodingError,
					requests.exceptions.ReadTimeout,
					requests.exceptions.InvalidURL) as e:
			self.logger.error(' Não consegui conectar na url, porque ocorreu um erro.\n{e}'.format(e=e))
			pass
