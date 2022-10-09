from datetime import date
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
    transaction_type = "Debit" if amount < 0 else "Credit"

    sql = ("INSERT INTO transactions(amount, description, type) VALUES(%s, %s, %s)")
    cursor.execute(sql, (amount, description,transaction_type,))
    commit()

def get_balance():
    sql = ("SELECT SUM(amount) FROM transactions")
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]

def get_transactions_by_filter(filter):
    date_query = ""
    base_query = (
            "SELECT ABS(amount), description FROM transactions t "
            "WHERE t.type='Debit' AND t.created_at "           
        )
    order_by = (" ORDER BY t.created_at DESC")

    # Date Query based on Fiter
    if filter == "Today":
        date_query = (
                "BETWEEN CONCAT(CURRENT_DATE(), ' 00:00:00')"
                "AND CONCAT(CURRENT_DATE(), ' 23:59:59')"
            )
    elif filter == "Yesterday":
        date_query = (
                "BETWEEN CONCAT(DATE_SUB(CURDATE(), INTERVAL 1 DAY),' 00:00:00')"
                "AND CONCAT(DATE_SUB(CURDATE(), INTERVAL 1 DAY),' 23:59:59')"
            )
    elif filter == "This Week":
        date_query = (
                "BETWEEN CONCAT(DATE_SUB(CURDATE(), INTERVAL 7 DAY),' 00:00:00')"
                "AND CONCAT(DATE_SUB(CURDATE(), INTERVAL 7 DAY),' 23:59:59')"
            )

    # Query
    sql = base_query+date_query+order_by
    cursor.execute(sql)

    # Results
    results = cursor.fetchall()
    print("--- --- ---")
    if len(results) == 0:
        print("No records")
    for result in results:
        print("{} - {}".format(result[0], result[1]))
    print("--- --- ---")



def show_balances():
        balance_option = 0
        while balance_option != 4:
            print(f'1. Today\n2. Yesterday\n3. This Week\n4. Exit to Main menu')
            balance_option = int(input("Enter option : "))
            try:
                if balance_option == 1:
                    # sql = ("SELECT SUM(ABS(amount)) FROM transactions t WHERE t.type = 'Debit'")
                    get_transactions_by_filter("Today")
                elif balance_option == 2:
                    get_transactions_by_filter("Yesterday")
                elif balance_option == 3:
                    get_transactions_by_filter("This Week")


            except Exception as err:
                print("Error {}".format(err))


option = 0
while option != 3:
    clear()
    # print("Today: ".format(date.today()))
    print(f'1. Commit Transaction\n2. Balance & Transactions\n3. Exit\n')
    try:
        option = int(input("Select : "))
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
            clear()
            print("Current Balance : {:.2f}".format(get_balance()))
            show_balances()
        elif option == 3:
            print("Exiting...")
            sleep(0.5)
            clear()
    except:
        print('Sorry I cannot understand')