import helper_functions
import http.client
import os
import json

user_select = input('Do you have a specific cryptocurrency in your mind? \n 1. Yes \n 2. No \n').lower()

if(user_select == '1' or user_select == 'yes'):
    user_input = input('Enter a cryptocurrency to get latest info:').lower()
    helper_functions.user_selected_crypto(user_input)

else:
    if(user_select=='' or user_select!='no' and user_select!='2'):
        print(" Wrong option selected. Automatically showing top 10 currencies \n")
    else:
        print('Then choose one from the current top 10 cryptocurrencies \n')
    crypto_names = helper_functions.top_10_crypto()


    user_crypto_selection = (input('Which one would you like to know more about? \n')).lower()

    correct_selection = True
    while correct_selection:
        if user_crypto_selection.isdigit():
            index = int(user_crypto_selection)
            if 0 < index <= len(crypto_names):
                helper_functions.user_selected_crypto(crypto_names[index-1])
                correct_selection = False
            else:
                user_crypto_selection = input('Wrong input, please choose index between 1-10. \n').lower()


        # Check if user input matches a value
        elif user_crypto_selection in crypto_names:
            helper_functions.user_selected_crypto(user_crypto_selection)
            correct_selection = False

        else:
            user_crypto_selection = input('Wrong input, please enter valid index / name of crypto currency from the above to continue. \n').lower()


print('Success!!')