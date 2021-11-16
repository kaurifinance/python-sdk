from typing import Dict


def get_order_details(self,
                      order_id: str) -> Dict:
    """
    Shows order details
    :param order_id: (required) order ID
    :return: Dict
    """
    method = 'GET'
    api_url = '/api/v1/orders/details'
    path = self._host + api_url

    params = {
        "order_id": order_id
    }

    signature = self._make_signature(method, api_url, params)

    response = self._make_request(method, path, signature, params=params)

    return response.get('order_details')


def get_orders_history(self,
                       page: str = None,
                       items_per_page: str = None,
                       order_type: str = None,
                       order_status: str = None,
                       order_sub_type: str = None,
                       from_timestamp: str = None,
                       till_timestamp: str = None,
                       currency: str = None,
                       address: str = None) -> Dict:
    """
    Shows orders' history for specified account

    Orders' history has pagination with 10 orders per page.

    :param page: (optional) page number
    :param items_per_page: (optional) how many items to show per page
    :param order_type: (optional) - Allowed values are ‘DEPOSIT’, ‘WITHDRAWAL’,
                                    ‘EXCHANGE’, ‘INTERNAL_MOVEMENT’, ‘INVOICE’.
    :param order_status: (optional)- Allowed values:
                                    "NEW", "ERROR", "CLOSED", "EXPIRED", "CANCELLED",
                                    "CANCELLING", "WAITING_FOR_CONFIRMATION",
                                    "PAYMENT_IN_PROGRESS", "WAITING_FOR_PRICE", "BLOCKED"
    :param order_sub_type: (optional) Allowed values: "GATEWAY", "CASHBOX", "BANK_COLLECTION", "SEPA"
    :param from_timestamp: (optional) filtering by time of order creation.
    :param till_timestamp: (optional) filtering by time of order creation.
    :param currency: (optional) filtering by currency
    :param address: (optional) deposit source - payment card number for fiat,
                               crypto wallet address for cryptocurrencies, IBAN and other details for SEPA etc
    :return: Dict
    """
    method = 'GET'
    api_url = '/api/v1/orders/history'
    path = self._host + api_url

    params = {
        "page": page,
        "limits": items_per_page,
        "order_type": order_type,
        "order_status": order_status,
        "order_sub_type": order_sub_type,
        "from_timestamp": from_timestamp,
        "till_timestamp": till_timestamp,
        "currency": currency,
        "address": address
    }

    params = {key: value for key, value in params.items() if value}

    signature = self._make_signature(method, api_url, params)

    return self._make_request(method, path, signature, params=params)
