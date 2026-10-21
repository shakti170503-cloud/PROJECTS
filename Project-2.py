print("      WELCOME TO GUESS THE NUMBER GAME       ")

print("""RULES:
1.You will have 3 chances to guess the number 
2.There are three levels to game: EASY, MEDIUM, HARD
3.Points will displayed at the last
""")

from random import randint

points = 0

number2 = randint(1,50)
number3 = randint(1,100)
def game_easy():
    global points
    number1 = randint(1,16) 
    k = number1
    guess = int(input("Please Enter your first guess: "))
    if guess == k:
      print("You Won!")
      points += 100
    else:
      guess2 = int(input("Please enter your second guess: "))
      if guess2 == k:
        print("You won!")
        points += 60
      else:
        guess3 = int(input("Please enter your third guess: "))
        if guess3 == k:
          print("You won!")
          points += 30
        else:
          print(f"Your number was: {k}")
          print("Hard luck! Better Luck next Time.")
          ask = input("Do you want to play again: ")
          if ask.lower() == "yes":
            game_easy()
          else:
            print("Thank You.")
            quit()
def game_hard(): 
    guess = input("Please Enter your first guess: ")
    if guess == number2:
      print("You Won!")
      point += 100
    else:
      guess = input("Please enter your second guess: ")
      if guess == number2:
        print("You won!")
        points += 80
      else:
        guess = input("Please enter your second guess: ")
        if guess == number2:
          print("You won!")
          points += 50
        else:
          print(f"Your number was: {number2}")
          print("Hard luck! Better Luck next Time.")
          ask = input("Do you want to play again: ")
          if ask.lower() == "yes":
            game_hard()
          else:
            print("Thank You.")
            quit()

a = input("Do yo want to play: ")

if a.lower() == "yes":
  level = input("Please select a level: \nEASY\tMEDIUM\tHARD: ").lower()
  if level == "easy":
    print("You have to guess a number between 1 to 15")
    game_easy()
  elif level == "hard":
    print("You have to guess a number between 1 to 52")
    game_hard()    

  print(f"You have scored: {points}")


else:
  print("Thank you for Coming!")
  quit()
