# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 20:22:53 2025

@author: PRASANNA
"""

def Show_balance(balance):
    print("----------------------------------------------------")
    print(f"Your bank balance is {balance:.2f}")
    print("----------------------------------------------------")
def deposit(balance):
    print("----------------------------------------------------")
    amount=float(input("enter the amount to be deposited :"))
    print("----------------------------------------------------")
    if amount<0:
        print("That's not a valid amount")
        print("----------------------------------------------------")
        return 0
    else:
        return amount
    print("----------------------------------------------------")
def withdraw(balance):
   amount=float(input("enter the amount to be withdrawn:"))
   print("----------------------------------------------------")
   if amount>balance:
       print("Insufficient Amount")
       print("----------------------------------------------------")
       return 0
   elif amount < 0:
       print("Amount must be greater than zero ")
       print("----------------------------------------------------")
       return 0
   else:
       return amount
def main():
    balance=0
    is_running=True
    while is_running:
        print("----------------------------------------------------")
        print("Banking Program")
        print("----------------------------------------------------")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("----------------------------------------------------")
        
        choice=input("enter your choice(1-4):")
        if choice=='1':
            Show_balance(balance)
        elif choice=='2':
            balance +=deposit(balance)
            print(f"The remaining balance in your account :{balance}")
        elif choice=='3':
            balance -=withdraw(balance)
            print(f"The remaining balance in your account :{balance}")
        elif choice=='4':
            is_running =False
        else:
            print("That's not a valid choice")
    print("THANK YOU!!!!! HAVE A NICE DAY........")
if __name__=='__main__':
    main()
