def cal():
    def add(a,b):
        c = a+b
        return c
    def sub(a,b):
        c = a-b
        return c
    def div(a,b):
        c = a/b
        return c
    def mod(a,b):
        c = a%b
        return c
    def mu(a,b):
        c = a*b
        return c
    def fl(a,b):
        c = a//b
        return c
    def sq(a,b):
        c = a**b
        return c
    print("NOTE:- To use first enter a NUMBER then press ENTER and the PUT operator and then AGAIN press ENTER and enter ANOTHER number and to get RESULT just PRESS ENTER INSTEAD of operator. ")
    print(" _______________________________________________________")
    print("|                                                       |")
    print("| Enter the number and press following for calculation: |")
    print("|                     Add: +                            |")
    print("|                     Substranct: -                     |")
    print("|                     Multiplication: *                 |")
    print("|                     Divide: /                         |")
    print("|                     Floor Divide: //                  |")
    print("|                     Exponent: **                      |")
    print("|                     Modulo: %                         |")
    print("|                     Get Result :- ENTER               |")
    print("|_______________________________________________________|")
    y = ['','+','-','/','//','%','*','**']
    a = int(input("Enter the number: "))
    z = a
    while True:
        k = input()
        while k not in y:
            k = input("Enter valid operator: ")
        if k == '':
            print("Result is: ",z)
            print("Calculator by Ansh Raj aka ArkHam369")
            break
        elif k == '+':
            h = int(input("Enter the number: "))
            z = add(z,h)
        elif k == '-':
            h = int(input("Enter the number: "))
            z = sub(z,h)
        elif k == '/':
            h = int(input("Enter the number: "))
            z = div(z,h)
        elif k == '%':
            h = int(input("Enter the number: "))
            z = mod(z,h)
        elif k == '*':
            h = int(input("Enter the number: "))
            z = mu(z,h)
        elif k == '//':
            h = int(input("Enter the number: "))
            z = fl(z,h)
        elif k == '**':
            print("Power to be applied to: ",z)
            h = int(input("Enter the power: "))
            z = sq(z,h)
