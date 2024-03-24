import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
uscore = 0
cscore = 0
game_images = [rock, paper, scissors]
def game():
    global uscore, cscore
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    else:
        print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])
        if user_choice == 0 and computer_choice == 2:
            print("You win!")
            uscore += 1
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
            cscore += 1
        elif computer_choice > user_choice:
            print("You lose")
            cscore += 1
        elif user_choice > computer_choice:
            print("You win!")
            uscore += 1
        elif computer_choice == user_choice:
            print("It's a draw")
        print("Your Score =", uscore)
        print("Computer Score =", cscore)
def main():
    while True:
        user_input = input("Do you want to play a game? (yes/no): ").lower()
        if user_input == "yes":
            game()
        elif user_input == "no":
            print("Exiting the game.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
if __name__ == "__main__":
    main()