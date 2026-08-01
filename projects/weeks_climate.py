from func import savefunc
import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt

today = datetime.datetime.now()
week_ago = today - datetime.timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()

# --------------------------------------------------------------

daily_data = data["daily"]

df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)

df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------------------------

plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], label="Max Temperature", marker="o", color="green")
plt.plot(
    df["date"], df["min_temp"], label="Min Temperature", marker="o", color="violet"
)
plt.xlabel("DATE", color="blue")
plt.ylabel("TEMPERATURE (°C)", color="blue")
plt.title(
    "DAILY MAX AND MIN TEMPERATURES FOR THE PAST WEEK",
    fontsize=14,
    fontweight="bold",
    color="red",
)
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

savefunc.function_to_save()

plt.savefig("./projects/data/weeks_climate.png")
plt.show()

# --------------------------------------------------------------

# save to csv

df.to_csv("projects/data/weeks_climate.csv", index=False)
print("Data saved to weeks_climate.csv in the 'data' directory.")
