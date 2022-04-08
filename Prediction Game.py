def game():    
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
game()
