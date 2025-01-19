import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
data = {
    'Category A': [50, 60, 80, 100],
    'Category B': [40, 50, 60, 80],
    'Category C': [30, 35, 50, 60],
    'Category D': [20, 25, 30, 40],
}
df = pd.DataFrame(data, index=['2020-01', '2020-02', '2020-03', '2020-04'])

fig, ax = plt.subplots(figsize=(8, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
bars = ax.barh(df.columns, df.iloc[0].values, color=colors)

 
def update(frame):
    ax.clear()
    values = df.iloc[frame].values
    ax.barh(df.columns, values, color=colors)
    ax.set_xlim(0, max(df.max()))
    ax.set_title(f'Bar Chart Race: {df.index[frame]}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Categories')

ani = animation.FuncAnimation(
    fig, update, frames=len(df), interval=1000, repeat=True
)

ani.save('bar_chart_race.gif', writer='imagemagick')  # Save as GIF
plt.show()
