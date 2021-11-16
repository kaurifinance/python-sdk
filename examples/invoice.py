from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = ''

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def create_invoice_all_methods(currency='UAH',
                               amount='1000',
                               payment_option='ALL',
                               pay_account_email='my_email@mail.com'):
    """
    Creates invoice with all payment methods allowed
    :param currency: currency name
    :param amount: invoice amount
    :param payment_option: specifies allowed payment methods
    :param pay_account_email: the email to which the invoice will be sent
    :return: dict containing the link to payment page ("url" key) and order ID
    """

    result = pay.create_invoice(currency=currency,
                                amount=amount,
                                payment_option=payment_option,
                                pay_account_email=pay_account_email)
    return {'url': result.get('url'), 'order_id': result.get('order_id')}


def create_invoice_fiat(currency='UAH',
                        amount='1000',
                        payment_option='FIAT',
                        pay_account_email='my_email@mail.com'):
    """
    Creates invoice with only FIAT payment method allowed
    :param currency: currency name
    :param amount: invoice amount
    :param payment_option: specifies allowed payment methods
    :param pay_account_email: the email to which the invoice will be sent
    :return: dict containing the link to payment page ("url" key) and order ID
    """

    result = pay.create_invoice(currency=currency,
                                amount=amount,
                                payment_option=payment_option,
                                pay_account_email=pay_account_email)
    return {'url': result.get('url'), 'order_id': result.get('order_id')}
