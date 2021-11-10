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
    
class Bank():
    @staticmethod
    def login(account_list, account_number, code):
        sys('clear')
        check1 = False
        for i in range(len(account_list)):
            if account_number == account_list[i].account_number() and code == account_list[i].pass_code():
                return True,account_list[i]
        return False
    
    @staticmethod
    def transfer_money(sender_account_number, receiver_account_number, amount):
        if receiver_account_number.deposit_bill(amount):
            sender_account_number.balance -= amount 
            return True

    @staticmethod
    def compare(current_account, account_list, other_account_number):
        check2 = False
        for j in range(len(account_list)):
            if other_account_number == account_list[j].account_number():
                check2 = True
                print("\nYour Details: ")
                BankAccount.account_details(current_account)
                print("\nOther Account's Details: ")
                BankAccount.account_details(account_list[j])
                if current_account.check_balance() > account_list[j].check_balance():
                    return 1
                elif current_account.check_balance() == account_list[j].check_balance():
                    return 0
                else:
                    return -1
        if not check2:
            print("\nAccount Number Doesn't Exist\n\n")

    @staticmethod
    def find_account(account_number):
        account_number.account_details()


def run():
    account_number_id = 1000
    obj = []
    while(1):
        option = int(input("1) Create Account \n2) Login \n3) Find Account \n0) Exit \nChoose:"))

        if option == 1:
            sys('clear')
            account_number_id += 1
            name = input("Enter Full Nmae: ")
            pass_code = int(input("Enter Passcode "))
            while(1):
                account_select = int(input("Select Account Type from following:\n1) Current \n2) Saving \n3) Business\n"))
                if account_select == 1:
                    account_type = "Current"
                    break
                elif account_select == 2:
                    account_type = "Saving"
                    break
                elif account_select == 3:
                    account_type = "Business"
                    break
                else:
                    print("\nInvalid Account Type\n")
            balance = 0
            obj.append(BankAccount(name, pass_code, account_number_id, balance, account_type))
            print(f"Account Created Successfully\nYour Account Number is {account_number_id}\n\n")
            input("\nPress Any Key to Continue\n")
            sys("clear")
        
        elif option == 2:
            account_number = int(input("Enter Account Number: "))
            code = int(input("Enter Passcode: "))
            log = Bank.login(obj, account_number, code)
            if log[0]:
                print("Login Successful!")
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
                        found = False
                        money = int(input("Enter Transfer Amount: "))
                        transfer_account_number = int(input("Enter Account Number of Other User: "))
                        if account_number_id != transfer_account_number >= 1001:
                            for k in range(len(obj)):
                                if transfer_account_number == obj[k].account_number() :
                                    Bank.transfer_money(log[1], obj[k], money)
                                    found = True
                            if not found:
                                print("Invalid Account Number!")
                            else:
                                print("Successfull Money Transfer!")
                        else:
                            print("Not enough cash!")
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 5:
                        print(log[1].check_account_type())
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 6:
                        other_account_number = int(input("Enter Account Number you want to compare with: "))
                        value = Bank.compare(log[1], obj, other_account_number)
                        if value == 1:
                            print("Your Account is Greater than Provided Account!")
                        elif value == 0:
                            print("Your Account is Equal to the Provided Account!")
                        else:
                            print("Your Account is Smaller than Provided Account!")
                        input("\nPress Any Key to Continue\n")
                    
                    elif select == 7:
                        print(BankAccount.account_details(log[1]))
                        input("\nPress any Key to Continue\n")
                    
                    elif select == 0:
                        break

                    else:
                        print("Incorrect Option!")
                        input("\nPress any Key to Continue\n")

        elif option == 3:
            account_number = int(input("Enter Account Number:"))
            for i in range(len(obj)):
                if obj[i].account_number() == account_number:
                    Bank.find_account(obj[i])
            input("\nPress any Key to Continue\n")
            sys("clear")

        elif option == 0:
            break

        else:
            print("\nInvalid option\n")

if __name__ == "__main__":
    run()