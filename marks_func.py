def marks(a):
    while a >= 0 and a <=100:
        if a >= 95:
            print("Passed With Disctinction")
            break
        elif a < 95 and a >= 75:
            print("Passed With First Class")
            break
        elif a < 75 and a >= 40:
            print("Passed with Second Class")
            break
        else:
            print("You have failed.Study hard next time")
            break
a = eval(input("Enter the marks: "))
marks(a)
