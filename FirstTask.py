from os import system as sys

class BankAccount:
    def __init__(self, Name, PassCode, AccNumber, Balance, AccoutType):
        self.Name = Name
        self.Passcode = PassCode
        self.Balance = Balance
        self.AccountType = AccoutType
        self.AccNumber = AccNumber

    def FullName(self):
        return self.Name

    def AccountNumber(self):
        return self.AccNumber

    def PassCode(self):
        return self.Passcode

    def CheckBalance(self):
        return self.Balance

    def CheckAccountType(self):
        return self.AccountType

    def AccDetails(self):
        print("Account # ", self.AccNumber)
        print("Name: ", self.Name)
        print("Balance: ", self.Balance)
        print("Account Type: ", self.AccountType)

    def DepositBill(self,Bill):
        if Bill >= 0:
            self.Balance += Bill
            return True
        else:
            return False

    def DrawMoney(self,Money):
        if self.Balance >= Money:
            self.Balance -= Money
            return True
        else:
            return False
    
    def TransferMoney(self,Amount):
        if self.Balance >= Amount:
            self.Balance -= Amount
            return True
        else:
            return False

    @staticmethod
    def Login(obj, AccNo, Code):
        while(1):
            chk1 = False
            for i in range(len(obj)):
                if (AccNo == obj[i].AccountNumber() and Code == obj[i].PassCode()):
                    return (True,obj[i])
            print("\nInvalid Credentials\n")
            input("\nPress Any Key to Continue!\n")
            sys('clear')
            return (False,obj[i])

    @staticmethod
    def Compare(log, obj, AccNum):
        chk2 = False
        #AccNum = int(input("Enter Account Number you want to be compared with: "))
        for j in range(len(obj)):
            if AccNum == obj[j].AccountNumber():
                chk2 = True
                print("\nYour Details: ")
                log.AccDetails()
                print("Other Account's Details: ")
                obj[j].AccDetails()
                if log.CheckBalance() > obj[j].CheckBalance():
                    print("\nYour Account is Larger than Provided Account\n\n")
                elif log.CheckBalance() == obj[j].CheckBalance():
                    print("Your Account is Equal to the Provided Account\n\n")
                else:
                    print("Your Account is Smaller than Provided Account\n\n")
        if (not chk2):
            print("Account Number Doesn't Exist\n\n")
                
AccNo=1000
obj = []

                                
if __name__ == '__main__':
   while(1):
        option = int(input('1) Create Account \n2) Login \n0) Exit\nChoose:'))
        if option == 1 :
            sys("clear")
            AccNo += 1
            Name = input('Enter Full Name:')
            Passcode = int(input("Enter Passcode:"))
            while(1):
                AccSelect = int(input("Select Account Type from following:\n1) Current \n2) Saving \n3) Business \n"))
                if AccSelect == 1:
                    AccType = "Current"
                    break
                elif AccSelect == 2:
                    AccType = "Saving"
                    break
                elif AccSelect == 3:
                    AccType = "Business"
                    break
                else: 
                    print("Invalid Selection")
            Balance = 0
            obj.append(BankAccount(Name, Passcode, AccNo, Balance, AccType))
            print(f"Account Created Successfull!\nYour Account Number is {AccNo}\n\n")
            input("\nPress Any Key to Continue\n")
            sys("clear")
        elif option == 2 :
            sys("clear")
            AccNo = int(input('Enter Account Number:'))
            Code = int(input('Enter Passcode:'))
            log = BankAccount.Login(obj, AccNo, Code)
            if log[0]:
                print('Login Successful!')
                select=1
                while(not select == 0 ):
                    sys('clear')
                    select = int(input('1) Check Balance \n2) Deposit Bill \n3) Draw Money \n4) Transfer Money \n5) Account Type \n6) Compare Your Account \n7) Account Details \n0) Exit\nChoose:'))
                    if select == 1:#checkbalance
                        print(log[1].CheckBalance())
                        input("\nPress Any Key to Continue\n")
                    elif select == 2:#depositbill
                        Dep = int(input("Enter Deposit Amount:"))
                        if log[1].DepositBill(Dep): 
                            print("Money successfully deposited!")
                        else:
                            print('Money Must be Greater than 0!')
                        input("\nPress Any Key to Continue\n")
                    elif select == 3:#draw money
                        Amount = int(input('Enter Amount to with draw:'))
                        if log[1].DrawMoney(Amount):
                            print("Money Draw Successful!")
                        else:
                            print('Not enough cash!')
                        input("\nPress Any Key to Continue\n")
                    elif select == 4:#transfercash
                        found = False
                        Money = int(input('Enter Transfer amount:'))
                        if log[1].TransferMoney(Money):
                            TransferAccountNo = int(input('Enter Account Number of other User:'))
                            if AccNo != TransferAccountNo >= 1001:
                                for k in range(len(obj)):
                                    if TransferAccountNo == obj[k].AccountNumber():
                                        obj[k].DepositBill(Money)
                                        found = True
                            if not found:
                                print("Invalid Account Number!")
                            else:
                                print('Successful Money Transfer!')
                        else:
                            print("Not enough cash!")
                        input("\nPress Any Key to Continue\n")
                    elif select == 5:
                        print(log[1].CheckAccountType())
                        input("\nPress Any Key to Continue\n")
                    elif select == 6:
                        sys('clear')
                        AccNum = int(input("Enter Account Number you want to be compared with: "))
                        BankAccount.Compare(log[1],obj,AccNum)
                        input("\nPress Any Key to Continue\n")
                    elif select == 7:
                        print(log[1].AccDetails())
                        input("\nPress Any Key to Continue\n")
                    elif select == 0:
                        break
                    else:
                        print('Incorrect Option!\n\n')
                        input("\nPress Any Key to Continue\n")

        elif option == 0:
            break
        else:
            print('Invalid Selection!\n\n')