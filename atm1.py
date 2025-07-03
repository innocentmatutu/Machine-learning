def debit(deposit,funds):
    funds.append({'Deposit': deposit})

def credit(withdrawal,funds):
    funds.append({'Withdrawal': withdrawal})

def get_balance(funds):
    return sum(item.get('Deposit', 0) - item.get('Withdrawal', 0) for item in funds)


def main():
    funds = []
    while True:
        print('\nAccount activity:')
        print('\n1.Deposit')
        print('\n2.Withdrawal')
        print('\n3.Balance')
        print('\n4.Exit')


        choice = input('Enter your choice:')

        if choice == '1':
            deposit = float(input('Enter your amount: '))
            if deposit <= 0:
                print('Enter a valid amount')
            else:
                debit(deposit,funds)
        
        elif choice == '2':
            withdrawal = float(input('Enter the amount you wish to withdraw: '))
            current_balance = get_balance(funds)
            if withdrawal <= 0:
                print('Enter a valid amount')

            elif withdrawal > current_balance:
                print('insufficient funds')

            else:
                credit(withdrawal,funds)
        
        elif choice == '3':
            print('Current balance is:', get_balance(funds))

        elif choice == '4':
            print('Exiting the program')
            break
        
        else:
            print('Enter the choice between 1 and 4')

main()