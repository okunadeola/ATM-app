# bank assignment
import sys
import math
import random
import time

account__balance = 0
account__name = ''
account__pin = 0

bankLog = []
currentIndex = 0


def banking():
  print("you are welcome to TechBank")
  print("""Enter your operation
  1. Start Registration
  2. Login to your Account
  3. quit""")
  route = input("Enter your operation >>>")
  if route == "1":
    register()
  elif route == "2":
    login()
  elif route == "3":
    sys.exit()


def register():
  global account__name
  account__name = input("Enter your account name >>>")
  while True:
    global account__pin
    account__pin = int(
        input("type your 4 digit account pin of your choice or 0 to exit>>>"))
    if len(str(account__pin)) != 4:
      print("pin should be 4 digit")
      continue
    elif len(str(account__pin)) == 4:
      if len(bankLog) == 0:
        validRegister()
      for i in bankLog:
        if account__pin == i["pin"]:
          print("oops! this account pin " + str(i["pin"]) + " already exist")
        elif account__pin != i["pin"]:
          validRegister()


def login():
  print("===========LOGIN=============")
  while True:
    account__pin = int(
        input("type your 4 digit account pin or 0 to go back >>>"))
    if len(bankLog) == 0:
      print("You have not register yet")
      register()
    if account__pin == 0:
      banking()
    for i in bankLog:
      if account__pin == i["pin"]:
        print("You are welcome " + str(i["account__name"]))
        global currentIndex
        currentIndex = bankLog.index(i)
        bank()
      elif account__pin != i["pin"]:
        continue
    print("user not found")


def validRegister():
  account__number = math.floor(random.random()*10000000000)
  bankLog.append({"account__name": account__name, "account__number": account__number,
                 "account__balance": account__balance, "pin": account__pin})
  print("you have successfully register")
  print(bankLog)
  login()


def bank():
  print("""Enter your operation
  1. Deposit
  2. Withdraw
  3. Check Balance
  4. Main Menu
  5. quit""")
  option = input(">>>")
  if option == "1":
    deposit()
  elif option == "2":
    withdrawal()
  elif option == "3":
    checkbalance()
  elif option == "4":
    banking()
  elif option == "5":
    sys.exit()


def deposit():
  print("++++ Account Deposit +++")
  amount = int(input("Enter the amount you want to deposit >>>"))
  while True:
    your_pin = int(input("Enter your secrete PIN or 0 to go back >>>"))
    if your_pin == bankLog[currentIndex]["pin"]:
      global account__balance
      bankLog[currentIndex]["account__balance"] += amount
      print("Please wait for your transaction is proccesing....")
      time.sleep(5)
      print(bankLog)
      print(bankLog[currentIndex]["account__name"] +
            " , you have successfully deposited " + f"{amount} to your account")
      bank()
    else:
      print("your pin is not valid")


def withdrawal():
  print("++++ Account Withdrawal +++")
  while True:
    amount = input("Enter the amount you want to withdraw or b to go back to main menu >>>")
    numb = int(amount)
    your_pin = int(input("Enter your secrete PIN or 0 to go back >>>"))
    if your_pin == bankLog[currentIndex]["pin"]:
      if numb > bankLog[currentIndex]["account__balance"]:
        print("opps your account balance is less than your requested withdrawal amount")
      elif numb <= 0:
        print("opps your withdrawal amount is invalid")
      elif numb <= bankLog[currentIndex]["account__balance"]:
        print("Please wait for your transaction is proccesing....")
        time.sleep(5)
        bankLog[currentIndex]["account__balance"] -= numb
        print(str(bankLog[currentIndex]["account__name"]) + ", you have successfully withdraw " + amount + " from your account, new balance is " + str(bankLog[currentIndex]["account__balance"]))
        bank()
    elif amount.lower() == "b":
      bank()
    else:
      print("your pin is not valid")


def checkbalance():
  print("++++ Check Account Balance +++")
  while True:
    your_pin = int(input("Enter your secrete PIN or 0 to go back >>>"))
    if your_pin == bankLog[currentIndex]["pin"]:
      print(str(bankLog[currentIndex]["account__name"]) + ", your account balance is "  + str(bankLog[currentIndex]["account__balance"]))
      bank()
    elif your_pin == 0:
      bank()
    else:
      print("your pin is not valid")

# bank()
banking()
