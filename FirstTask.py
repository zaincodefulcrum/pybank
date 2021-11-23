from os import system as sys

class BankAccount:
    def __init__(self, name, password, account_no, balance, account_type):
        self.name = name
        self.balance = balance
        self.account_no = account_no
        self.account_type = account_type
        self.password = password

    def account_number(self):
        return self.account_no

    def pass_code(self):
        return self.password
    
    def check_balance(self):
        return self.balance

    def check_account_type(self):
        return self.account_type
    
    def deposit_bill(self, bill):
        if bill >= 0:
            self.balance += bill
            return True
        else:
            return False
    
    def draw_money(self, money):
        if self.balance >= money:
            self.balance -= money
            return True
        else:
            return False
    
    def account_details(self):
        print("Account # ", self.account_no)
        print("Name: ", self.name)
        print("Balance: ", self.balance)
        print("Account Type: ", self.account_type)
  
class Bank:

    ACCOUNT_TYPES = ["Current", "Saving", "Business"]
    bank_accounts = []
    logged_in_account = None

    def total_account(self):
        return len(self.bank_accounts)

    def create_account(self, name, code, account_type):
        account = BankAccount(name, code, 1000 + self.total_account() + 1, 0, account_type)
        self.bank_accounts.append(account)
        return account.account_no

    def find_account(self, account_number):
        for i in range(len(self.bank_accounts)):
            if account_number == self.bank_accounts[i].account_number():
                return True, self.bank_accounts[i]
        return False, f"{account_number} Account Not Found!"

    def login(self, account_number, code):
        status, response = self.find_account(account_number)
        if status:
            if code == response.pass_code():
                self.logged_in_account = response
                return True, "Successfully Login!"
        return False, f"{account_number} Account Not Found!"

    def transfer_money(self, sender_account_number, receiver_account_number, amount):
        status_1, response_1 = self.find_account(sender_account_number)
        status_2, response_2 = self.find_account(receiver_account_number)
        if status_1 and status_2:
            if response_1.draw_money(amount):
                response_2.deposit_bill(amount)
                return True, "Money Successfully transferred!"
        else:
            if status_1 == False:
                account_not_found = sender_account_number
            elif status_2 == False:
                account_not_found = receiver_account_number
            if status_1 == False and status_2 == False:
                return False, f"Both {sender_account_number} and {receiver_account_number} are invalid!"
            return False, f"{account_not_found} Account Not Found!"
    
    def compare(self, current_account, other_account):
        status_1, response_1 = self.find_account(current_account)
        status_2, response_2 = self.find_account(other_account)
        if status_1 and status_2:
            if response_1.check_balance() > response_2.check_balance():
                return True, "Your Account is Greater than Provided Account!"
            if response_1.check_balance() < response_2.check_balance():
                return True, "Your Account is Smaller than Provided Account!"
            if response_1.check_balance() == response_2.check_balance():
                return True, "Your Account is Equal to the Provided Account!"
        else:
            if status_1 == False:
                account_not_found = current_account
            elif status_2 == False:
                account_not_found = other_account
            if status_1 == False and status_2 == False:
                return False, f"{current_account} and {other_account} are invalid!"
            return False, f"{account_not_found} Account Not Found!"
   
    def account_details(self, account_number):
        status,response = self.find_account(account_number)
        if status:
            response.account_details()
        else:
            return False, f"{account_number} Account Not Found!"
   
    def logout(self):
        self.logged_in_account = None
        return self.logged_in_account

    def is_logged_in(self):
        if self.logged_in_account:
            return True
        return False

def run():
    bank = Bank()
    while(True):
        option = int(input("1) Create Account \n2) Login \n3) Find Account \n4) Total Accounts\n0) Exit \nChoose:"))
        if option == 1:
            sys('clear')
            name = input("Enter Full Name: ")
            pass_code = int(input("Enter Passcode "))
            while(True):
                msg = "\n".join(f'{index + 1}) {account_type}' for index, account_type in enumerate(bank.ACCOUNT_TYPES))
                print(msg)
                account_select = int(input())
                if 0 < account_select <= len(bank.ACCOUNT_TYPES):
                    account_type = bank.ACCOUNT_TYPES[account_select - 1]   
                    break 
                else:
                    print('\Invalid Selection\n')
                input('Press any key to continue!')
            print("Account Created and your ID is:", bank.create_account(name, pass_code, account_type))
            input("\nPress Any Key to Continue")
            sys("clear")
        
        elif option == 2:
            if bank.is_logged_in() == False:
                account_number = int(input("Enter Account Number: "))
                code = int(input("Enter Passcode: "))
                status, response = bank.login(account_number, code)

            if bank.is_logged_in():
                print("Login Successful!")
                input("\nPress Any Key to Continue\n")
                select = 1
                while not select == 0:
                    sys('clear')
                    select = int(input("1) Check Balance \n2) Deposit Bill \n3) Draw Money \n4) Transfer Money \n5) Account Type \n6) Compare Your Account \n7) Account Details \n0) Log Out \nChoose:"))
                    if select == 1:
                        print(bank.logged_in_account.check_balance())
                        input("\nPress Any Key to Continue\n")

                    elif select == 2:
                        deposit_money = int(input("Enter Deposit Amount: "))
                        if bank.logged_in_account.deposit_bill(deposit_money):
                            print("Money Successfully Deposited")
                        else:
                            print("Money must be Greater than 0!")
                        input("\nPress Any Key to Continue\n")

                    elif select == 3:
                        amount = int(input("Enter Amount to withdraw: "))
                        if bank.logged_in_account.draw_money(amount):
                            print("Money Draw Successfull")
                        else:
                            print("Not Enough Cash")
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 4:
                        money = int(input("Enter Transfer Amount: "))
                        receiver_account_number = int(input("Enter Account Number of Other User: "))
                        status, response = bank.transfer_money(bank.logged_in_account.account_number(), receiver_account_number, money)
                        if status:
                            print(response)
                        else:
                            print(response)
                        input("\nPress Any Key to Continue\n")
                            
                    elif select == 5:
                        print(bank.logged_in_account.check_account_type())
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 6:
                        other_account_number = int(input("Enter Account Number you want to compare with: "))
                        status, response = bank.compare(bank.logged_in_account.account_number(), other_account_number)
                        if(status):
                            print(response)
                        else:
                            print("Invalid Account!")
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 7:
                        print(BankAccount.account_details(bank.logged_in_account))
                        input("\nPress any Key to Continue\n")

                    elif select == 0:
                        bank.logout()
                        print("\nSuccessfully Logged Out\n")
                        input("\nPress any Key to Continue\n")
                        sys("clear")

                    else:
                        print("Incorrect Option!")
                        input("\nPress any Key to Continue\n")

        elif option == 3:
            account_number = int(input("Enter Account Number:"))
            bank.account_details(account_number)
            input("\nPress Any Key to Continue\n")
            sys("clear")

        elif option == 4:
            print('Total Accounts:', bank.total_account())

        elif option == 0:
            break

        else:
            print("\nInvalid option\n")

if __name__ == "__main__":
    run()