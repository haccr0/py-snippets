import requests

latitude = 48.8566  # Latitude for Paris
longitude = 2.3522  # Longitude for Paris
response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m")
data = response.json()
print(data)

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m")
    data = response.json()
    return data["hourly"]["temperature_2m"][0] # Return the temperature for the first hour

paris_temp = get_weather(48.8566, 2.3522)
london_temp = get_weather(51.5074, -0.1278)
tokyo_temp = get_weather(35.6895, 139.6917)

print(f"paris: {paris_temp}°C")
print(f"london: {london_temp}°C")
print(f"tokyo: {tokyo_temp}°C")