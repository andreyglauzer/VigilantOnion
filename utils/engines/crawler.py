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
import socket
import yara
import requests
import collections
import time
import pprint
from random import choice
from functools import wraps
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from utils.engines.dbconnection import DataBase


class TorConnect:
    def __init__(self,
                 urls=None,
                 port_proxy=None,
                 type_proxy=None,
                 server_proxy=None,
                 dbname=None,
                 dbpath=None,
                 timeout=None,
                 count_categories=None,
                 logport=None,
                 logip=None,
                 sendlog=None,
                 score_categorie=None,
                 score_keywords=None):
        self.database = DataBase(
            dbname=dbname,
            dbpath=dbpath)
        self.urls = urls
        self.timeout = timeout
        self.sendlog = sendlog
        self.logip = logip
        self.logport = logport
        self.score_keywords = score_keywords
        self.score_categorie = score_categorie
        self.count_categories = count_categories
        self.logger = logging.getLogger('Class:TorConnect')
        self.session = requests.session()
        self.desktop_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0']

        self.proxies = {
            "http": f"{type_proxy}://{server_proxy}:{port_proxy}",
        }

    @property
    def headers(self):
        """
            Seleciona de modo aleatório o user agent
        """
        return {
            'User-Agent': choice(self.desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

    def send_splunk_udp(self, message=None):
        """
            .INFOS
                This function sends the received logs to the splunk via UDP
        """
        time.sleep(10)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(json.dumps(message).encode(
            'UTF-8'), (self.logip, self.logport))

    def json_parse(self, raw=None):

        jsoninfos = {
            "lastscan": raw[13],
            "id": raw[0],
            "type": raw[1],
            "url": raw[2],
            "title": raw[3],
            "baseurl": raw[4],
            "status": raw[5],
            "count_status": raw[6],
            "source": raw[7],
            "categorie": raw[8],
            "keywords": [{
                "full_keywords": raw[10].replace('[', '').replace(']', '').split(', '),
                "score_keywords": raw[11]
            }],
            "categorie": [{
                "full_categorie": raw[14].replace('[', '').replace(']', '').split(', '),
                "score_categorie": raw[9]
            }],
            "discovery_date": raw[12],

        }
        """
        if self.sendlog \
                and int(raw[9]) >= self.score_categorie \
                and int(raw[11]) >= self.score_keywords:
            self.send_splunk_udp(message=jsoninfos)
        """
        self.send_splunk_udp(message=jsoninfos)

    @property
    def start(self):
        for url in self.urls:
            self.logger.info(
                "Starting the process "
                + f"Crawler at url {url[2]}.")

            self.crawler(url=url)
            if self.database.select_url(url=url[2])[0][5] == 'Online':
                self.json_parse(raw=self.database.select_url(url=url[2])[0])

            if self.database.select_url(url=url[2])[0][5] == 'Online' \
                    and int(self.database.select_url(url=url[2])[0][9]) >= self.score_categorie:
                self.logger.info(
                    "Getting more urls from the address "
                    + f"{url[2]}.")
                moreurls = self.more_urls(url=url[2])
                if moreurls is not None:
                    for uri in moreurls:
                        if len(self.database.select_url(url=uri)) == 0:
                            self.database.save(
                                url=uri,
                                source="Script",
                                type="URI",
                                baseurl=url[2],
                            )
                        self.crawler(url=self.database.select_url(url=uri)[0])
                        if self.database.select_url(url=uri)[0][5] == 'Online':
                            self.json_parse(
                                raw=self.database.select_url(url=uri)[0])

    def check_yara(self, raw=None,
                   yarafile=None):
        """
            Validates Yara Rule to categorize the sites.
        """
        if raw is not None:
            file = os.path.join(yarafile)
            rules = yara.compile(file)
            matches = rules.match(data=raw)
            return matches

    def text(self,
             response=None):
        """
            Removes all the garbage from the HTML and takes only text elements from the page.
        """
        soup = BeautifulSoup(response, features="lxml")
        for s in soup(['script', 'style']):
            s.decompose()

        return ' '.join(soup.stripped_strings)

    def crawler(self,
                url=None):
        if url is not None:
            try:
                request = self.session.get(
                    f"http://{url[2]}", proxies=self.proxies,  headers=self.headers, timeout=self.timeout)

                if request.status_code == 200:
                    self.logger.info(
                        "Updating url status "
                        + f"{url[2]} for 200.")
                    self.database.update_status(
                        id=url[0],
                        url=url[2],
                        result=200,
                        count_categories=self.count_categories
                    )
                    full_match_yara = self.check_yara(raw=self.text(
                        response=request.content).lower(),
                        yarafile="utils/yara/categories.yar")

                    if len(full_match_yara) == 0:
                        full_match_yara = "no_match"
                        categorie = "no_match"
                        score_categorie = 0
                    else:
                        full_match_yara = full_match_yara
                        categorie = full_match_yara[0]
                        cont = 1
                        score_categorie = 0
                        while cont <= int(len(full_match_yara)):
                            score_categorie += int(
                                full_match_yara[cont-1].meta['score'])
                            cont += 1

                    full_match_keywords = self.check_yara(raw=self.text(
                        response=request.content).lower(),
                        yarafile="utils/yara/keywords.yar")

                    if len(full_match_keywords) == 0:
                        full_match_keywords = "no_match"
                        score_keywords = 0
                    else:
                        full_match_keywords = full_match_keywords
                        cont = 1
                        score_keywords = 0
                        while cont <= int(len(full_match_keywords)):
                            score_keywords += int(
                                full_match_keywords[cont-1].meta['score'])
                            cont += 1

                    soup = BeautifulSoup(request.content, features="lxml")
                    try:
                        title = soup.find('title').get_text() \
                            .replace(r'\s', '') \
                            .replace('\t', '') \
                            .replace('\n', '') \
                            .replace("'", "") \
                            .replace("  ", "") \
                            .replace("   ", "")
                    except:
                        title = None

                    self.database.update_categorie(
                        id=url[0],
                        categorie=categorie,
                        full_match_categorie=full_match_yara,
                        title=title,
                        score_categorie=score_categorie,
                        score_keywords=score_keywords,
                        full_match_keywords=full_match_keywords
                    )
                else:
                    self.logger.info(
                        "Updating url status "
                        + f"{url[2]} for 404.")
                    self.database.update_status(
                        id=url[0],
                        url=url[2],
                        result=404,
                        count_categories=self.count_categories
                    )
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ChunkedEncodingError,
                    requests.exceptions.ReadTimeout,
                    requests.exceptions.InvalidURL) as e:
                self.logger.debug(
                    f'An error has occurred.\n\n{str(e)}\n')
                self.logger.info(
                    "Could not connect to the site. "
                    "Updating url status "
                    + f"{url[2]} for 404.")
                self.database.update_status(
                    id=url[0],
                    url=url[2],
                    result=404,
                    count_categories=self.count_categories
                )

    def more_urls(self, url=None):
        self.logger.info(f"Searching for new urls in: {url}")
        try:
            request = self.session.get(
                f"http://{url}", proxies=self.proxies,  headers=self.headers, timeout=self.timeout)
            if request.status_code == 200:
                pages = []
                soup = BeautifulSoup(request.content, features="lxml")
                try:
                    for raw in soup.find('body').findAll():
                        mosturl = str(raw.get('href'))
                        if raw.get('href') is not None:
                            if '/' in mosturl \
                                    and '/' != mosturl \
                                    and 'http://' not in mosturl \
                                    and 'https://' not in mosturl \
                                    and '://' not in mosturl \
                                    and 'www' not in mosturl \
                                    and ' ' not in mosturl \
                                    and "'" not in mosturl \
                                    and '(' not in mosturl \
                                    and '.m3u' not in mosturl \
                                    and '.zip' not in mosturl \
                                    and '.exe' not in mosturl \
                                    and '.onion' not in mosturl:

                                pages.append(f"{url}{mosturl}")
                                self.logger.debug('01: '+f"{url}{mosturl}")

                            elif '/' not in mosturl \
                                    and '.m3u' not in mosturl \
                                    and '.zip' not in mosturl \
                                    and '.exe' not in mosturl \
                                    and url not in mosturl \
                                    and '.php' in mosturl \
                                    or '.htm' in mosturl \
                                    and '.onion' not in mosturl:
                                pages.append(f"{url}/{mosturl}")

                                self.logger.debug('02: '+f"{url}/{mosturl}")

                            elif url in mosturl \
                                    and '.php' in mosturl \
                                    or '.htm' in mosturl \
                                    and 'http://' in mosturl:

                                pages.append(f"{mosturl}".replace(
                                    'http://', '').replace('https://', ''))

                                self.logger.debug('03: '+f"{mosturl}".replace(
                                    'http://', '').replace('https://', ''))
                            elif '.onion' in mosturl \
                                    and '.m3u' not in mosturl \
                                    and '.zip' not in mosturl \
                                    and '.exe' not in mosturl \
                                    and 'http://' in mosturl \
                                    and url not in mosturl:

                                pages.append(f"{mosturl}".replace(
                                    'http://', '').replace('https://', ''))
                                self.logger.debug('04: '+f"{mosturl}".replace(
                                    'http://', '').replace('https://', ''))
                            else:
                                self.logger.debug('ELSE: '+mosturl)
                    return pages

                except AttributeError as e:
                    self.logger.error(
                        f"OPSS... It looks like there's no text on that page.\n{e}")

        except (requests.exceptions.ConnectionError,
                requests.exceptions.ChunkedEncodingError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.InvalidURL) as e:
            self.logger.debug(
                f"Um erro ocorreu.\n\n{str(e)}\n")
