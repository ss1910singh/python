#Satish Singh-22AD1003
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Cannot divide by zero") 
        return None
    else:
        return a/b
    
a = int(input("Enter first number : "))
b = int(input("Enter second number: "))

print("1. Addition, 2.Subtraction, 3. Multiplication, 4. Division")

choice = int(input("Enter your choice: "))
if choice==1:
    print("Addition is", add(a,b))
elif choice==2:
    print("Subtraction is", sub(a,b))
elif choice ==3:
    print("Multiplication is",mul(a,b))
elif choice==4:
    print("Division is", div(a,b))
else:
    print("Invalid choice")