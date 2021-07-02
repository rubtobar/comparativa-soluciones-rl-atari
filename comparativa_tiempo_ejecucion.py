import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('tiempos_ejecucion/tiempos_ejecucion.csv', sep=',')

PLOTS_DIR = 'plots/'

a = df.loc[df['algorithm'] == 'DQN']['time_min']
b = df.loc[df['algorithm'] == 'A2C']['time_min']
c = df.loc[df['algorithm'] == 'PPO']['time_min']

labels = ['SeaquestNoFrameskip-v4', 'BreakoutNoFrameskip-v4',
          'QbertNoFrameskip-v4', 'SpaceInvadersNoFrameskip-v4']
 
x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x + width * 0, a, width, label='DQN')
rects2 = ax.bar(x + width * 1, b, width, label='A2C')
rects3 = ax.bar(x + width * 2, c, width, label='PPO')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

plt.savefig(PLOTS_DIR + 'tiempos_ejecucuion.png', transparent=True, dpi=100)
