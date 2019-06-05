#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

from Observer.modules.database import DataBase
import logging

class Categories:
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

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('DataBase')


        self.categories_names = {
            "1" : "Other",
            "2" : "Communications",
            "3" : "Core Sites",
            "4" : "Other Languages",
            "5" : "Adult",
            "6" : "Hosting",
            "7" : "Personal",
            "8" : "Social",
            "9" : "Politics and Religion",
            "10" : "Developer",
            "11" : "Hacking",
            "12" : "Security",
            "13" : "Drug",
            "14" : "Games",
            "15" : "Script"
        }


        self.categories_term_Communications = [
            "forum",
            "press",
            "chat",
        ]
        self.categories_term_Core_Sites = [
            "search",
            "introduction point",
        ]
        self.categories_term_Other_Languages = [
            "arabic",
            "chinese",
            "french",
            "german",
            "italian",
            "japanese",
            "polish",
            "portuguese",
            "russians",
            "Spanish",
        ]
        self.categories_term_Adult = [
            "hardcore",
            "softcore",
            "erotica",
            "fetish",
            "violence",
            "escorts",
            "porn",
        ]
        self.categories_term_Hosting = [
            "domains",
            "file Hosting",
            "pastebin",
            "proxies",
            "web hosting",

        ]
        self.categories_term_Personal = [
            "blog",
            "books",
            "pages",
        ]
        self.categories_term_Social = [
            "bbs",
            "chans",
            "wiki",
            "social network",
        ]
        self.categories_term_Politics_and_Religion = [
            "activism",
            "law",
            "paranormal",
            "politics",
            "religion",
            "whistleblowing",
        ]
        self.categories_term_Developer = [
            "development",
            "c++",
            "c#",
            "python",
            "HTML",
            "ruby",
            "jupyter notebook",
            "java script",
            "java",
        ]
        self.categories_term_Hacking = [
            "hacker",
            "blackbox",
            "read team",
            "redhat",
            "blackhat",
            "word",
            "cracked",
            "hacked",
            "blueteam",
            "Phishing",
            "Malware",
            "Lamer",
            "Cracker",
            "Defacer",
            "Spyware",
            "Ciberpirata",
            "Freiro",
            "Scammers",
            "Uc",
            "RAT",
            "DDOS",
            "FUD",
            "SQL",
            "XSS",
            "Skid",
            "Malware",
            "VPS",
            "ANSI Bomb",
            "Back Door",
            "Bot",
            "Botnet",
            "Buffer Overflow",
            "Cracker",
            "DOX",
            "Exploit",
            "Rainbow Table",
            "Root",
            "Reverse Engineering",
            "Shell",
            "Script Kiddie",
            "Spoof",
            "SQL Injection",
            "Trojan",
            "worm",
            "zero day exploit",
        ]
        self.categories_term_Security = [
            "Sniffr",
            "wash",
            "Pay",
            "Shield",
            "Private",
            "Strategic",
            "Intelligence",
            "Safe",
            "Bitcoin",
            "Anonymity",
        ]
        self.categories_term_Drug = [
            "drugs",
            "drug-shop",
            "Acid",
            "Asteroid",
            "Berry",
        ]
        self.categories_term_Games = [
            "Poker",
            "games",
            "Multiplayer",
            "Play Free",
            "Casino",
        ]



    @property
    def start(self):
        self.save_categories()
        self.save_terms()

    def save_categories(self):
        self.logger.info(' Verificando se as categorias já estão registradas no banco de dados.')

        for id, name in self.categories_names.items():
            if self.database.compare_categories_add(categorie=name):
                self.logger.debug(' Categoria {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_add(categorie=name)

    def save_terms(self):
        self.logger.info(' Verificando se os termos das categorias já estão registradas no banco de dados.')

        for name in self.categories_term_Communications:
            if self.database.compare_categories_terms_add(id=2, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=2, term=name)

        for name in self.categories_term_Core_Sites:
            if self.database.compare_categories_terms_add(id=3, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=3, term=name)

        for name in self.categories_term_Other_Languages:
            if self.database.compare_categories_terms_add(id=4, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=4, term=name)

        for name in self.categories_term_Adult:
            if self.database.compare_categories_terms_add(id=5, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=5, term=name)

        for name in self.categories_term_Hosting:
            if self.database.compare_categories_terms_add(id=6, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=6, term=name)

        for name in self.categories_term_Personal:
            if self.database.compare_categories_terms_add(id=7, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=7, term=name)

        for name in self.categories_term_Social:
            if self.database.compare_categories_terms_add(id=8, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=8, term=name)

        for name in self.categories_term_Politics_and_Religion:
            if self.database.compare_categories_terms_add(id=9, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=9, term=name)

        for name in self.categories_term_Developer:
            if self.database.compare_categories_terms_add(id=10, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=10, term=name)

        for name in self.categories_term_Hacking:
            if self.database.compare_categories_terms_add(id=11, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=11, term=name)

        for name in self.categories_term_Security:
            if self.database.compare_categories_terms_add(id=12, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=12, term=name)

        for name in self.categories_term_Drug:
            if self.database.compare_categories_terms_add(id=13, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=13, term=name)

        for name in self.categories_term_Games:
            if self.database.compare_categories_terms_add(id=14, term=name):
                self.logger.debug(' Termo {} já existe no banco de dados.'.format(name))
            else:
                self.database.save_categorie_term_add(id=14, term=name)
