user = 'Raun'
passw = "python"
username = input("Enter your username: ")
password = input("Enter your password: ")
while i in range(1,4):
    
     if username == user and password == passw:
        amount = int(input("Enter amount to Transfer: "))
        print("Transfer successfull")
        break
     else:
        attempts = 3-i
        print("You have ", attempts ,"Left")
        if attempts == 0:
         print("Account Locked")
        
