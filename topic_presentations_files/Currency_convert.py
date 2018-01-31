#!/usr/bin/env python

# coding: utf-8

# ## Converts USD to EURO or from EURO to USD

# In[20]:


import requests
import json

def get_exchange_rates(base_currency, target_currency):

    request_url = 'https://api.fixer.io/latest?base={}'.format(base_currency)
    request = requests.get(request_url)
    conversion_from_base_currency= json.loads(request.content.decode('utf-8'))
    conversion_rate = conversion_from_base_currency['rates'][target_currency]

    return conversion_rate




def CurrencyConvert():

    # Find out what the user wants to convert. 1) USD  to Euro or 2) Euro to USD.
    # Store answer into variable.
    userChoice = input("What do you want to convert? \n1) USD > EURO \n2) EURO > USD \n3) AUD > EUR \n4) EURO > AUD \n5) USD > AUD \n6) AUD > USD ")

    conversion_from_EUR_to_USD = get_exchange_rates("EUR", "USD")
    conversion_from_USD_to_EUR = get_exchange_rates("USD", "EUR")

    conversion_from_AUD_to_EUR = get_exchange_rates("AUD", "EUR")
    conversion_from_EUR_to_AUD = get_exchange_rates("EUR", "AUD")

    conversion_from_USD_to_AUD = get_exchange_rates("USD", "AUD")
    conversion_from_AUD_to_USD = get_exchange_rates("AUD", "USD")

    # Check and see what the typed.
    # If the user typed 1
    if userChoice == "1":
        # Prompt the user the amount of the USD they want to convert
        # Store what the user typed into a variable
        userUSD = float(input("Enter the amount in USD you wish to convert \n"))

        EUR = (userUSD) * conversion_from_USD_to_EUR
        # Out amount to the user.
        print ("$ %0.2f" %userUSD, "= %0.2f" %EUR, "Euro")
        print ("----------------------------------------")
        doAgain()

    # If the user typed 2
    elif userChoice == "2":
        # Prompt the user the amount of the USD they want to convert
        # Store what the user typed into a variable
        userEuro = float(input("Enter the amount in Euro you wish to convert \n"))

        USD = (userEuro) * conversion_from_EUR_to_USD
         # Out amount to the user.
        print ("%0.2f" %userEuro, "Euro = $ %0.2f" %USD)
        print ("----------------------------------------")
        doAgain()

    # If the user typed 3
    elif userChoice == "3":
        # Prompt the user the amount of the USD they want to convert
        # Store what the user typed into a variable
        userAUD = float(input("Enter the amount in AUD you wish to convert \n"))

        EUR = (userAUD) * conversion_from_AUD_to_EUR
         # Out amount to the user.
        print ("%0.2f" %userAUD, "AUD = %0.2f" %EUR, "EUR")
        print ("----------------------------------------")
        doAgain()

    elif userChoice == "4":
        # Prompt the user the amount of the USD they want to convert
        # Store what the user typed into a variable
        userEUR = float(input("Enter the amount in EUR you wish to convert \n"))

        AUD = (userEUR) * conversion_from_EUR_to_AUD
         # Out amount to the user.
        print ("%0.2f" %userEUR, "EUR = %0.2f" %AUD, "AUD")
        print ("----------------------------------------")
        doAgain()

    elif userChoice == "5":
        # Prompt the user the amount of the USD they want to convert
        # Store what the user typed into a variable
        userUSD = float(input("Enter the amount in USD you wish to convert \n"))

        AUD = (userUSD) * conversion_from_USD_to_AUD
         # Out amount to the user.
        print ("$ %0.2f" %userUSD, "USD = %0.2f" %AUD, "AUD")
        print ("----------------------------------------")
        doAgain()

    elif userChoice == "6":
        # Prompt the user the amount of the USD they want to convert
        # Store what the user typed into a variable
        userAUD = float(input("Enter the amount in AUD you wish to convert \n"))

        USD = (userAUD) * conversion_from_AUD_to_USD
         # Out amount to the user.
        print ("%0.2f" %userAUD, "AUD = $ %0.2f" %USD)
        print ("----------------------------------------")
        doAgain()

    # If the user typed anything else
    else:
        # Tell the user what they did wrong.
        print("Error: You entered invalid information, please try again")
        # Run the script again.
        CurrencyConvert()

def doAgain():
    # Prompts the user if they would to run the convert currency program again
    userDoAgain = input("Would do you like to convert again? \n1) Yes \n2) No \n")

    # Check what the user typed.
    # If choice was 1
    if userDoAgain == "1":
        CurrencyConvert()
    # If choice was 1
    elif userDoAgain == "2":
        print ("Thank do you for using this program")
    # If choice was anything else
    else:
        print("Error: You entered invalid information, please try again")
        doAgain()


if __name__ == '__main__':
    CurrencyConvert()
