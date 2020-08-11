from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('netflixviewinghistory_yo.csv')
# print(df)

df['show_title'] = [s.partition(':') [0] for s in df.Title]
my_titles = list(df['show_title'])
df.head()
# print(df)

top_views = pd.Series(my_titles).value_counts().nlargest(10)

N = len(top_views)
x = np.arange(N)

colors = plt.get_cmap('autumn')

plt.figure(figsize=(10, 6))
plt.bar(top_views.index, top_views.values, color=colors(x/N))
plt.ylabel('Freq.', fontsize=12)
plt.xlabel('Show Titles', fontsize=12)
plt.xticks(rotation=30, ha='right', fontsize=11)
plt.title('My Top 10 Shows on Netflix', fontsize=15)

plt.savefig('top_10_shows_bar_yo.png', dpi=300, bbox_inches='tight')
plt.show()

df['date'] = pd.to_datetime(df['Date'])
df['weekday'] = df['date'].dt.day_name()
# print(df)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df.weekday = pd.Categorical(df['weekday'], categories=weekdays, ordered=True)
by_day = df.sort_values('weekday')['weekday'].value_counts().sort_index()

N = len(by_day)
x = np.arange(N)

colors = plt.get_cmap('autumn').reversed()

plt.figure(figsize=(10, 6))
plt.bar(by_day.index, by_day.values, color=colors(x/N))
plt.ylabel('Freq.', fontsize=12)
plt.xlabel('Day of the Week', fontsize=12)
plt.title('Netflix Pattern Viewing by Day of the Week', fontsize=15)

plt.savefig('freq_by_day_yo.png', dpi=300, bbox_inches='tight')
plt.show()
