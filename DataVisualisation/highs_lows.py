import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "sitka_weather_2014.csv"


def convert_to_celsius(temp):
    temp = ((int(temp) - 32) * 5) / 9
    return temp


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        highs.append(int(convert_to_celsius(row[1])))
        low = int(convert_to_celsius(row[3]))
        lows.append(low)
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

fig = plt.figure(dpi=150, figsize=(10, 6))

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("The highest and lowest temperature of the day,2014", fontsize=24)
plt.xlabel('', fontsize=16)

plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
plt.show()
