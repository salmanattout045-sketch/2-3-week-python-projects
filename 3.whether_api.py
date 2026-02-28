import datetime as dt
import json

import requests

from weather_and_csv import CSV_FILE

site_url = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "Your_API"
CITY = "Warsaw"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


url = site_url + "appid=" + API_KEY + "&q=" + CITY + "&lang=en"

response = requests.get(url).json()
print(response)

temp_kelvin = response["main"]["temp"]
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]

sunrise_time = dt.datetime.utcfromtimestamp(
    response["sys"]["sunrise"] + response["timezone"]
)
sunset_time = dt.datetime.utcfromtimestamp(
    response["sys"]["sunset"] + response["timezone"]
)

print(f"Temperature in {CITY}: {temp_celsius:.2f}c or {temp_fahrenheit}f")
print(f"Feels like in {CITY}: {feels_like_celsius:.2f}c or {feels_like_fahrenheit}f")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind speed in {CITY}: {wind_speed} m/s")
print(f"General weather in {CITY}: {description}")
print(f"Sunrise time in {CITY}: {sunrise_time}")
print(f"Sunset time in {CITY}: {sunset_time}")


#2. exersice 2

import requests
import csv

def get_joke():
    # Send GET request to the Joke API
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    data = response.json()
    return {
        "setup": data["setup"],
        "punchline": data["punchline"]
    }

for i in range(3):
    joke=get_joke()
    print(f"joke  {i+1} :")
    print(joke["setup"])
    print(joke["punchline"])
    print("---")

JOKE="joke.csv"
with open("joke.csv", "w",newline="") as f:
    write=csv.writer(f)

    write.writerow(["joke","setup","punchline"])
    #for


#Exercise 3: Cryptocurrency API function
import requests
response = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin")
data = response.json()


with open("bitcoin.json", "w") as f:
    json.dump(data, f, indent=4)

# or print(data.keys())

import requests

import requests

import csv
def crypto(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id.lower()}"

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Could not fetch data for {coin_id}")

    data = response.json()

    # Safely extract name, price (USD), market cap (USD)
    name = data.get("name", coin_id)
    market_data = data.get("market_data", {})
    current_price = market_data.get("current_price", {}).get("usd", None)
    market_cap = market_data.get("market_cap", {}).get("usd", None)

    return {
        "name": name,
        "current_price_usd": current_price,
        "market_cap_usd": market_cap
    }


# Example usage:
coins = ["bitcoin", "ethereum", "dogecoin"]
results = []

for coin in coins:
    try:
        info = crypto(coin)
        results.append(info)
    except Exception as e:
        print(f"Error for {coin}: {e}")

for item in results:
    print(item)

crypto_csv= "crypto"
with open("crypto.csv", "w",newline="") as f:
    writing = csv.writer(f)

    writing.writerow(["name","current_price_usd","market_cap_usd"])
    for item in results:
        writing.writerow([
            item["name"],
            item["current_price_usd"],
            item["market_cap_usd"]
        ])


import requests
import json
from datetime import datetime as dt

# ================= CONFIG =================




    




