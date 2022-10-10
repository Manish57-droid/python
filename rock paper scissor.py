from colorama import Fore

try:
    def decider(comp, inp, su, sc):
        if comp == 'rock' and inp == 'p':
            print(name + " Wins")
            print("Enter 1 to continue and 0 to leave the game")
            su += 1
            i1 = input()
            return i1, su, sc
        elif comp == 'rock' and inp == 's':
            print("Computer Wins")
            print("Enter 1 to continue and 0 to leave the game")
            sc += 1
            i1 = input()
            return i1, su, sc
        elif comp == 'paper' and inp == 'r':
            print("Computer Wins")
            print("Enter 1 to continue and 0 to leave the game")
            sc += 1
            i1 = input()
            return i1, su, sc
        elif comp == 'paper' and inp == 's':
            print(name + " Wins")
            print("Enter 1 to continue and 0 to leave the game")
            su += 1
            i1 = input()
            return i1, su, sc
        elif comp == 'scissors' and inp == 'r':
            print(name + " Wins")
            print("Enter 1 to continue and 0 to leave the game")
            su += 1
            i1 = input()
            return i1, su, sc
        elif comp == 'scissors' and inp == 'p':
            print("Computer Wins")
            print("Enter 1 to continue and 0 to leave the game")
            sc += 1
            i1 = input()
            return i1, su, sc
        elif (comp == 'rock' and inp == 'r') or (comp == 'paper' and inp == 'p') or (comp == 'scissors' and inp == 's'):
            print("Draw")
            print("Enter 1 to continue and 0 to leave the game")
            su += 1
            sc += 1
            i1 = input()
            return i1, su, sc


    def checker():
        inp = input("Enter your choice:")
        if inp == 'r' or inp == 'p' or inp == 's':
            return inp
        else:
            print("Wrong Input!!")
            return 0


    import random

    ele = ['rock', 'paper', 'scissors']
    print(Fore.LIGHTCYAN_EX + "Welcome to the game!")
    print(Fore.CYAN + "Enter:\nr for rock\np for paper\ns for scissors")
    name = input(Fore.YELLOW + "Enter your name:")
    i = '1'
    su1 = 0
    sc1 = 0
    while i == '1':
        inp3 = checker()
        while inp3 == 0:
            inp3 = checker()
        comp1 = random.choice(ele)
        print("Computer chooses:" + comp1)
        i, sc1, su1 = decider(comp1, inp3, su1, sc1)
        if i == '0':
            print(Fore.MAGENTA + "Scores for this match are as follows:")
            print(Fore.BLUE + name + "'s score: ", su1)
            print(Fore.BLUE + "computer's score: ", sc1)
            print(Fore.GREEN + "Thankyou for playing the game.\nHave a nice day!!")
        elif i != '0' and i != '1':
            print(Fore.RED + "Invalid Input!!")
            i = int(input("Please enter 1 to continue or 0 to leave the game:"))


except Exception as e:
    print(Fore.RED + "Error Occured!!\nPlease restart the game.")
