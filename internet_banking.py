user = 'Raun'
passw = "python"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == user and password == passw:
    amount = int(input("Enter amount to Transfer: "))
    print("Transfer successfull")
else:
    print("Username or password does not match") 
