# let's go get some software that someone else wrote

import luhn

# a function that uses the 'luhn' code = it takes a 'card_number' and returns 'true' or 'false' if the card is valid

def is_credit_card_valid(card_number):
    return luhn.verify(card_number)

#Let's tell the world whose awful credit card validator this is.

print("David Jason Bowlby Credit Card Validator")

#Let's get the card number from the user

card_number = input("Enter your 16-digit credit card number: ")

# Validate the credit card number using the Luhn algorithm

if is_credit_card_valid(card_number):     # we are calling the function above and sending it the card_number is validate

    print("The credit card number is valid.")

else:

    print("The credit card number is invalid.")


