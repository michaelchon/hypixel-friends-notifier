import logging
import sys

import requests

from utils.construct_query import construct_query


log = logging.getLogger(__name__)


class TelegramBotAPI:
    BASE_URL = 'https://api.telegram.org/bot'

    def __init__(self, TOKEN):
        self.TOKEN = TOKEN

    def get(self, method, params={}):
        query = construct_query(params)

        res = requests.get(
            f'{TelegramBotAPI.BASE_URL}{self.TOKEN}/{method}{query}').json()

        if res['ok']:
            return res
        else:
            log.error(f'{res["error_code"]} - {res["description"]}')
            sys.exit(1)

    def send_message(self, chat_id, text):
        res = self.get('sendMessage', {'chat_id': chat_id, 'text': text})

        return res
