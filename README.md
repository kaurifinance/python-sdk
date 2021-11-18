# KauriFinanceSDK

## Introduction

Kauri.Finance – EU licensed multifunctional investment and payment solution to enable any crypto operations for businesses and professional traders

## Requirements

This library requires Python version from 3.5 to 3.9.

Please note that this library also uses requests and certifi. These libraries' supported Python versions can differ from the versions supported by kauri_finance_sdk

## Installation
We recommend using [PyPI](https://pypi.org/project/kauri_finance_sdk/) to install the Kauri Finance Software Development Kit for Python.
```bash
$ pip install kauri_finance_sdk
```

## Usage
After the [registration](https://kauri.finance/auth/registration), api_key and api_secret will become available.
You can get them [here](https://kauri.finance/settings/api).
Please note that some features are fully available only after the [verification](https://kauri.finance/verification).

## Example
The [examples](examples) folder has basic and advanced examples.

Base api url - https://api.kauri.finance/
```python
from kauripay.processing import KauriPay

api_key = ''
api_secret = ''
host = 'https://api.kauri.finance/'

pay = KauriPay(api_key=api_key,
               api_secret=api_secret,
               host=host)


def get_total_balance(view_currency) -> float:
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
print(get_total_balance('BTC'))
```

## Documentation

Please see the [Documentation](https://github.com/kaurifinance/api-docs) for more details.

## Contact Us

- Website: https://kauri.finance
- Mail: support@kauri.finance
- Telegram BOT: https://t.me/kaurifinance_bot
- LinkedIn: https://www.linkedin.com/company/18495339
- Facebook: https://www.facebook.com/KAURIFinance-101252805245259

KAURIFINANCE OU Estonia,
Tallinn, Narva mnt. 7, V korrus

## License
Kauri Finance SDK for Python is licensed under MIT License.
