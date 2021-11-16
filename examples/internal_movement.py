from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = ''

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def create_internal_movement(currency='UAH',
                             amount='10',
                             destination_account_email='my_mail@mail.com'
                             ) -> str:
    """
    Creates internal movement order
    :param currency: order currency
    :param amount: transaction amount
    :param destination_account_email: email of the user to whose account the funds will be moved
    :return: order ID
    """

    result = pay.create_internal_movement(currency=currency,
                                          amount=amount,
                                          destination_account_email=destination_account_email)
    return result.get('order_id')


def create_internal_movement_with_callback(currency='UAH',
                                           amount='10',
                                           destination_account_email='my_mail@mail.com',
                                           callback_url='https://my_host.com/for_callbacks'
                                           ) -> str:
    """
    Creates internal movement order with custom callback_url for notifications about order's status
    :param currency: order currency
    :param amount: transaction amount
    :param destination_account_email: email of the user to whose account the funds will be moved
    :param callback_url: url for notifications about order's status
    :return: order ID
    """

    result = pay.create_internal_movement(currency=currency,
                                          amount=amount,
                                          destination_account_email=destination_account_email,
                                          callback_url=callback_url)
    return result.get('order_id')


def repeat_internal_movement(order_id='your-unique-order-id'
                             ) -> str:
    """
    Repeats previous internal movement order (if it is finished) with the same parameters.
    :param order_id: order ID of previously finished internal movement
    :return: order ID
    """

    result = pay.repeat_internal_movement(order_id=order_id)

    return result.get('order_id')


def repeat_internal_movement_custom_amount(order_id='your-unique-order-id',
                                           amount='11'
                                           ) -> str:
    """
    Repeats previous internal movement order (if it is finished) with the same parameters but with the new amount
    :param order_id: order ID of previously finished internal movement
    :param amount: custom amount
    :return: order ID
    """

    result = pay.repeat_internal_movement(order_id=order_id,
                                          amount=amount)

    return result.get('order_id')
