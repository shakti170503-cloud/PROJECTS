#***PASSWORD GENERATOR***#
import string
import secrets

def pwd_generator(min_length,numbers=True,special_char=True):
  letters= string.ascii_letters
  digits = string.digits
  special = string.punctuation

  characters = letters
  if numbers:
    characters += digits
  if special_char:
    characters += special

  pwd = ""
  meets_criteria = False
  has_num = False
  has_special = False

  while not meets_criteria or len(pwd) < min_length:
    new_characters = secrets.choice(characters)
    pwd += new_characters

    if new_characters in digits:
      has_num = True
    elif new_characters in special:
      has_special = True

    meets_criteria = True
    if numbers:
      meets_criteria = has_num
    if special_char:
      meets_criteria = meets_criteria and has_special

  print(pwd, len(pwd), meets_criteria)
  return pwd
  
min_length = int(input("Enter the Minium length for your password: "))
has_num = input("Do you wanna add numbers(y/n): ").strip().lower() == "y"
has_special = input("Do you wanna add special characters(y/n): ").strip().lower() == "y"


pwd = pwd_generator(min_length,has_num,has_special)
print(pwd)