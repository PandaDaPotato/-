# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define  clear function
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
# Welcome screen
print('Welcome to the Bank of Python!')
input('Press Enter to continue...')
clear()


flag = True
balance = 300

def atm():
    global balance
    balance = balance
# Directory aka Main Menu
    print('Here is the directory:')
    directory = input('1. Withdraw \n2. Deposit \n3. Fast Cash \n4. Balance\n')
    clear()
# loop
    while flag == True:
# Withdraw    
        if directory == "1":
            print("How much would you like to Withdraw?")
            withdrawamount = input('$')
            if balance < int(withdrawamount):
                print('Insufficient funds!')
                continue

            elif balance >= int(withdrawamount):
                balance = balance - int(withdrawamount)
                print('\nWithdrawing $'+ withdrawamount + '...\n')
                print('Please take your card and cash from below.')
                print('\nYour current balance is: $' + str(balance))
                sleep(5)
                break
                clear()
# Deposit
        elif directory == "2":
            print("How much would you like to Deposit?")
            depositamount = input('$')
            print('\nDepositing $'+ depositamount + '...\n')
            print('Please take your card from below.')
            balance = balance + int(depositamount)
            print('\nYour current balance is: $' + str(balance))
            sleep(5)
            break
            clear()
            continue 
# Fast Cash
        elif directory == "3":
            print("Choose amount you would like to Withdraw:\n1. $10\n2. $20\n3. $50\n4. $100\n5. Custom amount")
            fastamount = input('')
    # $10
            if fastamount == "1":
                if balance < 10:
                    print('Insufficient funds!')
                    continue

                elif balance >= 10:
                    print('\nWithdrawing $10...\n')
                    print('Please take your card and cash from below.')
                    balance = balance - int(10)
                    print('\nYour current balance is: $' + str(balance))
                    sleep(5)
                    break
                    clear()
    # $20
            elif fastamount == "2":
                if balance < 20:
                    print('Insufficient funds!')
                    continue

                elif balance >= 20:
                    print('\nWithdrawing $20...\n')
                    print('Please take your card and cash from below.')
                    balance = balance - int(10)
                    print('\nYour current balance is: $' + str(balance))
                    sleep(5)
                    break
                    clear()
    # $50
            elif fastamount == "3":
                if balance < 50:
                    print('Insufficient funds!')
                    continue

                elif balance >= 50:
                    print('\nWithdrawing $50...\n')
                    print('Please take your card and cash from below.')
                    balance = balance - int(10)
                    print('\nYour current balance is: $' + str(balance))
                    sleep(5)
                    break
                    clear()
    # $100    
            elif fastamount == "4":
                if balance < 100:
                    print('Insufficient funds!')
                    continue

                elif balance >= 100:
                    print('\nWithdrawing $100...\n')
                    print('Please take your card and cash from below.')
                    balance = balance - int(10)
                    print('\nYour current balance is: $' + str(balance))
                    sleep(5)
                    break
                    clear()
                    
    # Custom
            elif fastamount == "5":
                customfast = input('\nPlease enter amount:\n')

                if balance < customfast:
                    print('Insufficient funds!')
                    continue

                elif balance >= customfast:
                    print('\nWithdrawing $' + customfast + '...\n')
                    print('Please take your card and cash from below.')
                    balance -= int(customfast)
                    print('\nYour current balance is: $' + str(balance))
                    sleep(5)
                    break
                    clear()
# Invalid choice    
            else:
                print('That is an invalid input, please try again.')
                continue
# Balance
        elif directory == "4":
            print('\nYour current Balance is: $' + str(balance))
            sleep(5)
            break
            clear() 
# Invalid choice
        else:
            print('That is an invalid input, please try again.')
            continue
    return balance
atm()
# Additional request        
print('\nWould you like to make another transaction?\n') 
additionalrequest = input('Y or N\n')
# If input y or Y, restart loop
if additionalrequest == str('Y'):
    clear()
    atm()
# If input n or N, break loop
elif additionalrequest == str('N'):
    flag == False
    print('Thank you for banking with Bank of Python. Have a wonderful day!')

# Invalid input
else:
    print('That is an invalid input, please try again.') 
# Exit message
if flag == False:
    print('Thank you for banking with Bank of Python. Have a wonderful day!')
    sleep(5)
    clear()
