#rock, paper, scissors game!

import random   #(import random module)

#Possible options
options = ['Rock','Paper','Scissor']

#playerrname
name = input("Enter your name :")

#scores and rounds
CScore = 0 
PScore = 0
GameRounds = 0

#set game to start
gameOn = True
print(f"Welcome {name.title()}")

#Let's play!
while GameRounds < 5:
#let computer choose randomly
  ComputerOption = random.choice(options)

#let player choose
  PlayerOption = input("Enter a choice  (rock, paper, scissors): ").title()

#display both options
  print(f"Computer option :{ComputerOption}")
  print(f"{name.title()} option :{PlayerOption}")

#increase gamerounds by 1
  GameRounds += 1

#if analysis
  if ComputerOption == PlayerOption:
    print("it's a tie!")
  elif (ComputerOption == 'Rock' and PlayerOption == 'Scissor') or (ComputerOption == 'Scissor' and PlayerOption == 'Paper') or (ComputerOption == 'Paper' and ComputerOption == 'Rock'):
    print("Computer wins!")
    CScore += 1
  elif (PlayerOption == 'Rock' and ComputerOption == 'Scissor') or (PlayerOption == 'Scissor' and ComputerOption == 'Paper') or (PlayerOption == 'Paper' and ComputerOption == 'Rock'):
    print(f"{name.title()} wins!")
    PScore += 1
  else:
    print("Choose a valid option to continue.") 

#display scoreboard
  print("-------------------------")
  print("")
  print(f"RoundNumber: {GameRounds}")
  print("------ Scoreboard ------")
  print(f"{name.title()}: {PScore} | Computer: {CScore}")
  print("===============================")
  print("")

#complete on round 5(end loop)
  if GameRounds == 5:
    gameOn = False
    break
#results and display winner
if PScore == CScore:
  print("it's a Draw!")
elif PScore > CScore:
  print(f"Congrats {name.title()}, You won the game!")
else:
  print(f"Oops Computer won the game! Better luck next time {name.title()}!")