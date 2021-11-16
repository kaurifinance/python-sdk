from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = ''

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def create_withdrawal(currency='UAH',
                      amount='10',
                      wallet_to='1234123412341234',
                      withdrawal_email='my_mail@mail.com',
                      callback_url='https://my_host.com/for_callbacks'
                      ) -> str:
    """
    Creates withdrawal order with chosen currency and amount. Custom callback URL is used for notifications
    :param currency: withdrawal currency
    :param amount: amount to withdrawal
    :param wallet_to: withdrawal destination - payment card number for fiat,
                    crypto wallet address for cryptocurrencies,
                    IBAN and other details for SEPA etc
    :param withdrawal_email: user's email
    :param callback_url: url for order's status notifications
    :return: order ID
    """

    result = pay.create_withdrawal(currency=currency,
                                   amount=amount,
                                   wallet_to=wallet_to,
                                   withdrawal_email=withdrawal_email,
                                   callback_url=callback_url)
    return result.get('order_id')


def create_withdrawal_with_payment_method(currency='USDT',
                                          amount='10',
                                          payment_method='ERC20',
                                          wallet_to='1234123412341234',
                                          withdrawal_email='my_mail@mail.com',
                                          callback_url='https://my_host.com/for_callbacks'
                                          ) -> str:
    """
    Creates withdrawal order with chosen currency and amount. Custom callback URL is used for notifications
    :param currency: withdrawal currency
    :param amount: amount to withdrawal
    :param payment_method: you must specify this param if several blockchains are available for chosen currency.
    E.g. if currency == 'USDT' payment_method can be 'ERC20', 'TRC20, 'BEP20'
    :param wallet_to: withdrawal destination - payment card number for fiat,
                    crypto wallet address for cryptocurrencies,
                    IBAN and other details for SEPA etc
    :param withdrawal_email: user's email
    :param callback_url: url for order's status notifications
    :return: order ID
    """

    result = pay.create_withdrawal(currency=currency,
                                   amount=amount,
                                   payment_method=payment_method,
                                   wallet_to=wallet_to,
                                   withdrawal_email=withdrawal_email,
                                   callback_url=callback_url)
    return result.get('order_id')


def repeat_withdrawal(order_id='your-unique-order-id'
                      ) -> str:
    """
    Repeats previous withdrawal order (if it is finished) with the same parameters.
    :param order_id: order ID of previously finished withdrawal
    :return: order ID
    """

    result = pay.repeat_withdrawal(order_id=order_id)

    return result.get('order_id')


def repeat_withdrawal_custom_amount(order_id='your-unique-order-id',
                                    amount='11'
                                    ) -> str:
    """
    Repeats previous withdrawal order (if it is finished) with the same parameters
    but with the new amount
    :param order_id: order ID of previously finished withdrawal
    :param amount: custom amount
    :return: order ID
    """

    result = pay.repeat_withdrawal(order_id=order_id,
                                   amount=amount)

    return result.get('order_id')
