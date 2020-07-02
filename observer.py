#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

import os.path
import logging
import argparse
import yaml
import sys
from utils.engines.crawler import TorConnect
from utils.engines.dbconnection import DataBase
from utils.engines.gist import GistAPI
from utils.engines.SecurityNews import CyberSecurityNews
from utils.engines.reddit import Reddit
from utils.engines.DiscoverDarkWeb import DiscoverDarkWebService
from utils.engines.torch import TORCH
from utils.engines.pastebin import Pastebin


class VigilantOnion:
    def __init__(self):

        parser = argparse.ArgumentParser(
            description="VigilantOnion is a script to collect as many sites from the onion network as possible and add them to a database. With all possible sites collected, a crawler will be created so that we can monitor the search for keywords defined by you.",
            epilog="You can also develop new framework so that the database has more urls onions."
        )
        parser.add_argument(
            '--config',
            '-c',
            help="Configuration file in yaml format",
            action='store',
            dest='config'
        )

        parser.add_argument(
            '--crawler',
            help="Starts the TOR network URL crawler process.",
            action='store_true',
            dest='crawler'
        )

        parser.add_argument(
            '--url',
            '-u',
            help="Specifies the URL to crawl.",
            action='store',
            dest='url'
        )

        parser.add_argument(
            '--search',
            help="Start the URL search process on the surface.\nSelect a framework where you want to search for urls.",
            action='store_true',
            dest='search'
        )

        parser.add_argument(
            '--engines',
            '-e',
            help="Validates the available engines for searching URLs.",
            action='store',
            dest='engines'
        )

        parser.add_argument(
            '--find',
            '-f',
            help="Search for arguments on .onion network research sites",
            action='store',
            dest='find'
        )
        parser.add_argument(
            '--pastebin',
            help="Search for .onion urls in pastebin paste.",
            action='store',
            dest='pastebin'
        )

        args = parser.parse_args()

        if os.path.exists(args.config):
            if '.yml' in args.config:
                with open(args.config, 'r') as stream:
                    data = yaml.load(stream, Loader=yaml.FullLoader)
                    self.debug = data.get('debug', '')
                    self.dbname = data.get('dbname', '')
                    self.dbpath = data.get('dbpath', '')
                    self.server_proxy = data.get('server_proxy', '')
                    self.port_proxy = data.get('port_proxy', '')
                    self.type_proxy = data.get('type_proxy', '')
                    self.timeout = data.get('timeout', '')
                    self.score_categorie = data.get('score_categorie', '')
                    self.score_keywords = data.get('score_keywords', '')
                    self.count_categories = data.get('count_categories', '')
                    self.sendlog = data.get('sendlog', '')
                    self.logip = data.get('logip', '')
                    self.logport = data.get('logport', '')

                    if self.debug:
                        logging.basicConfig(
                            level=logging.DEBUG,
                            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                        )
                    else:
                        logging.basicConfig(
                            level=logging.INFO,
                            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                        )
                    self.logger = logging.getLogger('Start VigilantOnion')
                    self.crawler = args.crawler
                    self.search = args.search
                    self.url = args.url
                    self.engines = args.engines
                    self.find = args.find
                    self.pastebin = args.pastebin

            else:
                self.logger.error(
                    'The type of settings file entered is not valid\n')
                sys.exit(1)
        else:
            self.logger.error(
                'The directory or file does not exist. Check and try again.\n')
            sys.exit(1)

    @property
    def start(self):
        self.logger.debug('Checking the database if everything is OK.')
        self.database = DataBase(
            dbname=self.dbname,
            dbpath=self.dbpath)
        if self.search \
                and self.engines is not None \
                or self.pastebin is not None \
                or self.find is not None:
            if self.engines is not None:
                for engine in self.engines.split(','):
                    if engine.lower() == 'cybersecuritynews':
                        geturls = CyberSecurityNews().start
                        if geturls is not None \
                                and len(geturls) > 0:
                            for url in geturls:
                                if len(self.database.compare(url=url)) == 0:
                                    self.database.save(
                                        url=url,
                                        source="CyberSecurityNews",
                                        type="Domain",
                                    )
                    elif engine.lower() == 'gist':
                        geturls = GistAPI().start
                        if geturls is not None \
                                and len(geturls) > 0:
                            for url in geturls:
                                if len(self.database.compare(url=url)) == 0:
                                    self.database.save(
                                        url=url,
                                        source="Gist",
                                        type="Domain",
                                    )
                    elif engine.lower() == 'reddit':
                        geturls = Reddit().start
                        if geturls is not None \
                                and len(geturls) > 0:
                            for url in geturls:
                                if len(self.database.compare(url=url)) == 0:
                                    self.database.save(
                                        url=url,
                                        source="Reddit",
                                        type="Domain",
                                    )

                    elif engine.lower() == 'discoverdarkwebservice':
                        geturls = DiscoverDarkWebService(port_proxy=self.port_proxy,
                                                         type_proxy=self.type_proxy,
                                                         server_proxy=self.server_proxy).start
                        if geturls is not None \
                                and len(geturls) > 0:
                            for url in geturls:
                                if len(self.database.compare(url=url)) == 0:
                                    self.database.save(
                                        url=url,
                                        source="DiscoverDarkWebService",
                                        type="Domain",
                                    )
            elif self.pastebin is not None:
                getPastebin = Pastebin(ids=self.pastebin).start
                for url in getPastebin:
                    if len(self.database.compare(url=url)) == 0:
                        self.database.save(
                            url=url,
                            source="Pastebin",
                            type="Domain",
                        )

            elif self.find is not None:
                geturlsTORCH = TORCH(port_proxy=self.port_proxy,
                                     type_proxy=self.type_proxy,
                                     server_proxy=self.server_proxy,
                                     terms=self.find.split(','),
                                     timeout=self.timeout).start
                if geturlsTORCH is not None:
                    for url in geturlsTORCH:
                        if len(self.database.compare(url=url)) == 0:
                            self.database.save(
                                url=url,
                                source="TORCH",
                                type="Domain",
                            )

        elif self.crawler:
            self.logger.info('Starting the Crawler process.')
            if self.url is not None:
                if len(self.database.compare(url=self.url)) == 0:
                    self.database.save(
                        url=self.url,
                        source="Script",
                        type="Script"
                    )
                TorConnect(
                    urls=self.database.select_url(url=self.url),
                    port_proxy=self.port_proxy,
                    type_proxy=self.type_proxy,
                    server_proxy=self.server_proxy,
                    dbname=self.dbname,
                    dbpath=self.dbpath,
                    timeout=self.timeout,
                    count_categories=self.count_categories,
                    sendlog=self.sendlog,
                    logip=self.logip,
                    logport=self.logport,
                    score_categorie=self.score_categorie,
                    score_keywords=self.score_keywords
                ).start
            else:
                select_urls = self.database.select(
                    score_categorie=self.score_categorie, score_keywords=self.score_keywords)
                TorConnect(
                    urls=select_urls,
                    port_proxy=self.port_proxy,
                    type_proxy=self.type_proxy,
                    server_proxy=self.server_proxy,
                    dbname=self.dbname,
                    dbpath=self.dbpath,
                    timeout=self.timeout,
                    count_categories=self.count_categories,
                    sendlog=self.sendlog,
                    logip=self.logip,
                    logport=self.logport,
                    score_categorie=self.score_categorie,
                    score_keywords=self.score_keywords
                ).start


VigilantOnion().start
