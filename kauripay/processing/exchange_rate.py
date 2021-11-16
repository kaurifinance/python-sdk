from typing import Dict


def get_exchange_rate(self) -> Dict:
    """
    Shows exchange rates for all currency pairs
    "currency_pair" example: "USD_USDT" - left value - currency to spend,
                                        - right value - currency to get

    :return: Dict {"currency_pair": "price"}
    """
    method = 'GET'
    api_url = '/api/v1/exchange_rate'
    path = self._host + api_url

    signature = self._make_signature(method, api_url)

    response = self._make_request(method, path, signature)

    return {value['pair']: value['price'] for value in response.get('rates')}
