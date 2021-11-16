from typing import Dict


def _generate_deposit_address(self,
                              currency: str,
                              deposit_email: str = None,
                              amount_to_spend: str = None,
                              amount_to_receive: str = None,
                              currency_convert_to: str = None,
                              fail_url: str = None,
                              success_url: str = None,
                              callback_url: str = None,
                              processing_url: str = None,
                              comment: str = None,
                              payment_method: str = None) -> Dict:
    """
    Creates deposit address
    :return: dict that contains: order ID ("external_id" key),
            link to payment page for fiat ("url" key),
            crypto wallet address as text ("addr" key)
            and as a QR code ("qr" key - image encoded in base64)
    """
    method = 'POST'
    api_url = '/api/v1/deposit/address'
    path = self._host + api_url

    params = {
        "currency": currency,
        "payment_type": "P2P",
        "payment_method": payment_method,
        "additional_info": {
            'deposit_email': deposit_email
        },
        "amount_to_receive": amount_to_receive,
        "amount_to_spend": amount_to_spend,
        "currency_convert_to": currency_convert_to,
        "fail_url": fail_url,
        "success_url": success_url,
        "callback_url": callback_url,
        "processing_url": processing_url,
        "comment": comment
    }

    params = {key: value for key, value in params.items() if value}

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def generate_fiat_deposit_address(self,
                                  currency: str,
                                  deposit_email: str,
                                  amount_to_spend: str = None,
                                  amount_to_receive: str = None,
                                  currency_convert_to: str = None,
                                  fail_url: str = None,
                                  success_url: str = None,
                                  callback_url: str = None,
                                  processing_url: str = None,
                                  comment: str = None) -> str:
    """
    Creates url for payment page for fiat deposit
    :param currency: (required) currency name, e.g.: 'UAH'
    :param deposit_email: (required) user's email

    :param amount_to_spend: (optional)
    :param amount_to_receive: (optional)
                            amount_to_spend, amount_to_receive - you need to specify one of these parameters.
                            In the first case, the fee will be subtracted from the amount, and in the second case,
                            the fee will NOT be subtracted from the amount, but charged separately from the card.
                            One of these fields must be used, but only for FIAT currencies deposit.

    :param currency_convert_to: (optional) currency that is being deposited can be converted on-the-fly
                                to the currency you specify
    :param fail_url: (optional) redirect URL for when deposit fails
    :param success_url: (optional) redirect URL for when deposit succeeds
    :param callback_url: (optional) url for order's status notifications
    :param processing_url: (optional) general case redirect URL to be used if the client doesn't want
                            or can't use redirects for separate fail and success cases
    :param comment: (optional) a comment that will be shown on the payment page and received in callback
    :return: payment page URL
    """
    result = self._generate_deposit_address(currency, deposit_email, amount_to_spend,
                                            amount_to_receive, currency_convert_to,
                                            fail_url, success_url, callback_url,
                                            processing_url, comment)

    return result.get("url")


def generate_crypto_deposit_address(self,
                                    currency: str,
                                    deposit_email: str,
                                    currency_convert_to: str = None,
                                    payment_method: str = None,
                                    callback_url: str = None) -> Dict:
    """
    Creates address for cryptocurrency deposit
    :param currency: (required) currency name, e.g: 'USDT'
    :param deposit_email: (required) user's email
    :param currency_convert_to: (optional) currency that is being deposited can be converted on-the-fly
                                to the currency you specify
    :param payment_method: (optional) specify this param when currency has more than one blockchain.
    E.g. if currency == 'USDT' payment_method can be 'ERC20', 'TRC20, 'BEP20'
    :param callback_url: (optional) url for order's status notifications
    :return: dict that contains: crypto wallet address as text ("addr" key)
            and as a QR code ("qr" key - image encoded in base64)
    """
    result = self._generate_deposit_address(currency, deposit_email,
                                            currency_convert_to,
                                            payment_method, callback_url)

    return {"address": result.get("addr"), "qr": result.get("qr")}
