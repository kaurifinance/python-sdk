from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = ''

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def calculate_exchange_spend_amount(currency_to_get='BTC',
                                    currency_to_spend='USDT',
                                    currency_to_get_amount='1') -> str:
    """
    Shows how much USDT will be spent for buying 1 BTC
    :param currency_to_get: currency that will be bought during the exchange
    :param currency_to_spend: currency that will be sold during the exchange
    :param currency_to_get_amount: amount of currency that will be bought during the exchange
    :return: amount of currency that will be sold during the exchange
    """

    result = pay.calculate_exchange(currency_to_get=currency_to_get,
                                    currency_to_spend=currency_to_spend,
                                    currency_to_get_amount=currency_to_get_amount)

    return result.get('currency_to_spend_amount')


def calculate_exchange_get_amount(currency_to_get='BTC',
                                  currency_to_spend='USDT',
                                  currency_to_spend_amount='1000') -> str:
    """
    Shows how much BTC will be bought when selling 1000 USDT
    :param currency_to_get: currency that will be bought during the exchange
    :param currency_to_spend: currency that will be sold during the exchange
    :param currency_to_spend_amount: amount of currency that will be sold during the exchange
    :return: amount of currency that will be sold during the exchange
    """

    result = pay.calculate_exchange(currency_to_get=currency_to_get,
                                    currency_to_spend=currency_to_spend,
                                    currency_to_spend_amount=currency_to_spend_amount)

    return result.get('currency_to_get_amount')


def create_market_exchange(currency_to_get='USDT',
                           currency_to_spend='BTC',
                           currency_to_spend_amount='1') -> str:
    """
    Creates exchange order to spend 1 BTC and buy USDT with MARKET price
    :param currency_to_get: currency that will be bought during the exchange
    :param currency_to_spend: currency that will be sold during the exchange
    :param currency_to_spend_amount: amount of currency that will be sold during the exchange
    :return: order ID
    """

    result = pay.create_exchange(currency_to_get=currency_to_get,
                                 currency_to_spend=currency_to_spend,
                                 currency_to_spend_amount=currency_to_spend_amount)
    return result.get('order_id')


def create_market_exchange_custom_callback(currency_to_get='USDT',
                                           currency_to_spend='BTC',
                                           currency_to_spend_amount='1',
                                           callback_url='https://my_host.com/for_callbacks') -> str:
    """
    Creates exchange order to spend 1 BTC and buy USDT with MARKET price.
    Custom callback URL is used for notifications about order's status.
    :param currency_to_get: currency that will be bought during the exchange
    :param currency_to_spend: currency that will be sold during the exchange
    :param currency_to_spend_amount: amount of currency that will be sold during the exchange
    :param callback_url: url for notifications about order's status
    :return: order ID
    """

    result = pay.create_exchange(currency_to_get=currency_to_get,
                                 currency_to_spend=currency_to_spend,
                                 currency_to_spend_amount=currency_to_spend_amount,
                                 callback_url=callback_url)
    return result.get('order_id')


def repeat_exchange(order_id='your-unique-order-id'
                    ) -> str:
    """
    Repeats previous exchange order (if it is finished) with the same parameters.
    :param order_id: order ID of previously finished exchange
    :return: order ID
    """

    result = pay.repeat_exchange(order_id=order_id)

    return result.get('order_id')


def create_limit_exchange(currency_to_get='USDT',
                          currency_to_spend='BTC',
                          currency_to_spend_amount='1',
                          exchange_price='100000'
                          ) -> str:
    """
    Creates exchange order to spend 1 BTC and buy USDT with custom LIMIT price.
    The order will be executed when market price = exchange price set by the order.
    :param currency_to_get: currency that will be bought during the exchange
    :param currency_to_spend: currency that will be sold during the exchange
    :param currency_to_spend_amount: amount of currency that will be sold during the exchange
    :param exchange_price: price for which the currency will be SOLD during the exchange
    :return: order ID
    """

    result = pay.create_exchange(currency_to_get=currency_to_get,
                                 currency_to_spend=currency_to_spend,
                                 currency_to_spend_amount=currency_to_spend_amount,
                                 exchange_price=exchange_price)
    return result.get('order_id')


def cancel_limit_exchange(order_id='your-unique-order-id'
                          ) -> str:
    """
    Cancels the exchange order.
    Only limit exchange order can be canceled and
    only if cancellation is allowed by processing rules
    and if the order is still being processed.
    :param order_id: (required) ID of the order to cancel
    :return: order ID
    """

    result = pay.cancel_exchange(order_id=order_id)

    return result.get('order_id')
