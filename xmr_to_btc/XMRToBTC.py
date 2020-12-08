from http import client
from json import decoder, loads
from sys import exit
from time import time
from urllib import parse


class XMRToBTC:
    def __init__(self, api_url: str = 'xmr.to/api', api_version: str = 'v3') -> None:
        self.API_URL = api_url
        self.API_VERSION = api_version

    def _api_query(self, api_method: str, params={}, request_type: str = 'POST') -> dict:
        params['nonce'] = int(round(time() * 1000))
        params = parse.urlencode(params)

        headers = {
            "Content-type": "application/json"
        }

        conn = client.HTTPSConnection(self.API_URL)
        conn.request(request_type, "/" + self.API_VERSION + "/" + api_method, params, headers)
        response = conn.getresponse().read()

        conn.close()

        try:
            obj = loads(response.decode('utf-8'))
            if 'error' in obj and obj['error']:
                print(obj['error'])
                raise exit()
            return obj
        except decoder.JSONDecodeError:
            print('Error while parsing response:', response)
            raise exit()
