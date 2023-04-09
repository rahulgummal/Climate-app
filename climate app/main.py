import json
import requests
import pyttsx3

city = input("Enter name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=4c70dd7d8abf454095e214554230804&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
temp_c = wdic["current"]["temp_c"]

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Convert the temperature to a string and format it as "X degrees Celsius"
temp_str = f"{temp_c:.0f} degrees Celsius"

# Use the engine to speak the temperature
engine.say(f"The temperature in {city} is {temp_str}")
engine.runAndWait()
