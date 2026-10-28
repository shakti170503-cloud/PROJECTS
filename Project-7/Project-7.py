from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://v3.football.api-sports.io"
API_KEY = "fe3f8fa3fc2065c6f6c44397682633a0"

printer = PrettyPrinter()


def get_api():
  endpoint = "/fixtures?team=541&league=140&season=2024"
  headers = {"x-apisports-key":API_KEY}

  url = (BASE_URL + endpoint )
  data = get(url,headers=headers).json()

  matches = data["response"]

  print("Total matches:", len(matches))

  for match in matches:
      home = match["teams"]["home"]["name"]
      away = match["teams"]["away"]["name"]

      home_goals = match["goals"]["home"]
      away_goals = match["goals"]["away"]

      status = match["fixture"]["status"]["short"]
      print("------------------------------------------------------")
      print(f"{home} {home_goals} - {away_goals} {away} ({status})")
      print("------------------------------------------------------")

get_api()