from database import cursor, commit
from os import system
from time import sleep

# Globals
clear = lambda : system('clear')

# Database Operations:
def create_transaction(amount, description, t_option):
    clear()
    is_debit = True
    if(t_option == 1):
        is_debit = False
    else:
        is_debit = True

    # Based on is_debit minus is added 
    amount = -abs(amount) if is_debit else amount

    sql = ("INSERT INTO transactions(amount, description) VALUES(%s, %s)")
    cursor.execute(sql, (amount, description,))
    commit()

def get_balance():
    sql = ("SELECT SUM(amount) FROM transactions")
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]

def show_balances():
        print(f'1. Today\n2. Show Balance\n3. Exit\n')

option = 0
while option != 3:
    print(f'1. Transaction\n2. Show Balance\n3. Exit\n')
    try:
        option = int(input("Enter option : "))
        if option == 1:
            print('1. Credit\n2. Debit\n ')
            t_option = int(input("Select: "))
            amount = float(input('Amount : '))
            description = input('Description : ')
            create_transaction(amount, description, t_option)
            clear()
            t_message = "Credited" if t_option == 1 else "Debited"
            print("{} amount {}".format(t_message, amount))
        elif option == 2:
            print("Showing balance: {:.2f}".format(get_balance()))
        elif option == 3:
            print("Exiting...")
            sleep(0.5)
            clear()
    except:
        print('Sorry I cannot understand')