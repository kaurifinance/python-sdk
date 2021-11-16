from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = ''

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def get_exchange_rate_(currency_to_spend='USDT',
                       currency_to_get='BTC'
                       ) -> str:
    """
    Shows exchange rate for the specified currency pair. For example - USDT_BTC
    :param currency_to_spend: currency that will be sold, it goes first in the pair
    :param currency_to_get: currency that will be bought, it goes second in the pair
    :return: exchange rate
    """

    result = pay.get_exchange_rate()
    pair = currency_to_spend + '_' + currency_to_get
    return result.get(pair)
