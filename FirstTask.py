from os import system as sys

logout_check = False

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

    account_list = []

    def create_account(self, account):
        self.account_list.append(account)
    
    def login(self, account_number, code):
        user1=self.find_account(account_number)
        global logout_check
        if  logout_check == False:
            if user1[0]:
                if code == user1[1].pass_code():
                    logout_check = False
                    return True, user1[1]
            return False, "Account Not Found!"

    def transfer_money(self, sender_account_number, receiver_account_number, amount):
        user1 = self.find_account(sender_account_number)
        user2 = self.find_account(receiver_account_number)
        if user1[0]:
            user2[1].deposit_bill(amount)
            user1[1].balance -= amount
            return True
        else:
            return False
    
    def compare(self,current_account,other_account):
        user1 = self.find_account(current_account)
        user2 = self.find_account(other_account)
        if user1[0] and user2[0]:
            if user1[1].check_balance() > user2[1].check_balance():
                return True, 1
            if user1[1].check_balance() < user2[1].check_balance():
                return True, -1
            if user1[1].check_balance() == user2[1].check_balance():
                return True, 0
        else:
            return False, "Account Not Found!"
    
    def find_account(self, account_number):
        for i in range(len(Bank.account_list)):
            if account_number == Bank.account_list[i].account_number():
                return True, Bank.account_list[i]
        return False, "Account not found!"

    def account_details(self, account_number):
        check = self.find_account(account_number)
        if check[0]:
            check[1].account_details()
        else:
            return False
   
    def logout():
        global logout_check
        logout_check = True

def run():
    account_number_id = 1000
    obj = []
    account_list=Bank()
    while(1):
        option = int(input("1) Create Account \n2) Login \n3) Find Account \n0) Exit \nChoose:"))
        if option == 1:
            sys('clear')
            account_number_id += 1
            name = input("Enter Full Name: ")
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
            account_list.create_account(BankAccount(name, pass_code, account_number_id, balance, account_type))
            print(f"Account Created Successfully\nYour Account Number is {account_number_id}\n\n")
            input("\nPress Any Key to Continue\n")
            sys("clear")
        
        elif option == 2:
            global logout_check
            if logout_check == False:
                account_number = int(input("Enter Account Number: "))
                code = int(input("Enter Passcode: "))
                log = account_list.login(account_number, code)
            if log[0]:
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
                        value = account_list.transfer_money(log[1].account_number(), receiver_account_number, money)
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
                        value = account_list.compare(log[1].account_number(), other_account_number)
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
                        sys("clear")
                        break

                    else:
                        print("Incorrect Option!")
                        input("\nPress any Key to Continue\n")

        elif option == 3:
            account_number = int(input("Enter Account Number:"))
            account_list.account_details(account_number)
            input("\nPress Any Key to Continue\n")
            sys("clear")

        elif option == 0:
            break

        else:
            print("\nInvalid option\n")

if __name__ == "__main__":
    run()