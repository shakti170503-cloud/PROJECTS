import random

ALPHABETS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
TRIES = 5
CODE_LENGTH = 5

if __name__ == "__main__":
  def generate_word():

    code = []

    with open("Project-9/Project-9-words.txt","r") as f:
      words = f.read().split(",")
    
    guess_word = random.choice(words).upper()
    for i in guess_word:
      code.append(i)

    return code

  def guess_word():
    while True:
      guess = input("Enter your Word(Space separated): ").upper().split(" ")

      if len(guess) != 5:
        print(f"The guess word should be of {CODE_LENGTH} letters .....Please try again")
        continue

      for word in guess:
        if word not in ALPHABETS:
          print(f"Invalid Alphabet!..{word}...Try Again!!")
          break
      else:
        break

    return guess

  def check_word(guess_word,real_word):
    alphabet_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for letter in real_word:
      if letter not in alphabet_counts:
        alphabet_counts[letter] = 0

      alphabet_counts[letter] += 1

    for guess_letter , real_letter in zip(guess_word,real_word):
      if guess_letter == real_letter:
        correct_pos += 1
        alphabet_counts[guess_letter] -= 1

    for guess_letter , real_letter in zip(guess_word,real_word):
      if guess_letter in alphabet_counts and alphabet_counts[guess_letter] > 0:
        incorrect_pos += 1
        alphabet_counts[guess_letter] -= 1

    return correct_pos , incorrect_pos

  def wordle_game():

    print(f"WELCOME TO WORDLE, You have {TRIES} Tries to guess the word")
    print("Attempt no. 1")
    
    word = generate_word()
    for attempts in range(1,TRIES+1):
      guess = guess_word()
      correct_pos ,incorrect_pos = check_word(guess,word)

      if correct_pos == CODE_LENGTH:
        print(f"You guessed the word in {attempts} tries")
        break
      
      print(f"Correct-Position:{correct_pos}|Incorrect-Position:{incorrect_pos}")
      print(f"\nAttempt no. {attempts+1}")

    else:
      print("You're out of tries!....Your word was: ",*word)
     

if __name__ == "__main__":
  a = input("Do you want to play the Wordle(y/n): ").strip().lower()
  if a == "y":
   wordle_game()
   while True:
    b = input("Do you want to play the Wordle Again?(y/n): ").strip().lower()
    if b == "y":
      wordle_game()
    else:
      print("Thank you for playing!!")
      break
  else:
    print("Thank you for coming!!")


    