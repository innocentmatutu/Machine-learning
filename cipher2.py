message = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def decryp (text,key,direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_holder = 0
    final_message = ''

    for char in text.lower():
        if not char.isalpha():
             final_message += char
        else:
            key_char =key[key_holder % len(key)]
            key_holder += 1

            index_key = alphabet.find(key_char)
            index_message = alphabet.find(char)
            decryp_index = (index_message + index_key*direction) % len(alphabet)
            final_message += alphabet[decryp_index]
    return final_message

def decryption(message,custom_key):            
    return decryp(message,custom_key,-1)

def encryption(message,custom_key):
    return decryp(message,custom_key)
decrypted =decryption(message,custom_key)
print(f'Encrypted message: {message}')
print(f'custom key:{custom_key}')
print(f'Decrypted message is: {decrypted}')