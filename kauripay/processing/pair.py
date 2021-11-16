from typing import Dict


def get_pairs(self) -> Dict:
    """
    Shows active currency pairs - i.e. pairs currently available for exchange
    :return: dict containing the list of active currency pairs
    """
    method = 'GET'
    api_url = '/api/v1/pair'
    path = self._host + api_url

    signature = self._make_signature(method, api_url)

    return self._make_request(method, path, signature)
