print("      WELCOME TO GUESS THE NUMBER GAME       ")

print("""RULES:
1.You will have 3 chances to guess the number 
2.There are three levels to game: EASY, MEDIUM, HARD
3.Points will displayed at the last
""")

from random import randint

points = 0

def game_easy():
    global points
    number1 = randint(1,15) 
    k = number1
    guess1 = int(input("Please Enter your first guess: "))
    if guess1 == k:
      print("You Won!")
      points += 100
      print(f"You have scored: {points}")
      ask_player_again()
    else:
      print("LOWER" if guess1<k else "HIGHER")
      guess2 = int(input("Please enter your second guess: "))
      if guess2 == k:
        print("You won!")
        points += 60
        print(f"You have scored: {points}")
        ask_player_again()
      else:
        print("LOWER" if guess2<k else "HIGHER")
        guess3 = int(input("Please enter your third guess: "))
        if guess3 == k:
          print("You won!")
          points += 30
          print(f"You have scored: {points}")
          ask_player_again()
        else:
          print(f"Your number was: {k}")
          print(f"You have scored: {points}")
          print("Hard luck! Better Luck next Time.")
          ask = input("Do you want to play again: ")
          if ask.lower() == "yes":
            ask_player()

          else:
            print("Thank You. :)")
            quit()

def game_medium(): 
    global points
    number2 = randint(1,50)
    k = number2
    guess1 = int(input("Please Enter your first guess: "))
    if guess1 == k:
      print("You Won!")
      points += 100
      print(f"You have scored: {points}")
      ask_player_again()
    else:
      print("LOWER" if guess1<k else "HIGHER")
      guess2 = int(input("Please enter your second guess: "))
      if guess2 == k:
        print("You won!")
        points += 70
        print(f"You have scored: {points}")
        ask_player_again()
      else:
        print("LOWER" if guess2<k else "HIGHER")
        guess3 = int(input("Please enter your third guess: "))
        if guess3 == k:
          print("You won!")
          points += 40
          print(f"You have scored: {points}")
          ask_player_again()
        else:
          print(f"Your number was: {k}")
          print(f"You have scored: {points}")
          print("Hard luck! Better Luck next Time.")
          ask = input("Do you want to play again: ")
          if ask.lower() == "yes":
            ask_player()
          else:
            print("Thank You. :)")
            quit()

def ask_player():
  
    level = input("Please select a level: \nEASY\t\tMEDIUM\t\tHARD: ").lower()
    if level == "easy":
      print("You have to guess a number between 1 to 15")
      game_easy()
    elif level == "medium":
      print("You have to guess a number between 1 to 50")
      game_medium()    
    elif level == "hard":
      print("You have to guess a number between 1 to 100")
      game_hard()

    # print(f"You have scored: {points}")

def game_hard(): 
    global points
    number3 = randint(1,100)
    k = number3
    guess1 = int(input("Please Enter your first guess: "))
    if guess1 == k:
      print("You Won!")
      points += 100
      print(f"You have scored: {points}")
      ask_player_again()
    else:
      print("LOWER" if guess1<k else "HIGHER")
      guess2 = int(input("Please enter your second guess: "))
      if guess2 == k:
        print("You won!")
        points += 80
        print(f"You have scored: {points}")
        ask_player_again()
      else:
        print("LOWER" if guess1<k else "HIGHER")
        guess3 = int(input("Please enter your third guess: "))
        if guess3 == k:
          print("You won!")
          points += 50
          print(f"You have scored: {points}")
          ask_player_again()
        else:
          print(f"Your number was: {k}")
          print(f"You have scored: {points}")
          print("Hard luck! Better Luck next Time.")
          ask = input("Do you want to play again: ")
          if ask.lower() == "yes":
            ask_player_again()
          else:
            print("Thank You. :) ")
            quit()


def ask_player_again():
    
    ag = input("Do you wanna play again: ").lower()
    if ag == "yes":
      level = input("Please select a level: \nEASY\t\tMEDIUM\t\tHARD: ").lower()
      if level == "easy":
        print("You have to guess a number between 1 to 15")
        game_easy()
      elif level == "medium":
        print("You have to guess a number between 1 to 50")
        game_medium()    
      elif level == "hard":
        print("You have to guess a number between 1 to 100")
    else:
      print("Thank You! Well Played :) ")


a = input("Do yo want to play: ")
if a.lower() == "yes":
  ask_player()

else:
  print("Thank you for Coming!")
  quit()


