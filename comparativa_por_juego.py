import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


PPO = 'red'
A2C = 'blue'
DQN = 'green'

PLOTS_DIR = 'plots/'

games = ['SeaquestNoFrameskip-v4',
         'BreakoutNoFrameskip-v4',
         'QbertNoFrameskip-v4',
         'SpaceInvadersNoFrameskip-v4']

evaluation_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".npz"):
            evaluation_files.append(os.path.join(root, file))

for ngame in range(len(games)):
    # Una grafica comparativa por cada juego
    # Una línea por cada algorítmo
    plt.figure(figsize=(9.7082, 6))  # Proporción aurea

    for nfile in range(ngame, len(evaluation_files), 4):
        data = np.load(evaluation_files[nfile])
        mean = []
        for i in range(len(data['timesteps'])):
            mean.append(np.mean(data['results'][i]))

        timesteps = data['timesteps'].tolist()

        x = np.array(timesteps)
        y = np.array(mean)

        # define x as 200 equally spaced values between the min and max of original x
        xnew = np.linspace(x.min(), x.max(), 1000)

        # define spline mean
        spl = make_interp_spline(x, y, k=3)
        y_smooth = spl(xnew)

        algoritmo = str(evaluation_files[nfile]).split('\\')[1].upper()
        color = ''
        if algoritmo == 'PPO':
            color = PPO
        elif algoritmo == 'A2C':
            color = A2C
        elif algoritmo == 'DQN':
            color = DQN
        plt.plot(xnew, y_smooth, color, label=algoritmo)

    entorno = str(evaluation_files[ngame*(len(games)-1)]).split('\\')[2][:-2]
    plt.suptitle('Comparativa de algoritmos en el entorno ' + entorno)
    plt.xlabel("Ciclo de entrenamiento")
    plt.ylabel("Recompensa obtenida")
    plt.legend(loc='lower right')
    try:
        os.makedirs(PLOTS_DIR)
        print("Directory ", PLOTS_DIR,  " Created ")
    except FileExistsError:
        print("Directory ", PLOTS_DIR,  " already exists")
    plt.savefig(PLOTS_DIR + entorno + '.png', transparent=True, dpi=1000)
