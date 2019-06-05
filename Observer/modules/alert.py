#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Andrey Glauzer'
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrey Glauzer"
__status__ = "Development"

import requests

class Telegram:
    def __init__(self):

        self.chat_id = 'CHAID'
        self.token = 'TOKENID'
        self.url = "https://api.telegram.org/bot{token}/sendMessage".format(token=self.token)


    def send(self, text=None):
        alert = text.replace('\t', '')
        params = {'chat_id': self.chat_id, 'text': alert}
        response = requests.post(self.url, data=params)

        return response
