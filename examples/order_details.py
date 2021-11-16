from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = ''

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def get_order_details_(order_id='your-own-order-id'):
    """
    Shows all information about the order
    :param order_id: order ID
    :return: order details Dict
    """
    result = pay.get_order_details(order_id=order_id)
    return result


def get_orders_history_withdrawal(order_type='WITHDRAWAL'):
    """
    Shows all WITHDRAWAL orders with information about them
    :param order_type: specifies the type of an order to search for in orders history
    :return: order details Dict with keys {'orders', 'pages_count'}
    """
    result = pay.get_orders_history(order_type=order_type)
    return result


def get_orders_history_success(order_status='CLOSED'):
    """
    Shows all orders having 'Success' order status (system name = 'CLOSED') with information about them
    :param order_status: order status system name
    :return: order details Dict with keys {'orders', 'pages_count'}
    """
    result = pay.get_orders_history(order_status=order_status)
    return result


def get_orders_history_currency(currency='BTC'):
    """
    Shows all orders with transactions in chosen currency and with information about them
    :param currency: currency name
    :return: dict with keys 'orders' and 'pages_count' (because pagination is used)
    """
    result = pay.get_orders_history(currency=currency)
    return result


def get_orders_history_deposit_address(order_type='DEPOSIT',
                                       address='my-address'):
    """
    Shows deposit orders with specific payment card or crypto-address and with information about them
    :param order_type: specifies the type of an order to search for in orders history
    :param address: payment card number or crypto wallet address
    :return: dict with keys 'orders' and 'pages_count' (because pagination is used)
    """
    result = pay.get_orders_history(order_type=order_type,
                                    address=address)
    return result


def get_orders_history_withdrawal_address(order_type='WITHDRAWAL',
                                          address='wife"s-visa-debit-card-number'):
    """
    Shows withdrawal orders with specific payment card or crypto-address and with information about them
    :param order_type: specifies the type of an order to search for in orders history
    :param address: payment card number or crypto wallet address
    :return: dict with keys 'orders' and 'pages_count' (because pagination is used)
    """
    result = pay.get_orders_history(order_type=order_type,
                                    address=address)
    return result
