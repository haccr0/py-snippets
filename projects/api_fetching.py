import requests
import os

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")
temperature = response.json()

function = temperature['hourly']["temperature_2m"][0]

celsius_scale = f"It is {function} degrees celsius"

if function > 30:
    text_1 = "it is hot"
    print(f"{text_1.title()}. {celsius_scale}")
elif function <=30 and function >=20:
    text = "perfect weather!"
    print(f"{text.upper()}. {celsius_scale}")
elif function == 200:
    text_2 = "it is very cold"
    print(f"{text_2.title()}. {celsius_scale}")
else:
    txt = "this is not gonna happ   en"
    print(txt.upper())