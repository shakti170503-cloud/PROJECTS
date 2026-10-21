# QUIZ GAME
import time


print("WELCOME TO THIS QUIZ GAME")
print("""RULES:
1.There will 10 questions
2.Each question is worth 10 points is answered correctt
3.No negative marking
4.50 points is the passing marks
""")
a = input("Are you ready to play\t Enter Y for yes and N for no: ")

points = 0
if a.capitalize() == "Y":
  print("Be ready your 1st question will be displayed in 5 seconds.")
  time.sleep(5)
  q1 = input("1.What is the Area of a Circle\nA.πr\tB.2πr\nC.πr^2\tD.πrh -->Ans:  ")
  print()
  if q1.capitalize() == "C":
    points += 10
  else:
    print("Wrong Answer, Correct answer is C.")
    print()
  q2 = input("2.What is the Capital of Assam\nA.Guwahati\tB.Dispur\nC.Dibrugargh\tD.Tezpur -->Ans:  ")
  print()
  if q2.capitalize() == "B":
    points += 10
  else:
    print("Wrong Answer, Correct answer is B.")
    print()
  q3 = input("3.What is Longitude passes through 180'\nA.Prime Meridian\tB.Equator\nC.Anti Meridian\tD.Tropic of Cancer -->Ans:  ")
  print()
  if q3.capitalize() == "C":
    points += 10
  else:
    print("Wrong Answer, Correct answer is C.")
    print()
  q4 = input("4.What is the Area of a Circle\nA.πr\tB.2πr\nC.πr^2\tD.πrh -->Ans:  ")
  print()
  if q4.capitalize() == "C":
    points += 10
  else:
    print("Wrong Answer, Correct answer is C.")
    print()
  q5 = input("5.What is the Full Form of AI\nA.Artificial Intelligence\tB.Air Inversion\nC.Anti Isobar\tD.Auto Initiative -->Ans:  ")
  print()
  if q5 .capitalize() == "A":
    points += 10
  else:
    print("Wrong Answer, Correct answer is A.")
    print()
  q6 = input("6.How many Mbs are in 2Gbs\nA.1024\tB.3096\nC.4084\tD.2048 -->Ans:  ")
  print()
  if q6.capitalize() == "D":
    points += 10
  else:
    print("Wrong Answer, Correct answer is D.")
    print()
  q7 = input("7.Who is the G.O.A.T?\nA.CR7\tB.LM10\nC.NY11\tD.Pele10 -->Ans:  ")
  print()
  if q7.capitalize() == "A":
    points += 10
  else:
    print("Wrong Answer, Correct answer is A.")
    print()
  q8 = input("8.What is the Hungary\nA.Budapest\tB.Berlin\nC.Frankfurt\tD.Munich -->Ans:  ")
  print()
  if q8.capitalize() == "A":
    points += 10
  else:
    print("Wrong Answer, Correct answer is A.")
    print()
  q9 = input("9.Who is known as Father of Indian Constitution\nA.Mahatma Gandhi\tB.Jawaharlal Nehru\nC.Indira Gandhi\tD.Bhimrao Ambedkar -->Ans:  ")
  print()
  if q9.capitalize() == "D":
    points += 10
  else:
    print("Wrong Answer, Correct answer is D.")
    print()
  q10 = input("10.What is the Chemical formula of Hydrogen Peroxide\nA.H202\tB.H2O3\nC.HO2\tD.H20 -->Ans:  ")
  print()
  if q10.capitalize() == "A":
    points += 10
  else:
    print("Wrong Answer, Correct answer is A.")
    print()

else:
  print("Thank you for Coming!")
  quit()

print("**CONGRATULATIONS YOU HAVE COMPLETED THE QUIZ**")
print(f"You score is: {points}")
print(f"Total numbers of correct ans. {int(points/10)}/10")
a = "PASSED" if points >= 50 else "FAILED"
print(a)
