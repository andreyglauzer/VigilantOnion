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
from Observer.modules.database import DataBase


class GitHubAPI:
    def __init__(
        self,
        host_db=None,
        user_db=None,
        password_db=None,
        database=None,
        github_login=None,
        github_passwd=None,):

        self.github_login = github_login
        self.github_passwd = github_passwd
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

        self.logger = logging.getLogger('Class:GitHubAPI')
        self.source = 'github'
        self.user = self.github_login
        self.passwd = self.github_passwd
        self.argument = '.onion'
        self.url = 'https://github.com/session'

        compare_sorce = self.database.compare_source(source=self.source)

        if compare_sorce:
            pass
        else:
            self.database.save_source(source=self.source)

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
        self.database.replaces()
        self.cookies()
        self.login()
        self.pagination()
        self.scraping()
        self.raw()

    def cookies(self):
        with requests.Session() as self.session:

            self.headers = self.random_headers

            request = self.session.get(self.url, headers=self.headers)

            if request.status_code == 200:
                soup = BeautifulSoup(request.content, features="lxml")
                self.token = soup.find('input', attrs={'name': 'authenticity_token'})['value']

                self.logger.info( ' O token foi obtido com sucesso.')

            else:

                self.logger.error( ' Não foi possível obter o token uma nova tentativa será feita.')
                self.cookies()


    # Efetura login na página
    def login(self):

            self.login_data = {
                "commit": "Sign in",
                "utf8": True,
                "authenticity_token": "{}".format(self.token),
                "login": "{}".format(self.user),
                "password": "{}".format(self.passwd),
            }

            request = self.session.post(self.url, data=self.login_data, headers=self.headers)

            if request.status_code == 200:
                self.logger.info( ' Login efetuado com sucesso.')
            else:
                self.logger.error( ' Não foi possível efetuar login uma nova tentativa será realizada.')
                self.cookies()


    def pagination(self):
        # Converte o keyword para a leitura de URL.
        self.query = urllib.parse.quote(self.argument)
        full_url = 'https://github.com/search?q={query}&type=Code'.format(query=self.query)

        self.logger.info(' Conectando em {}'.format(full_url))

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
                full_url = 'https://github.com//search?p={pagination}&q={query}&type=Code'.format(query=self.query, pagination=cont-1)
                self.urls.append(full_url)



    def scraping(self):
        # Inicia o scraping em URL por URL
        self.url = []
        self.title = []
        for inurl in self.urls:
            self.logger.info(' Conectando em {}'.format(inurl))

            request = self.session.get(inurl,  headers=self.headers)
            self.soup = BeautifulSoup(request.content, features="lxml")



            for code in self.soup.findAll('div', {'class': 'code-list-item'}):
              if self.argument in code.get_text().lower():
                  for for_href in code.find('div', {'class': 'flex-auto'}).findAll('a'):
                      try:
                          # Obtem o titulo da URL, com informação do tipo de arquivo.
                          if '.txt' in for_href['title'].lower():
                              self.title.append(for_href['title'])
                              # Obtem informações em json, contendo a URL do arquivo
                              loaded_json = json.loads(for_href['data-hydro-click'])
                              # Faz substituição da URL para obter as informações em RAW
                              raw_url = loaded_json['payload']['result']['url'] \
                                  .replace('https://github.com/', 'https://raw.githubusercontent.com/') \
                                  .replace('/blob/', '/')
                              # Adicona as URLS em uma lista
                              self.url.append(raw_url)
                      except:
                          pass


    def raw(self):
        itens = []
        for raw in self.url:
            request = self.session.get(raw, headers=self.headers)
            self.logger.info(' Conectando em {raw}. AGUARDE...'.format(raw=raw))
            self.soup = BeautifulSoup(request.content, features="lxml")
            for pre in self.soup.findAll('body'):
                list = pre.get_text().split('\n')
                itens.extend(list)

        self.logger.info(' Realizando os replaces e regex. AGUARDE...')
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
