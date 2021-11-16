"""
KAURI Python SDK
"""

__title__ = "KauriPay Python SDK"
__version__ = "0.0.1"

import copy
import hashlib
import hmac
import urllib
from typing import Dict, List

import requests


class API(object):

    def __init__(self,
                 api_key: str,
                 api_secret: str,
                 host: str,
                 timeout: int,
                 proxies: Dict):
        """
        :param api_key:  KEY from key-secret pair, shown when new API key is added
        :param api_secret: SECRET from key-secret pair shown when new API key is added
        :param host: API url in format: 'https://example.com/'
        :param timeout: (optional) timeout for API requests in seconds
        :param proxies: (optional) proxies for API requests (IP and port)
        """
        self._api_secret = api_secret
        self._host = host
        self._api_key = api_key
        self._session = requests.Session()
        self._timeout = timeout
        self._proxies = proxies

    def _prepare_params(self,
                        method: str,
                        path: str,
                        params: Dict) -> List:
        """
        Processes method, path, params into a flat list
        :param method: request method - 'GET', 'POST'
        :param path: HOST url + API url
        :param params: a dictionary that contains key:value parameters that we send in request
        :return: flat list of parameters-ready-to-hash
        """
        # Default empty dicts for dict params.
        params = params or {}

        params_to_hash = copy.deepcopy(params)

        for key, value in params.items():
            if type(value) is dict:
                for key_one, value_one in value.items():
                    new_key = str(key) + '_' + str(key_one)
                    params_to_hash.update({new_key: value_one})
                params_to_hash.pop(key)

        params_to_hash = [method, path, urllib.parse.urlencode(sorted(params_to_hash.items()))]
        return params_to_hash

    def _make_signature(self,
                        method: str,
                        path: str,
                        params: Dict = None) -> str:
        """
        Creates signature for request
        :param method: request method - 'GET', 'POST'
        :param path: HOST url + API url
        :param params: (optional) a dictionary that contains key:value parameters that we send in request
        :return: request signature(a string of hexadecimal digits)
        """
        api_secret = self._api_secret

        hash_ = "-".join(self._prepare_params(method, path, params))

        hashing_key = api_secret.encode('utf-8')
        H = hmac.new(key=hashing_key, digestmod=hashlib.sha256)
        H.update(hash_.encode('utf-8'))
        signature = H.hexdigest()
        return signature

    def _make_headers(self,
                      signature: str,
                      accept_language: str) -> Dict:
        """
        Creates required headers for request including API Key data
        :param signature: request signature as a string of hexadecimal digits
        :param accept_language:
                                language code to determine the language
                                in which the error description is returned.
                                'en' - English
                                'ua' - Ukrainian
                                'ru' - Russian
                                API Default: 'en'
        :return: Headers dictionary
        """
        headers = {
            "Content-Type": "application/json",
            "Accept-Language": accept_language,
            "Sign": signature,
            "Key": self._api_key,
        }
        return headers

    def _make_request(self,
                      method: str,
                      path: str,
                      signature: str,
                      params: str = None,
                      accept_language: str = None) -> requests.Response:
        """
        Constructs and sends a :class:`Request <Request>`
        :param method: request method - 'GET', 'POST'
        :param path: HOST url + API url
        :param signature: request signature as a string of hexadecimal digits
        :param params: (optional) a dictionary that contains key:value parameters that we send in request
        :param accept_language: (optional)
                                language code to determine the language
                                in which the error description is returned.
                                'en' - English
                                'ua' - Ukrainian
                                'ru' - Russian
                                API Default: 'en'
        :return: :obj: requests.Response
        """
        # Default empty dicts for dict params.
        headers = self._make_headers(signature, accept_language)
        request_dict = {'method': method,
                        'url': path,
                        'headers': headers,
                        'timeout': self._timeout,
                        'proxies': self._proxies}

        if method == 'POST':
            request_dict['json'] = params
        if method == 'GET':
            request_dict['params'] = params

        result = self._session.request(**request_dict)
        if result.status_code >= 400:
            raise Exception(result.text)

        return result.json()
