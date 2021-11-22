from os import name, system as sys

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

    bank_accounts = []
    logged_in = False

    def total_account(self):
        return (len(self.bank_accounts))

    def create_account(self, name, code, account_type):
        self.bank_accounts.append(BankAccount(name, code, 1000+len(self.bank_accounts)+1, 0, account_type))

    def find_account(self, account_number):
        for i in range(len(Bank.bank_accounts)):
            if account_number == Bank.bank_accounts[i].account_number():
                return True, Bank.bank_accounts[i]
        return False, "Account not found!"

    def login(self, account_number, code):
        status, response = self.find_account(account_number)
        if status:
            if code == response.pass_code():
                self.logged_in_account = response
                Bank.logged_in = True
                return True, response
        return False, "Account Not Found!"

    def transfer_money(self, sender_account_number, receiver_account_number, amount):
        status_1, response_1 = self.find_account(sender_account_number)
        status_2, response_2 = self.find_account(receiver_account_number)
        if status_1 and status_2:
            if response_1.draw_money(amount):
                response_2.deposit_bill(amount)
                return True
        else:
            return False
    
    def compare(self, current_account, other_account):
        status_1, response_1 = self.find_account(current_account)
        status_2, response_2 = self.find_account(other_account)
        if status_1 and status_2:
            if response_1.check_balance() > response_2.check_balance():
                return True, 1
            if response_1.check_balance() < response_2.check_balance():
                return True, -1
            if response_1.check_balance() == response_2.check_balance():
                return True, 0
        else:
            return False, f"{other_account} Account Not Found!"
    
   
    def account_details(self, account_number):
        status,response = self.find_account(account_number)
        if status:
            response.account_details()
        else:
            return False
   
    def logout(self):
        self.logged_in = None
        return self.logged_in

    def is_logged_in(self):
        if self.logged_in:
            return True
        return False

def run():
    account_number_id = 1000 # Wrirting here just to print account number for user after account creation 
    bank = Bank()
    while(1):
        option = int(input("1) Create Account \n2) Login \n3) Find Account \n4) Total Accounts\n0) Exit \nChoose:"))
        if option == 1:
            sys('clear')
            account_number_id += 1
            name = input("Enter Full Name: ")
            pass_code = int(input("Enter Passcode "))
            while(1):
                ACCOUNT_TYPES = ["Current","Saving","Business"]
                account_select = int(input("Select Account Type from following:\n1) Current \n2) Saving \n3) Business\n"))
                if account_select == 1:
                    account_type = ACCOUNT_TYPES[1]
                    break
                elif account_select == 2:
                    account_type = ACCOUNT_TYPES[2]
                    
                    break
                elif account_select == 3:
                    account_type = ACCOUNT_TYPES[3]
                    break
                else:
                    print("\nInvalid Account Type\n")
            bank.create_account(name, pass_code,account_type)
            print(f"Account Created Successfully\nYour Account Number is {account_number_id}\n\n")
            input("\nPress Any Key to Continue\n")
            sys("clear")
        
        elif option == 2:
            if bank.is_logged_in() == False:
                account_number = int(input("Enter Account Number: "))
                code = int(input("Enter Passcode: "))
                log = bank.login(account_number, code)

            if bank.is_logged_in:
                print("Login Successful!")
                input("\nPress Any Key to Continue\n")
                select = 1
                while not select == 0:
                    sys('clear')
                    select = int(input("1) Check Balance \n2) Deposit Bill \n3) Draw Money \n4) Transfer Money \n5) Account Type \n6) Compare Your Account \n7) Account Details \n0) Log Out \nChoose:"))
                    if select == 1:
                        print(log[1].check_balance())
                        input("\nPress Any Key to Continue\n")

                    elif select == 2:
                        deposit_money = int(input("Enter Deposit Amount: "))
                        if log[1].deposit_bill(deposit_money):
                            print("Money Successfully Deposited")
                        else:
                            print("Money must be Greater than 0!")
                        input("\nPress Any Key to Continue\n")

                    elif select == 3:
                        amount = int(input("Enter Amount to withdraw: "))
                        if log[1].draw_money(amount):
                            print("Money Draw Successfull")
                        else:
                            print("Not Enough Cash")
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 4:
                        money = int(input("Enter Transfer Amount: "))
                        receiver_account_number = int(input("Enter Account Number of Other User: "))
                        value = bank.transfer_money(log[1].account_number(), receiver_account_number, money)
                        if value:
                            print("\nSuccessfull Money Transfer!\n")
                        else:
                            print("\nInvalid Details!\n")
                        input("\nPress Any Key to Continue\n")
                            
                    elif select == 5:
                        print(log[1].check_account_type())
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 6:
                        other_account_number = int(input("Enter Account Number you want to compare with: "))
                        value = bank.compare(log[1].account_number(), other_account_number)
                        if(value[0]):
                            if value[1] == 1:
                                print("Your Account is Greater than Provided Account!")
                            elif value[1] == -1:
                                print("Your Account is Smaller than Provided Account!")
                            else:
                                print("Your Account is Equal to the Provided Account!")
                        else:
                            print("Invalid Account!")
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 7:
                        print(BankAccount.account_details(log[1]))
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