import turtle
import random as r

COLORS = ["yellow","red","blue","cyan","pink","orange","brown","black","green","purple"]
WIDTH = 500
HEIGHT = 500

def get_racers_user():
  ask = input("Do you Want to Play(yes/no): ").strip().lower()
  if ask != "yes":
    raise SystemExit
  else:
    while True:
      racers = input("Enter the number of racers,You want to race(2-10): ")
      if racers.isdigit():
        racers = int(racers)
        if 2 <= racers <= 10:
          return racers
        else:
          print("The number must be in range!")
          continue
      else:
        print("Invalid! Please enter a correct choice. :)")

racer = get_racers_user()
print(f"Total racers: {racer}")

def display_screen():
  screen = turtle.Screen()
  screen.setup(WIDTH,HEIGHT)
  screen.title("Turtle Racing!")

r.shuffle(COLORS)
color = COLORS[:racer]
print(color)

def race(color):
  turtles = display_turtle(color)
  while True:
    for i,racers in enumerate(turtles):
      num = r.randrange(1,20)
      racers.forward(num)

      _,y = racers.pos()
      if y >= (HEIGHT//2) - 20:
        return color[i]


def display_turtle(color):
  turtles = []
  spacingx = WIDTH / (len(color)+1)
  for i,char in enumerate(color):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(char)
    t.left(90)
    t.penup()
    t.setpos(-WIDTH/2+(i+1)*spacingx,-HEIGHT/2 + 20)
    t.pendown()
    turtles.append(t)

  return turtles

def draw_lines():
    line = turtle.Turtle()
    line.hideturtle()
    line.speed(0)
    line.penup()

    line.goto(-WIDTH // 2, -HEIGHT // 2 + 40)
    line.pendown()
    line.forward(WIDTH)

    line.penup()
    line.goto(-WIDTH // 2, HEIGHT // 2 - 40)
    line.pendown()
    line.forward(WIDTH)

display_screen()
draw_lines()
winner = race(color)
print(f"The WINNER is: {winner}")
turtle.done()

