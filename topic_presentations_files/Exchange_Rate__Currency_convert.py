__author__ = 'justino'

import sys
# from catapa_home_works.interface import exchange_rate_menu
import json
import requests

CURRENCIES_LIST = ["EUR", "USD", "AUD", "JPY",
                   "IDR"]  # available currencies list


def get_exchange_rate(base_currency, target_currency):
    """ Define general propose , takes 2 arguments, base currency and target currency
    """
    request_url = 'https://api.fixer.io/latest?base={}'.format(base_currency)
    respond = requests.get(request_url)
    exchange_rate_from_base_currency = json.loads(respond.content.decode('utf-8'))
    # print(json.dumps(exchange_rate_from_base_currency, indent=4))
    exchange_rate = exchange_rate_from_base_currency['rates'][target_currency]

    return exchange_rate


def base_and_target_currency_keys(data):
    """    Transform currency list into dictionary
    then return dict
    :param data:  currency list
    :return: dict
    """
    count = 1
    dict_base_target_currency = {}

    for i, base_currency in enumerate(data):
        for j, target_currency in enumerate(data):
            if base_currency != target_currency:
                dict_base_target_currency[count] = {"base_currency": base_currency, "target_currency": target_currency}
                count += 1
    return dict_base_target_currency


def get_available_currency_len(data):
    return len(data) * (len(data) - 1)


def quit_():
    """
    Exit and terminated program
    :return:
    """
    print("Thank you for using Your Exchange Rate Currency App.")
    sys.exit(0)


def currency_convert(currency_list):
    """ Create a general purpose currency convert. For a list of currencies (e.g ["EUR", "USD", "AUD", "JPY"])
    Allow user to convert to and from the currencies in the list.
    for example:
    A user can choose to convert Euros to Australian Dollar
    A user can choose to convert from USD to Euros."""

    available_currency_list = base_and_target_currency_keys(currency_list)
    exchange_rate_menu(available_currency_list)  # Create Menu
    print("=" * 40)

    while True:
        selected_option = input("Enter an available option (q exit.) : ")

        if selected_option == 'q':
            quit_()

        elif selected_option.isdigit() and int(selected_option) in range(1,
                                                                         get_available_currency_len(currency_list) + 1):
            selected_option = int(selected_option)
            amount_in_base = float(
                    input("Enter amount in {}: ".format(available_currency_list[selected_option]["base_currency"]))[:3]))

            result = amount_in_base * get_exchange_rate(available_currency_list[selected_option]["base_currency"],
                                                        available_currency_list[selected_option]['target_currency'])
            print("{} {} ===> {} = {}".format(round(amount_in_base, 2),
                                              available_currency_list[selected_option]["base_currency"],
                                              available_currency_list[selected_option]['target_currency'],
                                              round(result, 2)))
        else:
            print("Please select correct option!")
##########################################################################################################################


class Color:
	# Shell Coloring
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def exchange_rate_menu(option_list):
    """
    :param currency_list: list of available currency
    Display menu base on available currency list
    :return:
    """
    if isinstance(option_list, dict):
        print(Color.GREEN + "=" * 50)
        print("{0:<5} {1:>15}".format("OPTION", "DESCRIPTION"))
        print(Color.GREEN + "=" * 50)

        for key, value in option_list.items():
            print("{0:^5}{1:^10}===>{2:^10}".format(key, value['base_currency'], value['target_currency']))


# MAIN PROGRAM ##########################################################################################################
if __name__ == '__main__':
    currency_convert(CURRENCIES_LIST)
