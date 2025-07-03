def add_expenses(expenses,amount,category):
    expenses.append({'Amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["Amount"]},Category: {expense["category"]}' )

def total_expenses(expenses):
    return sum(map(lambda expense:expense['Amount'],expenses))

def filter_expense_by_category(expenses,category):
    return filter(lambda expense:expense['category'] == category,expenses)

def main():
    expenses = []
    while True:
        print('\nExpense tracker')
        print('1. Add an expense')
        print('2. List total expenses')
        print('3. Show total expenses')
        print('4. Filter expense by category')
        print('5. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            amount = input('Enter the amount: ')
            category = input('Enter the category: ')
            add_expenses(expenses,amount,category)
        

        if choice == '2':
            print('\nAll expenses:',print_expenses(expenses))

        if choice == '3':
            print('\nTotal expense:',total_expenses(expenses))

        if choice == '4':
            category = input('Enter expense category:')
            print(f'\nExpense for {category}:', filter_expense_by_category(expenses,category))
           # print(filter_expense_by_category(expense,category))

        if choice == '5':
            print("\nExiting program")
        break

main()