#print day of week based on user input of number
DOW = ['Python_stupid_index','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
num = int(input("Enter the number:"))
while num > 0 and num <= 7:
    print(DOW[num])
    break
else:
    print("Number is not between 1 and 7")
