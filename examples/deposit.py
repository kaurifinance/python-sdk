from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = ''

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def generate_crypto_deposit_address(cryptocurrency='BTC',
                                    deposit_email='my_mail@mail.com',
                                    callback_url='https://my_host.com/for_callbacks') -> str:
    """
    Generates a new deposit address for chosen cryptocurrency
    with custom callback_url for notifications
    :param cryptocurrency: cryptocurrency name
    :param deposit_email: user's email
    :param callback_url: url for order's status notifications
    :return: str type new deposit address
    """
    result = pay.generate_crypto_deposit_address(currency=cryptocurrency,
                                                 deposit_email=deposit_email,
                                                 callback_url=callback_url)
    address = result.get('address')
    return address


def generate_crypto_deposit_address_with_payment_method(cryptocurrency='USDT',
                                                        payment_method='ERC20',
                                                        deposit_email='my_mail@mail.com',
                                                        callback_url='https://my_host.com/for_callbacks') -> str:
    """
    Generates a new deposit address for chosen cryptocurrency
    with custom callback_url for notifications
    :param cryptocurrency: cryptocurrency name
    :param deposit_email: user's email
    :param payment_method: you must specify this param if several blockchains are available for chosen currency.
    E.g. if currency == 'USDT' payment_method can be 'ERC20', 'TRC20, 'BEP20'
    :param callback_url: url for order's status notifications
    :return: str type new deposit address
    """
    result = pay.generate_crypto_deposit_address(currency=cryptocurrency,
                                                 deposit_email=deposit_email,
                                                 payment_method=payment_method,
                                                 callback_url=callback_url)
    address = result.get('address')
    return address


def generate_crypto_address_with_currency_convert(base_cryptocurrency='BTC',
                                                  deposit_email='my_mail@mail.com',
                                                  currency_convert_to='USDT') -> str:
    """
    Generates a new deposit address for chosen cryptocurrency
    with auto convert to desired currency
    :param base_cryptocurrency: cryptocurrency that will be sent to the deposit address and will be converted
    :param deposit_email: user's email
    :param currency_convert_to: cryptocurrency into which the funds will be converted
    :return: str type new deposit address
    """
    result = pay.generate_crypto_deposit_address(currency=base_cryptocurrency,
                                                 deposit_email=deposit_email,
                                                 currency_convert_to=currency_convert_to)
    address = result.get('address')
    return address


def generate_payment_link_with_amount_to_spend(currency='UAH',
                                               deposit_email='my_mail@mail.com',
                                               amount_to_spend='1000') -> str:
    """
    Generates URL for deposit of chosen fiat currency. Chosen amount will be charged.
    Chosen amount_to_spend minus the fee will be deposited to account.
    :param currency: currency to deposit
    :param deposit_email: email of user to whose account the deposit is made
    :param amount_to_spend: amount to deposit - the fee will be subtracted from it
    :return: URL for deposit payment page
    """
    result_url = pay.generate_fiat_deposit_address(currency=currency,
                                                   deposit_email=deposit_email,
                                                   amount_to_spend=amount_to_spend)
    return result_url


def generate_payment_link_with_amount_to_receive(currency='UAH',
                                                 deposit_email='my_mail@mail.com',
                                                 amount_to_receive='1000') -> str:
    """
    Generates URL for deposit of chosen fiat currency.
    Chosen amount_to_receive plus the fee will be charged from the card.
    Chosen amount_to_receive will be deposited to account.
    :param currency: currency to deposit
    :param deposit_email: email of user to whose account the deposit is made
    :param amount_to_receive: amount to deposit - the fee will NOT be subtracted from it,
                              but charged separately from the card
    :return: URL for deposit payment page
    """
    result_url = pay.generate_fiat_deposit_address(currency=currency,
                                                   deposit_email=deposit_email,
                                                   amount_to_receive=amount_to_receive)
    return result_url


def generate_payment_link_with_redirect_urls(currency='UAH',
                                             deposit_email='my_mail@mail.com',
                                             amount_to_receive='1000',
                                             fail_url='https://my_host.com/fail_paid_url/',
                                             success_url='https://my_host.com/success_paid_url/',
                                             processing_url='https://my_host.com/processing_url/', ) -> str:
    """
    Generates payment URL for deposit of chosen currency.
    Custom redirect URLs for fail and success cases are used.
    The general case processing_url is retained, to be used
    if the client doesn't want or can't use redirects for separate fail and success cases.
    :param currency: currency to deposit
    :param deposit_email: email of user to whose account the deposit is made
    :param amount_to_receive: amount to deposit - the fee will NOT be subtracted from it,
                              but charged separately from the card
    :param fail_url: redirect URL for when deposit fails
    :param success_url: redirect URL for when deposit succeeds
    :param processing_url: general case redirect URL to be used if the client doesn't want
                            or can't use redirects for separate fail and success cases
    :return: URL for deposit payment page
    """
    result_url = pay.generate_fiat_deposit_address(currency=currency,
                                                   deposit_email=deposit_email,
                                                   amount_to_receive=amount_to_receive,
                                                   fail_url=fail_url,
                                                   success_url=success_url,
                                                   processing_url=processing_url)
    return result_url


def generate_payment_link_with_custom_callback_url(currency='UAH',
                                                   deposit_email='my_mail@mail.com',
                                                   amount_to_receive='1000',
                                                   callback_url='https://my_host.com/callback_url/',
                                                   ) -> str:
    """
    Generates payment URL for deposit of chosen currency.
    Custom callback URL is used for notifications
    :param currency: currency to deposit
    :param deposit_email: email of the user to whose account the deposit is made
    :param amount_to_receive: amount to deposit - the fee will NOT be subtracted from it,
                              but charged separately from the card
    :param callback_url: url for order's status notifications
    :return: URL for deposit payment page
    """
    result_url = pay.generate_fiat_deposit_address(currency=currency,
                                                   deposit_email=deposit_email,
                                                   amount_to_receive=amount_to_receive,
                                                   callback_url=callback_url)
    return result_url
