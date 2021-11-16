from enum import Enum


class OrderStatusEnum(Enum):
    STATUSES = ("NEW", "ERROR", "CLOSED", "EXPIRED", "CANCELLED", "CANCELLING",
                "WAITING_FOR_CONFIRMATION", "PAYMENT_IN_PROGRESS",
                "WAITING_FOR_PRICE", "BLOCKED")


class OrderTypeEnum(Enum):
    TYPES = ("DEPOSIT", "EXCHANGE", "INTERNAL_MOVEMENT",
             "WITHDRAWAL", "FAST_EXCHANGE", "INVOICE")


class InvoicePaymentTypeEnum(Enum):
    TYPES = ("COINPAY", "FIAT", "CRYPTO", "ALL")


class ManyPaymentMethodCurrencyEnum(Enum):
    PAYMENT_METHOD_DICT = {
        "USDT": ["ERC20", "TRC20"]
    }
