def oddeven(a):
    while a > 0:
        if a%2 == 0:
            print("Even number")
            break
        else:
            print("Odd number")
            break
a = eval(input("Enter the number: "))
oddeven(a)
