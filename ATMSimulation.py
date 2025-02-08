class ATM:
    def __init__(self):
        self.balance = 0
    
    def check_balance(self):
        print(f'Your current balance is: {self.balance}')
    
    def withdraw_money(self,amount):
        if(amount <= 0):
            print('amount must be positive')
        elif amount > self.balance:
            print(f'insufficient funds')
        else:
            self.balance-=amount
            print(f'successfully withdrawn {amount}')
            
    def deposit_amount(self,amount):
        if(amount <= 0):
            print('amount must be positive')
        else:
            self.balance+=amount
            print(f'successfully deposited {amount}')
            
def main():
    atm = ATM()
    while True:
        print('\nWelcome to the ATM')
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        
        choice = input("Please Enter choice: ")
        if choice =='1':
            atm.check_balance()
        elif choice == '2':
            while True:
                try:
                    amount = float(input('Enter the amount to withdraw: '))
                    atm.withdraw_money(amount)
                    break
                except ValueError:
                    print('Please Enter a valid amount: ')
        elif choice == '3':
            while True:
                try:
                    amount = float(input("Enter Amount to deposit: "))
                    atm.deposit_amount(amount)
                    break
                except ValueError:
                    print('Please Enter a valid amount')
                    
        elif choice == '4':
                print("Exiting the ATM...")
                break
                
if __name__ == '__main__':
    main()
            