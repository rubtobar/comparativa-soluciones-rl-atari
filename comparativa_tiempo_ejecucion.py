import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('tiempos_ejecucion/tiempos_ejecucion.csv', sep=',')

PLOTS_DIR = 'plots/'

# Timepos de ejecución en minutos
a = df.loc[df['algorithm'] == 'DQN']['time_min']//60
b = df.loc[df['algorithm'] == 'A2C']['time_min']//60
c = df.loc[df['algorithm'] == 'PPO']['time_min']//60

labels = ['Seaquest', 'Breakout',
          'Qbert', 'SpaceInvaders']

x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots(figsize=(9.7082, 6))
rects1 = ax.bar(x + width * -1, a, width, label='DQN', color='#0e7a06')
rects2 = ax.bar(x + width * 0, b, width, label='A2C', color='#2329cf')
rects3 = ax.bar(x + width * 1, c, width, label='PPO', color='#c91016')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Tiempo ejecución en minutos')
ax.set_xlabel('Entorno de ejecución')
plt.suptitle('Tiempos de ejecución de los algoritmos para cada entorno')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.ylim([0, 120])

ax.bar_label(rects1, padding=7)
ax.bar_label(rects2, padding=7)
ax.bar_label(rects3, padding=7)

plt.savefig(PLOTS_DIR + 'tiempos_ejecucion.png', transparent=True, dpi=100)
