from typing import Dict


def create_internal_movement(self,
                             currency: str,
                             amount: str,
                             destination_account_email: str,
                             comment: str = None,
                             callback_url: str = None) -> Dict:
    """
    Creates internal movement order
    :param currency: (required) currency name
    :param amount: (required) transaction amount
    :param destination_account_email: (required) email of the user to whose account the funds will be moved
    :param comment: (optional) a comment that will be shown to the recipient and received in callback
    :param callback_url: (optional) url for order's status notifications
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/internal_movement'
    path = self._host + api_url

    params = {
        "currency": currency,
        "destination_account_email": destination_account_email,
        "comment": comment,
        "amount": amount,
        "callback_url": callback_url
    }

    params = {key: value for key, value in params.items() if value}
    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def repeat_internal_movement(self,
                             order_id: str,
                             amount: float = None) -> Dict:
    """
    Repeats previous internal movement order (if it is finished)
    with the same parameters (and optionally - new amount)
    :param order_id: (required) order ID of previously finished internal movement
    :param amount: (optional) if specified, this new amount will be used in the order
    :return: Dict
    """

    method = 'POST'
    api_url = '/api/v1/internal_movement/repeat'
    path = self._host + api_url

    params = {
        "order_id": order_id,
        "amount": amount
    }

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)
