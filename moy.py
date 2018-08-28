#Enter number print month
MOY = ['Python_stupid_index','January','Feburary','March','April','May','June','July','August','September','October','November','December']
num = int(input("Enter the number:"))
while num > 0 and num <= 12:
    print(MOY[num])
    break
else:
    print("Number is not between 1 and 12")
