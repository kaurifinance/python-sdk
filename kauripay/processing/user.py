from typing import Dict


def set_account_setting(self,
                        value: str,
                        name: str,
                        totp_code: str = None) -> Dict:
    """
    Updates the chosen account setting
    :param value: (required) setting's value
    :param name: (required) setting's name
    :param totp_code: (optional) code in TOTP form (time-based one-time password)
    :return: Dict
    """
    method = 'POST'
    api_url = '/api/v1/user/account/setting'
    path = self._host + api_url

    params = {
        "value": value,
        "name": name,
        "totp_code": totp_code
    }
    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)


def get_account_info(self) -> Dict:
    """
    Shows user's account information - fees, limits, processing rules, account settings etc
    :return: Dict
    """
    method = 'GET'
    api_url = '/api/v1/user/account_info'
    path = self._host + api_url

    signature = self._make_signature(method, api_url)

    return self._make_request(method, path, signature)


def get_balance(self) -> Dict:
    """
    Shows user's account balances and crypto wallets
    :return: Dict
    """
    method = 'GET'
    api_url = '/api/v1/user/balance'
    path = self._host + api_url

    signature = self._make_signature(method, api_url)

    return self._make_request(method, path, signature)
