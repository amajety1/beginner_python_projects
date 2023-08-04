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
import random
#Write your code below this line 👇
rps = [0,1,2]

selection = int(input("Enter 0 for rock, 1 for pap, 2 for scissors.\n"))
if selection not in rps:
  print("Wrong number")
else:
  ran_rps = random.randint(0,2)
print("You chose:\n\n\n")  

if selection==0:
  print(rock)
elif selection==1:
  print(paper)
elif selection==2:
  print(scissors)

print("Computer chose:\n\n\n")
if ran_rps==0:
  print(rock)
elif ran_rps==1:
  print(paper)
elif ran_rps==2:
  print(scissors)

if selection==ran_rps:
  print('It is a draw')
if selection==0 and ran_rps==1: 
  print("Loser")
if selection==1 and ran_rps==2: 
  print("Loser")
if selection==2 and ran_rps==0: 
  print("Loser")

if selection==1 and ran_rps==0: 
  print("Winner")
if selection==2 and ran_rps==1: 
  print("winner")
if selection==0 and ran_rps==2: 
  print("winner")

