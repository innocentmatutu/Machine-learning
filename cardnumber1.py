card_number = input('Enter your card number: ')


def verification(translated_card):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    card_number_reversed =translated_card[::-1]
    odd_digits = card_number_reversed[::2]
    even_digits = card_number_reversed[1::2]

    for digits in odd_digits:
        sum_of_odd_digits +=int(digits)

    for digits in even_digits:
        total = int(digits) * 2

        if total >= 10:
            total =(total % 10) + (total // 10)
        sum_of_even_digits += total
    sum = sum_of_even_digits + sum_of_even_digits
    return sum % 10 == 0

def translating(number):
    card_translation = str.maketrans({'-':'',' ':''})
    translated_card = number.translate(card_translation)

    
    if verification(translated_card):
        print('VALID')
    else:
        print('INVALID')
translating(card_number)