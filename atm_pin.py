denom1 = 100
denom2 = 500
denom3 = 200
pin = int(input("Enter the ATM PIN: "))
cor_pin = 1234
if pin == cor_pin:
     amount = int(input("Enter the amount you want to draw: "))
     if amount%denom1 == 0 or amount%denom2 == 0 or amount%denom3 == 0:
         print("Take and Count your Cash: ")
     else:
         print("Enter Correct Amount")
else:
    print("Enter correct Pin and try again")
