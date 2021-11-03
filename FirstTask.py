<<<<<<< HEAD
# check balance -> done
# draw money -> done
# deposit bills -> done
# transfeer money -> done
# type of account -> done
# compare accout -> done
=======
>>>>>>> origin/main
from random import randint as rand
from os import system as sys
from time import sleep
class Bank:
    def __init__(self,name,passcode,accNumber,balance,accoutType):
        self.balance=balance
        self.accountType=accoutType
        self.accNumber=accNumber
        self.name=name
        self.passcode=passcode
        self.accNumber=accNumber

    def FullName(self):
        return self.name

    def accountNumber(self):
        return self.accNumber

    def Passcode(self):
        return self.passcode

    def checkBalance(self):
        return self.balance

    def depositBill(self,bill):
        self.balance+=bill
        return True

    def drawMoney(self,money):
        if(self.balance>=money):
            self.balance-=money
            return True
        else:
            return False
    
    def transferMoney(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
            return True
        else:
            return False
  
    def checkAccountType(self):
        return self.accountType

    def accDetails(self):
        print("Account # ", self.accNumber)
        print("Name: ", self.name)
        print("Balance: ", self.balance)

obj = []
if __name__ == '__main__':
   while(1):
        option=int(input('1) Create Account \n2) Login \n0) Exit\nChoose:'))
        if(option == 1):
            sys("clear")
            accno=rand(1,100)+1000
            name=input('Enter Full Name:')
            passcode=int(input("Enter Passcode:"))
            accType=input("Enter Account Type:")
            balance=int(input("Enter Balance for Account:"))
            obj.append(Bank(name,passcode,accno,balance,accType))
            print(f"Account Created Successfull!\nYour Account Number is {accno}\n\n")
            sleep(5)
            sys("clear")

        elif option ==2 :
            sys('clear')
            accno=int(input('Enter Account Number:'))
            code=int(input('Enter Passcode:'))
            chk1 = False
            for i in range(len(obj)):
                if accno==obj[i].accountNumber() and code==obj[i].Passcode():
                    chk1 = True
                    print("Login Successful!\n\n")

                    while(1):
                        sys('clear')
                        select=int(input('1) Check Balance \n2) Deposit Bill \n3) Draw Money \n4) Transfer Money \n5) Account Type\n6) Compare Your Account \n0) Exit\nChoose:'))
                        if select == 1:#checkbalance
                            print(obj[i].checkBalance())
                            input()
                        elif select == 2:#depositbill
                            dep=int(input("Enter Deposit Amount:"))
                            obj[i].depositBill(dep)
                            print("Successfully money deposit!")
                            input()
                        elif select == 3:#draw money
                            amount=int(input('Enter Amount to with draw:'))
                            if(obj[i].drawMoney(amount)):
                                print("Money Draw Successful!")
                            else:
                                print('Not enough cash!')
                            input()
                        elif select == 4:#transfercash
                            money=int(input('Enter Transfer amount:'))
                            if( obj[i].transferMoney(money)):
                                print('Successful Money Transfer!')
                            else:
                                print("Not enough cash!")
                            input()
                        elif select == 5:
                            print(obj[i].checkAccountType())
                            input()
                        elif select == 6:
                            if len(obj) > 1:
                                chk2 = False

                                system('cls')
                                accNum = int(input("Enter Account Number you want to be compared with: "))
                                for j in range(len(obj)):
                                    if accNum == obj[j].accountNumber():
                                        chk2 = True
                                        print("\nYour Details: ")
                                        obj[i].accDetails()
                                        print("Other Account's Details: ")
                                        obj[j].accDetails()
                                        if(obj[i].checkBalance() > obj[j].checkBalance()):
                                            print("\nYour Account is Larger than Provided Account\n\n")
                                        elif (obj[i].checkBalance() == obj[j].checkBalance()):
                                            print("Your Account is Equal to the Provided Account\n\n")
                                        else:
                                            print("Your Account is Smaller than Provided Account\n\n")
                                if (not chk2):
                                    print("Account Number Doesn't Exist\n\n")
                        elif select == 0:
                            break
                        else:
                            print('Incorrect Option!\n\n')
                            sleep(1)
            if (not chk1):
                print("Incorrect Passcode or Account Number!\n\n")
                sleep(1)
                sys('cls')
        elif option == 0:
            break
        else:
            print('Invalid Selection!\n\n')