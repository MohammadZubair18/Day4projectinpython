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


images = [rock,scissors,paper]
print("Welcome to Rock paper scissor Game")
human_choice=int(input("Chose Your Choice for Rock paper scissor Game!!!. Type 0 for ROck, 1 for Scissor, 2 for Paper\n"))
print(images[human_choice])
computer_choice = random.randint(0,2)
print(int(computer_choice))
print(images[computer_choice])

if human_choice == computer_choice:
  print("heee Match is tied")
elif  human_choice == 0 and computer_choice == 1:
  print("Great You Won the Game ")

elif  human_choice == 1 and computer_choice == 0:
  print("Oops! You lost the game ")

elif  human_choice == 2 and computer_choice == 0:
  print("Great You Won the Game ")

elif  human_choice == 0 and computer_choice == 2:
  print("Oops! You lost the game ")
  
elif  human_choice == 1 and computer_choice == 2:
  print("Great You Won the Game ")
  
elif  human_choice == 2 and computer_choice == 1:
  print("Oops! You lost the game ")
  

elif  human_choice == 1 and computer_choice == 0:
  print("Oops! You lost the game ")
  
