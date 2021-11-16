from typing import Dict

from kauripay.api import API


class KauriPay(API):

    def __init__(self,
                 api_key: str,
                 api_secret: str,
                 host: str,
                 timeout: int = None,
                 proxies: Dict = None):
        super().__init__(api_key, api_secret, host, timeout, proxies)

    # CURRENCY METHODS
    from kauripay.processing.currency import get_currencies

    # DEPOSIT METHODS
    from kauripay.processing.deposit import _generate_deposit_address
    from kauripay.processing.deposit import generate_fiat_deposit_address
    from kauripay.processing.deposit import generate_crypto_deposit_address

    # EXCHANGE METHODS
    from kauripay.processing.exchange import create_exchange
    from kauripay.processing.exchange import calculate_exchange
    from kauripay.processing.exchange import repeat_exchange
    from kauripay.processing.exchange import cancel_exchange

    # EXCHANGE RATE METHODS
    from kauripay.processing.exchange_rate import get_exchange_rate

    # INTERNAL MOVEMENT METHODS
    from kauripay.processing.internal_movement import create_internal_movement
    from kauripay.processing.internal_movement import repeat_internal_movement

    # INVOICE METHODS
    from kauripay.processing.invoice import create_invoice
    from kauripay.processing.invoice import pay_invoice
    from kauripay.processing.invoice import pay_public_invoice

    # PAIR METHODS
    from kauripay.processing.pair import get_pairs

    # ORDERS METHODS
    from kauripay.processing.orders import get_order_details
    from kauripay.processing.orders import get_orders_history

    # USER METHODS
    from kauripay.processing.user import set_account_setting
    from kauripay.processing.user import get_account_info
    from kauripay.processing.user import get_balance

    # WITHDRAWAL METHODS
    from kauripay.processing.withdrawal import create_withdrawal
    from kauripay.processing.withdrawal import repeat_withdrawal
