from typing import Dict


def create_invoice(self,
                   currency: str,
                   amount: str,
                   payment_option: str,
                   pay_account_email: str,
                   additional_info: Dict = None,
                   comment: str = None) -> Dict:
    """
    Creates invoice order
    :param currency: (required) currency name
    :param amount: (required) invoice amount
    :param payment_option: (required) specifies allowed payment methods among: ALL, COINPAY, FIAT, CRYPTO.
                            Default value - ALL # TODO чи залишати параметр COINPAY - бо СДК має бути універсальним
    :param pay_account_email: (required) the email to which the invoice will be sent
    :param additional_info: (optional) Can include "callback_url", "success_url", "fail_url".
                            If "fail_url" is specified - user who pays the invoice
                            will be redirected to the specified page in case of unsuccessful payment
                            If "success_url" is specified - user who pays the invoice
                            will be redirected to the specified page in case of successful payment
    :param comment: (optional) a comment that will be shown on the payment page and received in callback
    :return: dict containing the payment link ("url" key), order ID, status
    """
    method = 'POST'
    api_url = '/api/v1/invoice/'
    path = self._host + api_url

    params = {
        "currency": currency,
        "pay_account_email": pay_account_email,
        "payment_option": payment_option,
        "amount": amount,
        "additional_info": additional_info,
        "comment": comment
    }
    params = {key: value for key, value in params.items() if value}
    print(params)
    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def pay_invoice(self,
                currency: str,
                order_id: str) -> Dict:
    """
    Enables authenticated users to pay the invoice order
    :param currency: (required) currency name
    :param order_id: (required) invoice order ID
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/invoice/pay'
    path = self._host + api_url

    params = {
        "currency": currency,
        "order_id": order_id
    }

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def pay_public_invoice(self,
                       currency: str,
                       order_id: str) -> Dict:
    """
    Enables non-authenticated users to pay the invoice order
    :param currency: (required) currency name
    :param order_id: (required) invoice order ID
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/invoice/pay/public'
    path = self._host + api_url

    params = {
        "currency": currency,
        "order_id": order_id
    }

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)
