import logging
import sys

import requests

from utils.construct_query import construct_query


log = logging.getLogger(__name__)


class HypixelAPI:
    BASE_URL = 'https://api.hypixel.net/'

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def get(self, method, params={}):
        params['key'] = self.API_KEY
        query = construct_query(params)

        res = requests.get(
            f'{HypixelAPI.BASE_URL}{method}{query}').json()

        if res['success']:
            return res
        else:
            log.error(res['cause'])
            sys.exit(1)

    def get_player(self, uuid):
        return self.get('player', {'uuid': uuid})['player']

    def get_player_session(self, uuid):
        return self.get('status', {'uuid': uuid})['session']

    def get_player_friends(self, uuid):
        return self.get('friends', {'uuid': uuid})['records']
