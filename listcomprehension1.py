def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_char_case_list = []
    
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            convert_to_lower ='_' + char.lower()
            snake_char_case_list.append(convert_to_lower)
        else:
            snake_char_case_list.append(char)
    snake_cased_string = ''.join(snake_char_case_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

def main():
    print(convert_to_snake_case('aLongAndComplexString'))
main()