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


class DataBase:
    def __init__(self,
                 dbpath=None,
                 dbname=None):
        self.logger = logging.getLogger("Database")
        self.logger.debug("Checking Database.")
        self.dbpath = dbpath
        self.dbname = dbname

        if not os.path.exists(f"{self.dbpath}/{self.dbname}"):
            conn = sqlite3.connect(
                f"{self.dbpath}/{self.dbname}")
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS "URL" (
                "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "type"	TEXT,
                "url"	TEXT,
                "title"	TEXT,
                "baseurl"	TEXT,
                "status"	TEXT,
                "count_status"	INTEGER,
                "source"	TEXT,
                "categorie"	TEXT,
                "score_categorie"	INTEGER,
                "keywords"	TEXT,
                "score_keywords"	INTEGER,
                "discovery_date"	DATE,
                "lastscan"	DATE,
                "full_match_categorie"	TEXT
            );
            """)
            conn.commit()
            conn.close()
        else:
            conn = sqlite3.connect(
                f"{self.dbpath}/{self.dbname}")
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS "URL" (
                "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "type"	TEXT,
                "url"	TEXT,
                "title"	TEXT,
                "baseurl"	TEXT,
                "status"	TEXT,
                "count_status"	INTEGER,
                "source"	TEXT,
                "categorie"	TEXT,
                "score_categorie"	INTEGER,
                "keywords"	TEXT,
                "score_keywords"	INTEGER,
                "discovery_date"	DATE,
                "lastscan"	DATE,
                "full_match_categorie"	TEXT
            );
            """)
            conn.commit()
            conn.close()

    def compare(self, url=None):
        conn = sqlite3.connect(f"{self.dbpath}/{self.dbname}")
        cursor = conn.cursor()
        r = cursor.execute(
            f"SELECT * FROM URL WHERE url='{url}';")
        return r.fetchall()
        conn.close()

    def save(self,
             url=None,
             source=None,
             type=None,
             baseurl=None):
        time.sleep(0.10)
        conn = sqlite3.connect(f"{self.dbpath}/{self.dbname}")
        cursor = conn.cursor()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        cursor.execute(
            f"INSERT INTO URL (type,url,source,baseurl,discovery_date) VALUES ('{type}','{url}','{source}','{baseurl}','{date}');")
        conn.commit()
        conn.close()

    def select(self,
               score_categorie=None,
               score_keywords=None):
        conn = sqlite3.connect(f"{self.dbpath}/{self.dbname}")
        cursor = conn.cursor()
        r = cursor.execute(
            f"SELECT * FROM URL WHERE status is NULL OR 'Offline' NOT IN ('status') AND score_keywords >= {score_categorie} OR score_keywords is NULL and score_categorie >= {score_categorie} OR score_categorie is NULL;")
        return r.fetchall()
        conn.close()

    def select_url(self, url=None):
        conn = sqlite3.connect(f"{self.dbpath}/{self.dbname}")
        cursor = conn.cursor()
        r = cursor.execute(
            f"SELECT * FROM URL WHERE url='{url}';")
        return r.fetchall()
        conn.close()

    def update_status(self,
                      id=None,
                      url=None,
                      result=None,
                      count_categories=None):
        if result == 404:
            if self.select_url(url=url)[0][6] is None:
                count_status = 1
                status = "Unknown"
            else:
                if int(self.select_url(url=url)[0][6]) <= int(count_categories):
                    count_status = int(self.select_url(url=url)[0][6])+1
                    status = "Unknown"
                else:
                    status = "Offline"
                    count_status = int(self.select_url(url=url)[0][6])+1
        else:
            status = "Online"
            count_status = 0
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        conn = sqlite3.connect(f"{self.dbpath}/{self.dbname}")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE URL
            SET status = '{status}', 
            count_status = {count_status}, 
            lastscan = '{date}'
            WHERE id = {id}""")
        conn.commit()

    def update_categorie(self,
                         id=None,
                         categorie=None,
                         title=None,
                         full_match_categorie=None,
                         score_categorie=None,
                         score_keywords=None,
                         full_match_keywords=None):
        conn = sqlite3.connect(f"{self.dbpath}/{self.dbname}")
        cursor = conn.cursor()
        if title is not None:
            if len(title) > 0:
                title = title
            else:
                title = 'Untitled'
        else:
            title = 'Untitled'

        print(f"'{categorie}',{title},'{full_match_categorie}'")
        cursor.execute(f"""
            UPDATE URL
            SET categorie = '{categorie}', 
            title = '{title}', 
            full_match_categorie = '{full_match_categorie}', 
            score_categorie = {score_categorie}, 
            keywords='{full_match_keywords}', 
            score_keywords={score_keywords}
            WHERE id = {id}""")
        conn.commit()
