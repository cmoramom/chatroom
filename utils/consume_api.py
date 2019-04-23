import requests
from requests.exceptions import InvalidSchema


class Consume(object):
    url = None
    api_token = None
    data = None

    def __init__(self, url=None, api_toke=None, data=None):
        self.url = url
        self.api_token = api_toke
        self.data = data
        self.headers = {'Content-Type': 'application/text/csv',
                        'Authorization': 'Bearer {0}'.format(self.api_token)}

    def consume_api(self):
        params = {'data': self.data}

        try:
            response = requests.get(url=self.url, data=params, headers=self.headers)
            if response.status_code == 200:
                return response.content.decode('utf-8')
            else:
                return None

        except InvalidSchema as e:
            return e
        except ConnectionError as e:
            return e
