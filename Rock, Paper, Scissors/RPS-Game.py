# Program to simulate Real-Life "Rock-Paper-Scissor" Game
# No of Rounds(selected by user) between user and computer
# Results will be displayed once the no of rounds completed
import os


def game():
    rounds = int(input('\n\t\t Welcome To Rock Paper Scissor Game\n\t\tHow Many Rounds You Want to Play:  '))
    user = 0
    comp = 0
    i = 1
    while i <= rounds:
        import random
        com_choice = random.choice(['r', 'p', 's'])  # Randomly generated choice for computer
        user_choice = input(f"Enter #{i} Choice [Rock(R), Paper(P), Scissor(S)]: ")
        if user_choice.lower() in ['r', 'p', 's']:  # To verify user selected choice
            if user_choice == com_choice:
                print("\n\tIT`S A TIE")
                print(f'''\tComputer V/S Human\n\t    {comp}          {user}\n''')

            elif user_choice == 'r' and com_choice == 's':
                user += 1
                print("\n\tYou Won !! ")
                print(f'''\tComputer V/S Human\n\t    {comp}          {user}\n''')
        
            elif user_choice == 'r' and com_choice == 'p':
                comp += 1
                print("\n\tComputer Won !! ")
                print(f'''\tComputer V/S Human\n\t    {comp}          {user}\n''')

            elif user_choice == 's' and com_choice == 'p':
                user += 1
                print("\n\tYou Won !! ")
                print(f'''\tComputer V/S Human\n\t    {comp}          {user}\n''')

            elif user_choice == 's' and com_choice == 'r':
                comp += 1
                print("\n\tComputer Won !! ")
                print(f'''\tComputer V/S Human\n\t    {comp}          {user}\n''')

            elif user_choice == 'p' and com_choice == 'r':
                user += 1
                print("\n\tYou Won !! ")
                print(f'''\tComputer V/S Human\n\t    {comp}          {user}\n''')

            elif user_choice == 'p' and com_choice == 's':
                comp += 1
                print("\n\tComputer Won !! ")
                print(f'''\tComputer V/S Human\n\t    {comp}          {user}\n''')

        else:
            print("Invalid Choice !! \n ")
        i += 1

    print(f'''\t THANKS FOR PLAYING 
                \n\t Computer : {comp} \n\t User : {user}\n''')
    if comp < user:
        print("\tYou Won the Series\n")
    elif comp > user:
        print("\tComputer Won the Series\n")
    else:
        print("Tie between Computer and You\n")
    again = input("Wanna Play Again (Y/N) : ")
    if again.lower() == 'y':
        os.system('cls')
        game()


game()
