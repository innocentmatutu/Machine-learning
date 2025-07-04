def multiply(a,b):
            return a*b

def addition(a,b):
            return a + b

def subtraction(a,b):
            return a - b

def modulus(a,b):
            return a % b

def power(a,b):
            return a ** b


while True:
    operand = input('Enter the operand(*,+,-,**,% ,q to quit): ')

    if operand.lower() == 'q':
           print('Exiting program')
           break

    elif operand in ('*','+','-','**','% '):
        first_number = float(input('Enter the first value: '))
        second_number = float(input('Enter the second value: '))

        if operand == '*':
            result = multiply(first_number,second_number)
    
        elif operand == '+':
            result = (addition(first_number,second_number))

        elif operand == '-':
            result = subtraction(first_number,second_number)
         
        elif operand == '%':
            result = modulus(first_number,second_number)
         
        elif operand == '**':
            result = power(first_number,second_number)
    
        print(f'\nAnswer is: {result}')
    
    else:
        print('Enter a valid operand')
        
 
