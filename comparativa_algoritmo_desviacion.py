import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


PPO = 'red'
A2C = 'blue'
DQN = 'green'

PLOTS_DIR = 'plots/'

evaluation_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".npz"):
            evaluation_files.append(os.path.join(root, file))


for evaluation_file in evaluation_files:
    data = np.load(evaluation_file)

    mean = []
    std = []
    for i in range(len(data['timesteps'])):
        mean.append(np.mean(data['results'][i]))
        std.append(np.std(data['results'][i]))
    #    print(str(np.mean(data['results'][i])) +
    #          ' +/- ' + str(np.std(data['results'][i])))

    m_s = [sum(x) for x in zip(mean, std)]
    m_ss = [x1 - x2 for (x1, x2) in zip(mean, std)]

    timesteps = data['timesteps'].tolist()

    x = np.array(timesteps)
    y = np.array(mean)
    y_std_top = np.array(m_s)
    y_std_bot = np.array(m_ss)

    # define x as 200 equally spaced values between the min and max of original x
    xnew = np.linspace(x.min(), x.max(), 1000)

    # define spline mean
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(xnew)
    # define spline top
    spl_top = make_interp_spline(x, y_std_top, k=3)
    y_smooth_top = spl_top(xnew)
    # define spline bot
    spl_bot = make_interp_spline(x, y_std_bot, k=3)
    y_smooth_bot = spl_bot(xnew)

    plt.figure(figsize=(9.7082, 6))  # Proporción aurea
    algoritmo = str(evaluation_file).split('\\')[1]
    entorno = str(evaluation_file).split('\\')[2][:-2]
    color = ''
    if algoritmo == 'PPO':
        color = PPO
    elif algoritmo == 'A2C':
        color = A2C
    elif algoritmo == 'DQN':
        color = DQN
    plt.plot(xnew, y_smooth, color, label="Recompensa media")
    plt.plot(xnew, y_smooth_top, 'gray')
    plt.plot(xnew, y_smooth_bot, 'gray')
    plt.fill_between(x=xnew, y1=y_smooth_top,
                     y2=y_smooth_bot,  color='gray', alpha=0.2, label="Desviación estándar")
    plt.xlabel("Ciclo de entrenamiento")
    plt.ylabel("Recompensa obtenida")
    plt.legend(loc='lower right')

    plt.suptitle("Evolución de la recompensa obtenida en el entrenamiento",
                 fontsize=14, fontweight='bold')
    plt.title("Algoritmo: " + algoritmo.upper() + ", Entorno: " + entorno)
    try:
        os.makedirs(PLOTS_DIR)
        print("Directory ", PLOTS_DIR,  " Created ")
    except FileExistsError:
        print("Directory ", PLOTS_DIR,  " already exists")
    plt.savefig(PLOTS_DIR + algoritmo.upper() + '_' + entorno + '.png',
                transparent=True, dpi=1000)
