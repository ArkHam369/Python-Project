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
            
def prg():    
    print("----------------------------------------")
    print("|               > Levels <             |")
    print("|          > For Easy type 3 <         |")
    print("|          > For Medium type 6 <       |")
    print("|          > For Hard type 9 <         |")
    print("|          > For Nightmare type 7 <    |")
    print("----------------------------------------")

    name = input("Enter your name: ")
    desire = int(input("Enter the desired level: "))
    valid_entries = [3,6,9,7]
    while desire not in valid_entries:
        print("\nChoose Your Desires Wisely +_+")
        desire = int(input("Enter the desired level: "))
    
    comp_score = 0
    player_score = 0
    while True:
        import random as rn
        if desire == 3:
            choice = rn.randint(1,2)
        elif desire == 6:
            choice = rn.randint(1,3)
        elif desire == 9:
            choice = rn.randint(1,4)
        elif desire == 7:
            choice = rn.randint(1,6)   
    
        if desire == 3:
            print("=======================================")
            inputt = int(input(">>>Enter your prediction as 1 or 2: "))
            while inputt == '':
                print("\n!!!Error!!!")
                inputt = int(input(">>>Enter your prediction as 1 or 2: "))
            while inputt not in range(1,3):
                print("\n!!!Error!!!")
                inputt = int(input(">>>Enter your prediction as 1 or 2: "))
                
        elif desire == 6:
            print("=======================================")
            inputt = int(input(">>>Enter any prediction from 1 to 3 : "))
            while inputt == '':
                print("\n!!!Error!!!")
                inputt = int(input(">>>Enter any prediction from 1 to 3 : "))
            while inputt not in range(1,4):
                print("\n!!!Error!!!")
                inputt = int(input(">>>Enter any prediction from 1 to 3 : "))
            
        elif desire == 9:
            print("=======================================")
            inputt = int(input(">>>Enter any prediction from 1 to 4 : "))
            while inputt == '':
                print("\n!!!Error!!!")
                inputt = int(input(">>>Enter any prediction from 1 to 4 : "))
            while inputt not in range(1,5):
                print("\n!!!Error!!!")
                inputt = int(input(">>>Enter any prediction from 1 to 4 : "))
            
        elif desire == 7:
            print("=======================================")
            inputt = int(input(">>>Enter any prediction from 1 to 6 : "))
            while inputt == '':
                print("\n!!!Error!!!")
                inputt = int(input(">>>Enter any prediction from 1 to 6 : "))
            while inputt not in range(1,7):
                print("\n!!!Error!!!")
                inputt = int(input(">>>Enter any prediction from 1 to 6 : "))
        
    
        if inputt == choice:
            print(">>>Computer's Choice: ", choice)
            player_score += 1
            print("\nYou Lucky Lucky :) ")
            if player_score == 10:
                print("\n  ********************************   ")
                print("  >> Computer's Score :- ", comp_score)
                print("  >>",name,"'s Score :- ",player_score)
                print("            Jackpot :)        ")
                print("\n  >Game by Ansh Raj aka ArkHam369<")
                print("  ********************************   ")
                print("=======================================")
                break
            print("\n>> Computer's Score :- ", comp_score)
            print(">>",name,"'s Score :- ",player_score)
            print("=======================================")
        else:
            print(">>>Computer's Choice: ", choice)
            comp_score += 1
            print("\nBetter luck next time :)")
            if comp_score == 10:
                print("\n  ********************************   ")
                print("  >> Computer's Score :- ", comp_score)
                print("  >>",name,"'s Score :- ",player_score)
                print("            Loooser '_'        ")
                print("\n  >Game by Ansh Raj aka ArkHam369<")
                print("  ********************************   ")
                print("=======================================")
                break
            print("\n>> Computer's Score :- ", comp_score)
            print(">>",name,"'s Score :- ",player_score)
            print("=======================================")
