def enter_expense(expenses,amount,category):
    expenses.append({'Amount':amount, 'Category':category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["Amount"]}, Category: {expense["Category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense:expense["Amount"],expenses))

def filter_by_category(expenses,category):
    return filter(lambda expense:expense["Category"] == category,expenses)

def main():
    expenses = []
    while True:
        print('Expense Tracker')
        print('1. Enter the expense:')
        print('2. Print the expense:')
        print('3. Calculate total expenses:')
        print('4. Filter the expenses')
        print('5. Exit')

        choice = input('Enter expense tracker choice:')


        if choice == '1':
            amount = float(input('Enter the amount:'))
            category = input('Enter the category:')
            enter_expense(expenses,amount,category)

        elif choice == '2':
            print('\nAll expenses:',print_expenses(expenses))

        elif choice == '3':
            print('\nTotal expense:', total_expenses(expenses))


        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('\nExiting program')
            break
                
    
main()