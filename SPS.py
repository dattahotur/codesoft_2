import random

game1 = str(input("Rock, Paper, Scissor? ")).capitalize()
game2 = random.randint(1,3)

if game2 == 1:
     game2 = "Rock"
elif game2 == 2:
     game2 = "Papper"
elif game2 == 3:
     game2 = "Scissor"

print("Computer: ", game2)

if game1 == game2:
     print("Its a tie...!!")
elif (game1 == "Rock" and game2 == "Scissor") or (game1 == "Paper" and game2 == "Rock") or (game1 == "Scissor" and game2 == "Paper"):
     print("YOU WON....!!")
else:
     print("YOU LOOSE....!!")
     
