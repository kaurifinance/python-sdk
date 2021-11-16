from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = ''

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def get_total_balance(view_currency='BTC') -> float:
    """
    Shows total balance for account in chosen currency
    :param view_currency: currency for total balance
    :return: total balance amount for account
    """
    result = pay.get_balance()
    balance_dict = result.get('balance')
    total = 0
    for currency in balance_dict:
        total += ((balance_dict.get(currency).get(view_currency).get('total')) +
                  (balance_dict.get(currency).get(view_currency).get('reserved')))
    return total


def get_balance_currency_converted_to_another_currency(base_currency='BTC',
                                                       view_currency='UAH') -> float:
    """
    Shows balance for chosen currency converted to the desired currency
    :param base_currency: currency, which amount will be shown converted
    :param view_currency: currency to which the amount to show will be converted
    :return: balance amount
    """
    result = pay.get_balance()
    if result['status'] == 'success':
        balance_dict = result.get('balance')
        balance = balance_dict.get(base_currency).get(view_currency).get('total')
        return balance


def get_processing_limits(order_type='WITHDRAWAL',
                          currency='ETH',
                          payment_method: str = None) -> tuple:
    """
    Shows limits for processing of chosen currency, depending on the order type
    :param order_type: choice from ('INTERNAL', 'WITHDRAWAL', 'INVOICE', 'DEPOSIT')
    :param currency: processing currency
    :param payment_method: you must specify this param if order_type == 'WITHDRAWAL' and
    if several blockchains are available for chosen currency.
    E.g. if currency == 'USDT' payment_method can be 'ERC20', 'TRC20, 'BEP20'
    :return: min_limit, max_limit
    """
    result = pay.get_account_info()
    if result['status'] == 'success':
        if order_type == 'INTERNAL':
            prefix = result['internal_movement_limits'][currency]
            min_limit = prefix.get('CROSS_ACCOUNT').get('min_amount')
            max_limit = prefix.get('CROSS_ACCOUNT').get('max_amount')
        elif order_type == 'WITHDRAWAL':
            prefix = result['withdrawal_order_limits'][currency]['GATEWAY']
            if payment_method:
                min_limit = prefix[payment_method].get('min_amount')
                max_limit = prefix[payment_method].get('max_amount')
            else:
                min_limit = prefix.get('min_amount')
                max_limit = prefix.get('max_amount')
        elif order_type == 'INVOICE':
            prefix = result['invoice_order_limits'][currency]
            min_limit = prefix['min_amount']
            max_limit = prefix['max_amount']
        elif order_type == 'DEPOSIT':
            prefix = result['deposit_order_limits'][currency]
            min_limit = prefix['GATEWAY']['P2P']['min_amount']
            max_limit = prefix['GATEWAY']['P2P']['max_amount']
        return min_limit, max_limit


def get_exchange_limits(currency_to_get='ETH',
                        currency_to_spend='UAH') -> tuple:
    """
    Shows limits for exchange of chosen currency pair
    :param currency_to_get: currency to buy
    :param currency_to_spend: currency to sell
    :return: min_limit, max_limit for "currency_to_spend"
    """
    result = pay.get_account_info()
    if result['status'] == 'success':
        pair = currency_to_get + '_' + currency_to_spend
        min_limit = result['exchange_order_limits'][pair]['min_amount']
        max_limit = result['exchange_order_limits'][pair]['max_amount']
        return min_limit, max_limit


def get_account_fees(order_type='withdrawal',
                     currency='UAH') -> tuple:
    """
    Shows fees for withdrawal or deposit of chosen currency
    :param order_type: choice from ("withdrawal", "deposit")
    :param currency: currency, for which fees will be shown
    :return: static_fee, percent_fee values
    """
    result = pay.get_account_info()
    if result['status'] == 'success':
        if order_type == 'withdrawal':
            data = result['withdrawal_order_fees'][currency]['GATEWAY']
        elif order_type == 'deposit':
            data = result['deposit_order_fees'][currency]['GATEWAY']['P2P']
        return data['static_fee'], data['percent_fee']


def get_crypto_account_wallet(cryptocurrency='BTC',
                              payment_method: str = None) -> str:
    """
    Shows the user's main wallet's address for chosen cryptocurrency
    :param cryptocurrency: currency, for which wallet will be shown
    :param payment_method: you must specify this param if several blockchains are available for chosen currency.
    E.g. if currency == 'USDT' payment_method can be 'ERC20', 'TRC20, 'BEP20'
    :return: wallet address
    """
    result = pay.get_balance()
    if result['status'] == 'success':
        if payment_method:
            address = result.get('wallets').get(cryptocurrency, {}).get(payment_method, {}).get('address')
        else:
            address = result.get('wallets').get(cryptocurrency, {}).get('address')
        return address
