import pandas as pd
import matplotlib.pyplot as plt

file_path = 'DCOILWTICO.csv'
df = pd.read_csv(file_path)


df['DATE'] = pd.to_datetime(df['DATE'])
df['DCOILWTICO'] = pd.to_numeric(df['DCOILWTICO'], errors='coerce')
df['DCOILWTICO'] = df['DCOILWTICO'].interpolate(method='linear')

df = df.sort_values(by='DATE').reset_index(drop=True)

mean_values = []
max_values = []
window_dates = []

for i in range(len(df)):
    start = max(0, i - 2)
    end = min(len(df), i + 3)
    window = df.iloc[start:end]

    mean_values.append(round(window['DCOILWTICO'].mean(), 2))
    max_values.append(window['DCOILWTICO'].max())
    window_dates.append(df['DATE'].iloc[i])

df['WINDOW_MEAN'] = mean_values
df['WINDOW_MAX'] = max_values

plt.figure(figsize=(12, 6))
plt.plot(df['DATE'], df['DCOILWTICO'], label='Actual Value', color='blue')
plt.plot(df['DATE'], df['WINDOW_MEAN'], label='Window Mean', color='green')
plt.plot(df['DATE'], df['WINDOW_MAX'], label='Window Max', color='red')

plt.xlabel('Date')
plt.ylabel('Oil Prices')
plt.title('Actual Prices, Window Mean, and Window Max')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

df_100 = df[-100:]

plt.figure(figsize=(12, 6))
plt.plot(df_100['DATE'], df_100['DCOILWTICO'], label='Actual Value', color='blue')
plt.plot(df_100['DATE'], df_100['WINDOW_MEAN'], label='Window Mean', color='green')
plt.plot(df_100['DATE'], df_100['WINDOW_MAX'], label='Window Max', color='red')

plt.xlabel('Date')
plt.ylabel('Oil Prices')
plt.title('Actual Prices, Window Mean, and Window Max: Last 100 days')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()