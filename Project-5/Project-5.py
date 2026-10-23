import time
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def sound(seconds):
  time_elapsed = 0

  print(CLEAR)
  while time_elapsed <= seconds:
    time_remaining = seconds - time_elapsed
    time.sleep(1)
    time_elapsed += 1

    minutes_remaining = time_remaining // 60
    seconds_remaining = (time_remaining - (minutes_remaining*60))

    print(f"{CLEAR_AND_RETURN}Alarm in-->{minutes_remaining:02d}:{seconds_remaining:02d}")

  playsound("Project-5/Alarm.mp3")


a = int(input("Enter minutes for your Alarm Clock: "))
b = int(input("Enter seconds for your Alarm Clock: "))

  
set_time = a*60 + b

sound(set_time)