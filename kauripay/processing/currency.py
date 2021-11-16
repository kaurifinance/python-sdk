from typing import List


def get_currencies(self) -> List:
    """
    Shows active currencies list
    :return: the list of currencies that are active at the moment,
            with their names as identified in the system
    """
    method = 'GET'
    api_url = '/api/v1/currency'
    path = self._host + api_url

    signature = self._make_signature(method, api_url)

    response = self._make_request(method, path, signature)

    return response.get("currencies")
