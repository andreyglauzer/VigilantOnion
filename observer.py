#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

from Observer.frameworks.github import GitHubAPI
from Observer.frameworks.danwin import DanwinAPI
from Observer.frameworks.underdir import UnderDir
from Observer.frameworks.AltOnionDir import AltOnionDir
from Observer.frameworks.DiscoverDarkWeb import DiscoverDarkWebService
from Observer.frameworks.gist import GistAPI
from Observer.frameworks.ExternalList import ExternalListAPI
from Observer.frameworks.securitynews import CyberSecurityNews
from Observer.frameworks.donion import Donion
from Observer.frameworks.freshonions import FleshOnionsAPI
from Observer.frameworks.torch import TORCH
from Observer.modules.NewTor import TorConnect
from Observer.modules.database import DataBase
from Observer.modules.header import header
from Observer.modules.add_categories import Categories
from Observer.frameworks.ggoogle import GoogleAPI
import os.path
import logging
import argparse
import yaml


class VigilantOnion:
	def __init__(self,):

		with open('configure/config.yml', 'r') as stream:
			data = yaml.load(stream, Loader=yaml.FullLoader)
			self.host_db = data.get('host_db', '')
			self.user_db = data.get('user_db', '')
			self.password_db = data.get('password_db', '')
			self.database = data.get('database', '')
			self.github_login = data.get('github_login', '')
			self.github_passwd = data.get('github_passwd', '')
			self.type_proxy = data.get('type_proxy', '')
			self.server_proxy = data.get('server_proxy', '')
			self.port_proxy = data.get('port_proxy', '')
			self.telegram_chat_id = data.get('telegram_chat_id', '')
			self.telegram_token = data.get('telegram_token', '')
			self.api_key = data.get('api_key', '')
			self.cse_id = data.get('cse_id', '')

		parser = argparse.ArgumentParser(
			description="""
				VigilantOnion is a script to collect as many sites as possible from the onion network, and add to a database.
					With all possible sites collected, a crawler will be made, so we can monitor, searching for keywords defined by you.""",
			epilog="""
				You can also develop new framework so that the database has more urls onions.""",
		)
		parser.add_argument(
			'-Sg',
			help="""
				Start Get: Start the web site crawler tor through a list.\n
				Available frameworks: google/altonion/danwin/discoverydarkweb/donion/fresnonions/gist/github/securitynews/underdir,torch \n
			""",
			action='store_true',
			dest='StartGet')

		parser.add_argument(
			'-Sl',
			help="""
				Start Get: Function to do crawler on websites and get urls onions.\n
				Ex: -Sl [-l/--list] /path/file.txt\n
			""",
			action='store_true',
			dest='StartList')

		parser.add_argument(
			'-Si',
			help="""
				Start Import: Make the import of urls onions and a file.
			""",
			action='store_true',
			dest='StartImport')

		parser.add_argument(
			'-Sc',
			help="""
				Start Crawler: Start the crawler process on all URLs in the database.
				This process is very time consuming, I recommend that you use screen (Linux) to accomplish this task.
				Ex: -Sc
			""",
			action='store_true',
			dest='StartCrawler')

		parser.add_argument(
			'-So',
			help="""
				Start crawler by order by jumping one quantity at a time.
				This option should be used to start more than one screen to perform the crawler, preventing it from passing the same urls in other sessions.
				Ex: -So [-d/--desc] 3
			""",
			action='store_true',
			dest='StartOrder')

		parser.add_argument(
			'-Su',
			help="""
				Start Crawler URL: Make the crawler a single url
				Ex: -Su --url
			""",
			action='store_true',
			dest='StartCrawlerURL')

		parser.add_argument(
			'-u',
			'--url',
			help="""
				Tell the url that you want to crawl without http: // or https: //
				Ex: -Su [-u/--url] diodishsdidds.onion
			""",
			dest='url')

		parser.add_argument(
			'-i',
			'--imput',
			help="""
				Enter the directory where the file you want to import into the database is located.
				Ex: -Si [-i/--imput] /home/root/Downloads/list.txt
			""",
			dest='imput')

		parser.add_argument(
			'-l',
			'--list',
			help="""
				Enter the directory of the list of sites on the onion network.\n
				Ex: -Sl [-l/--list] /path/file.txt\n
				If you want to ignore the last time, add --ignoredate.\n
				Ex: -Sl [-l/--list] /path/file.txt --ignoredate\n
			""",
			dest='list')

		parser.add_argument(
			'-f',
			'--framework',
			help="""
				Enter the framework you want to use to get URLs onions.
				Available frameworks: alt/danwin/discover/donion/fresh/gist/github/security/underdir.
				Always use commas to separate frameworks
				Ex: -Sg [-f/--framework] alt,github,security
			""",
			dest='framework')

		parser.add_argument(
			'-d',
			'--debug',
			help='If you want to view all the action logs in the script, use debug mode in any order.',
			action='store_true',
			dest='debug')

		parser.add_argument(
			'-c',
			'--clear',
			help='Perform cleanup on the database, removing line breaks, space and tab.',
			action='store_true',
			dest='clear')

		parser.add_argument(
			'--ignoredate',
			help='Skip last view.',
			action='store_true',
			dest='ignoredate')

		parser.add_argument(
			'--initial',
			help='First adjust the database by adding new information.',
			action='store_true',
			dest='initial')

		parser.add_argument(
			'-o',
			'--order',
			help='This option is to be used along with -So, to determine how many urls you would like to skip.',
			dest='order')

		parser.add_argument(
			'--infinite',
			help="""
				It keeps the script always running in an infinite loop.
				Ex: python observer.py -Sg --framework google --infinite
			""",
			action='store_true',
			dest='infinite')


		self.args = parser.parse_args()


	@property
	def start(self):
		self.header = header()
		self.header.start

		start_framework = None

		if self.args.debug:
			logging.basicConfig(level=logging.DEBUG)
		else:
			logging.basicConfig(
				    level=logging.INFO,
				    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
				    datefmt='%Y-%m-%d %H:%M:%S',
				)

		logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

		if self.args.clear:
			database = DataBase(host_db=self.host_db,
				user_db=self.user_db,
				password_db=self.password_db,
				database=self.database,)

			database.clear()

		if self.args.initial:

			self.initialdb()

		if self.args.StartList:
			self.logger = logging.getLogger('StartListURL')
			self.start_StartList()

		if self.args.StartGet:

			self.logger = logging.getLogger('GetStStartGetart')
			if self.args.framework is not None:
				self.start_StartGet(argument=self.args.framework )
			else:
				self.logger.error(' Você precisa informar o framework que deseja usar\nEx: -Sc --framework github,gist\n\n')
				exit(0)

		if self.args.StartImport:

			self.logger = logging.getLogger('StartImport')
			if self.args.imput is not None:
				self.start_StartImport(argument=self.args.imput )

			else:
				self.logger.error(' Você precisa informar o arquivo que deseja importar\nEx: -Si --imput /root/file.txt\n\n')
				exit(0)

		if self.args.StartCrawler:

			self.logger = logging.getLogger('StartCrawler')
			self.start_StartCrawler()

		if self.args.StartCrawlerURL:

			self.logger = logging.getLogger('StartCrawlerURL')
			self.start_StartCrawler_alone()

		if self.args.StartOrder:
			self.logger = logging.getLogger('StartCrawlerURLDESC')

			try:
				if isinstance(int(self.args.order), int):
					self.start_StartCrawler_order(number=int(self.args.order))
			except ValueError as e:
				self.logger.error(' Você precisa informar um número\nEx: -So --order 3\n\n')
				exit(1)

	def start_StartList(self):

		if os.path.isfile(self.args.list):
			if self.args.ignoredate:
				database = DataBase(host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)

				self.logger.info(' Iniciando o processo de Crawler por arquivo de lista.')
				self.logger.info(' VOCÊ ESTÁ IGNORANDO A ULTIMA VEZ VISTA DA URL.')

				tor = TorConnect(telegram_chat_id = self.telegram_chat_id,
					telegram_token = self.telegram_token,
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,
					list=True,
					list_file=self.args.list,
					ignoredate=True)
				tor.start
			else:
				database = DataBase(host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)

				self.logger.info(' Iniciando o processo de Crawler por arquivo de lista.')

				tor = TorConnect(telegram_chat_id = self.telegram_chat_id,
					telegram_token = self.telegram_token,
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,
					list=True,
					list_file=self.args.list,)
				tor.start

		else:
			self.logger.error(' O arquivo {file} não existe ou o caminho está incorreto, verifique e tente novamente.\n\n'.format(file=self.args.list))
			exit(1)


	def start_StartCrawler_order(self, number=None):

		if number is not None:
			database = DataBase(host_db=self.host_db,
				user_db=self.user_db,
				password_db=self.password_db,
				database=self.database,)

			self.logger.info(' Iniciando o processo de Crawler')

			tor = TorConnect(telegram_chat_id = self.telegram_chat_id,
				telegram_token = self.telegram_token,
				host_db=self.host_db,
				user_db=self.user_db,
				password_db=self.password_db,
				database=self.database,
				order=True,
				number=number,)
			tor.start

	def start_StartCrawler_alone(self):
		database = DataBase(host_db=self.host_db,
			user_db=self.user_db,
			password_db=self.password_db,
			database=self.database,)
		self.logger.info(' Iniciando o processo de Crawler')
		tor = TorConnect(telegram_chat_id = self.telegram_chat_id,
			telegram_token = self.telegram_token,
			host_db=self.host_db,
			user_db=self.user_db,
			password_db=self.password_db,
			database=self.database,
			alone=self.args.url)
		tor.start


	def start_StartCrawler(self):
		database = DataBase(host_db=self.host_db,
			user_db=self.user_db,
			password_db=self.password_db,
			database=self.database,)
		database.clear()
		self.logger.info(' Iniciando o processo de Crawler')
		tor = TorConnect(telegram_chat_id = self.telegram_chat_id,
			telegram_token = self.telegram_token,
			host_db=self.host_db,
			user_db=self.user_db,
			password_db=self.password_db,
			database=self.database,)
		tor.start

	def start_StartImport(self, argument):
		self.logger.info(' Iniciando o processo de coleta de URLs de  {framework}'.format(framework=argument))
		if os.path.isfile(argument):
			   externallist = ExternalListAPI(
				file=argument,
				host_db=self.host_db,
				user_db=self.user_db,
				password_db=self.password_db,
				database=self.database)
			   externallist.start
		else:
			self.logger.error(' O nome de arquivo ou diretório que você digitou não existe, tente novamente.\n\n')
			exit(0)

	def start_StartGet(self, argument):
		self.logger.info(' Coletando URLs onion em {framework}'.format(framework=argument))

		self.list_frameworks = [
			'altonion',
			'danwin',
			'discoverydarkweb',
			'donion',
			'fresnonions',
			'gist',
			'github',
			'securitynews',
			'underdir',
			'google',
			'torch'
		]

		for frameworks in argument.split(','):
			if frameworks in self.list_frameworks:
				pass
			else:
				self.logger.error(" O framework '{framework}' não existe, verifique a escrita e tente novamente.\n\n".format(framework=frameworks))
				exit(0)

		if len(self.args.framework.split(',')) == 1:

			if self.args.infinite:
				while True:
					self.start_framework(framework=argument)
			else:
				self.start_framework(framework=argument)

		else:
			if self.args.infinite:
				while True:
					for frameworks in argument.split(','):
						self.start_framework(framework=frameworks)
			else:
				for frameworks in argument.split(','):
					self.start_framework(framework=frameworks)

	def initialdb(self):
		categories = Categories(
			host_db=self.host_db,
			user_db=self.user_db,
			password_db=self.password_db,
			database=self.database,)

		categories.start

	def start_framework(self, framework):

		categories = Categories(
			host_db=self.host_db,
			user_db=self.user_db,
			password_db=self.password_db,
			database=self.database,)

		categories.start
		self.logger.info(' Estou iniciando o processo de coleta de URLs com o framework {}\n'.format(framework))
		if framework is not None:
			if framework == 'altonion':
				alt = AltOnionDir(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				alt.start

			elif framework == 'danwin':
				danwin = DanwinAPI(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				danwin.start
			elif framework == 'discoverydarkweb':
				discover = DiscoverDarkWebService(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				discover.start

			elif framework == 'donion':
				donion = Donion(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				donion.start

			elif framework == 'fresnonions':
				flashonions = FleshOnionsAPI(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				flashonions.start

			elif framework == 'gist':
				gist = GistAPI(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				gist.start

			elif framework == 'github':
				github = GitHubAPI(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,
					github_login=self.github_login,
					github_passwd=self.github_passwd,)
				github.start

			elif framework == 'securitynews':
				securitynews = CyberSecurityNews(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				securitynews.start

			elif framework == 'underdir':
				underdir = UnderDir(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				underdir.start

			elif framework == 'google':
				google = GoogleAPI(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,
					api_key=self.api_key,
					cse_id=self.cse_id,)
				google.start

			elif framework == 'torch':
				torch = TORCH(
					host_db=self.host_db,
					user_db=self.user_db,
					password_db=self.password_db,
					database=self.database,)
				torch.start

			else:
				self.logger.error(" O framework '{framework}' não existe, verifique a escrita e tente novamente.\n\n".format(framework=framework))
				exit(0)

get_start = VigilantOnion()
get_start.start
