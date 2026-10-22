import random as r
print("******WELCOME TO GUESS THE ROLL THE DICE GAME******")

print("""RULES:
1.A player can any number of times and each roll will added to his|her points
2.If the player rolls 1 his|her turn will be terminated and points will convert to 0
3.Whoever scores 50 points first will win
""")
def roll():
    
  MIN_VALUE = 1
  MAX_VALUE = 6
  roll= r.randint(MIN_VALUE,MAX_VALUE)
  return roll

points = {}


ask_player = input("Do you want you play(yes/no)? ").strip().lower()
if ask_player == "yes":
  while True:
    players = input("Enter the Number of Players(2-4)")
    if players.isdigit():
      players = int(players)
      if 2 <= players <= 4:
        print(f"Players: {players}")
        break
      else:
        print("Invalid Choice! Please enter in the given range :)")
        continue
else:
  print("Thank You! Bye:)")
  raise SystemExit

for i in range (players): 
  points[f"Player{i+1}"] = 0
  

print(f"Scores-->{points}")

while max(points.values()) < 50:
  
  for chance in range(players):
     while True:
      print(f"\nPlayer{chance+1},Total Score: ",end="")
      print(points[f"Player{chance+1}"])
      roll_now = input("Do you wanna roll the Dice(y/n)? ").strip().lower()
      if roll_now != "y":
        break
      num = roll()
      if num == 1:
        print("You rolled a 1!Turn done!")
        points[f"Player{chance+1}"] = 0
        print(f"Player{chance+1},Current Score: ",end="")
        print(points[f"Player{chance+1}"])
        break
      else:
        
        print(f"\nPlayer{chance+1},Playing....")
        print(f"Dice rolled: {num}")
        points[f"Player{chance+1}"] += num
        print(f"Player{chance+1},Current Score: ",end="")
        print(points[f"Player{chance+1}"])

for player_name in points.keys():
  if points[player_name] == max(points.values()):
    print(f"The winner is: {player_name},Score: {points[player_name]}")
    
  
print(f"Final Score-->{points}")