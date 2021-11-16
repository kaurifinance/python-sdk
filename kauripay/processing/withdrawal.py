from typing import Dict


def create_withdrawal(self,
                      currency: str,
                      amount: str,
                      wallet_to: str,
                      withdrawal_email: str,
                      payment_method: str = None,
                      callback_url: str = None,
                      comment: str = None) -> Dict:
    """
    Creates withdrawal order
    :param currency: (required) currency name
    :param amount: (required) withdrawal amount
    :param wallet_to: (required) withdrawal destination - payment card number for fiat,
                        crypto wallet address for cryptocurrencies,
                        IBAN and other details for SEPA etc
    :param withdrawal_email: (required) user's email
    :param payment_method: (optional) specify this param when currency has more than one blockchain.
    E.g. if currency == 'USDT' payment_method can be 'ERC20', 'TRC20, 'BEP20'
    :param callback_url: (optional) url for order's status notifications
    :param comment: (optional) a comment that will be received in callback
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/withdrawal'
    path = self._host + api_url

    params = {
        "currency": currency,
        "payment_method": payment_method,
        "callback_url": callback_url,
        "amount": amount,
        "additional_info": {
            "withdrawal_email": withdrawal_email},
        "withdrawal_type": "GATEWAY",
        "comment": comment,
        "wallet_to": wallet_to
    }

    params = {key: value for key, value in params.items() if value}

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def repeat_withdrawal(self,
                      order_id: str,
                      amount: float = None) -> Dict:
    """
    Repeats previous withdrawal order (if it is finished)
    with the same parameters (and optionally - new amount).
    :param order_id: (required) order ID of previously finished withdrawal
    :param amount: (optional) if specified, this new amount will be used in the order
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/withdrawal/repeat'
    path = self._host + api_url

    params = {
        "order_id": order_id,
        "amount": amount,
    }

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)
