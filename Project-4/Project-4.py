def get_racers_user():
  racers = 0
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
print(racer)