#Satish Singh-22AD1003

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try :
    print(a/b)
except ZeroDivisionError as e:
    print("Exception occured:",e)
else :
    print("No exception occured")
finally :
    print("End of program")
