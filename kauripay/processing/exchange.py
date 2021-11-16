from typing import Dict


def create_exchange(self,
                    currency_to_get: str,
                    currency_to_spend: str,
                    currency_to_spend_amount: str = None,
                    currency_to_get_amount: str = None,
                    exchange_price: str = None,
                    callback_url: str = None) -> Dict:
    """
    Creates exchange order. If exchange_price if set - limit exchange order will be created,
    otherwise it will be market order.
    :param currency_to_get: (required) currency that will be bought during the exchange
    :param currency_to_spend: (required) currency that will be sold during the exchange

    :param currency_to_spend_amount: (optional) amount of currency that will be sold during the exchange
    :param currency_to_get_amount: (optional) amount of currency that will be bought during the exchange
                                    Only one of the two amount parameters above must be specified.
                                    If currency_to_spend_amount is specified - this amount of the currency
                                    specified in currency_to_spend parameter will be sold.
                                    If currency_to_get_amount is specified - this amount of the currency
                                    specified in currency_to_get parameter will be bought.

    :param exchange_price: (optional) used for limit exchange order only,
                            to specify the exchange price different from market
    :param callback_url: (optional) url for order's status notifications
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/exchange'
    path = self._host + api_url

    params = {
        "currency_to_get": currency_to_get,
        "currency_to_spend": currency_to_spend,
        "currency_to_get_amount": currency_to_get_amount,
        "currency_to_spend_amount": currency_to_spend_amount,
        "exchange_price": exchange_price,
        "callback_url": callback_url,
    }

    params = {key: value for key, value in params.items() if value}

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def repeat_exchange(self,
                    order_id: str) -> Dict:
    """
    Repeats previous exchange order (if it is finished) with the same parameters
    :param order_id: (required) order ID of previously finished exchange
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/exchange/repeat'
    path = self._host + api_url

    params = {
        "order_id": order_id,
    }

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def cancel_exchange(self,
                    order_id: str) -> Dict:
    """
    Cancel LIMIT order.
    Hint: Only a limit exchange order can be canceled if cancellation is enabled
    and the order is being processed.
    :param order_id: (required) order ID of the exchange to cancel
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/exchange/cancel'
    path = self._host + api_url

    params = {
        "order_id": order_id,
    }

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def calculate_exchange(self,
                       currency_to_get: str,
                       currency_to_spend: str,
                       currency_to_get_amount: str = None,
                       currency_to_spend_amount: str = None,
                       exchange_price: str = None) -> Dict:
    """
    Method, which calculates exchange
    :param currency_to_get: (required) currency that will be bought during the exchange
    :param currency_to_spend: (required) currency that will be sold during the exchange

    :param currency_to_get_amount: (optional) amount of currency that will be bought during the exchange
    :param currency_to_spend_amount: (optional) amount of currency that will be sold during the exchange
                                    Only one of the two amount parameters above must be specified.
                                    If currency_to_spend_amount is specified - this amount of the currency
                                    specified in currency_to_spend parameter will be sold.
                                    If currency_to_get_amount is specified - this amount of the currency
                                    specified in currency_to_get parameter will be bought.

    :param exchange_price: (optional) used for limit exchange order only
    :return: Dict
    """
    method = 'GET'
    api_url = '/api/v1/exchange/calculate'
    path = self._host + api_url

    params = {
        "currency_to_get": currency_to_get,
        "currency_to_spend": currency_to_spend,
        "currency_to_get_amount": currency_to_get_amount,
        "currency_to_spend_amount": currency_to_spend_amount,
        "exchange_price": exchange_price,
    }

    params = {key: value for key, value in params.items() if value}

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)
