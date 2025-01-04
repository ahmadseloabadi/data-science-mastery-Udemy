def add(a,b):
    return a + b
def subtract (a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        print("invalid division number!")

while True:
    print("\n Menu :")
    print(" 1. additional")
    print(" 2. subtraction")
    print(" 3. multiplication")
    print(" 4. devision")
    print(" 5. exit")

    choice=input("Enter the number :")

    if choice == "5":
        print(" exit program :)")
        break

    num1=float(input("input first number"))
    num2=float(input("input second number"))

    if choice == "1":
        print("result :", add(num1,num2))
    elif choice == "2":
        print("result :", subtract(num1,num2))
    elif choice == "3":
        print("result :", multiply(num1,num2))
    elif choice == "4":
        print("result :", divide(num1,num2))
    else:
        print("invalid choice ,please try again ")
    
    