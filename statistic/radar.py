import numpy as np
from math import pi
import matplotlib.pyplot as plt

def radar_chart(df, title, img):
    categories = list(df)[1:]
    N = len(categories)
    plt.clf()

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values = df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    plt.title(title, size=11, color='grey', y=1.1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    # Draw ylabels
    limit = max(values) + 100
    ax.set_rlabel_position(30)
    plt.yticks(np.arange(0, limit, 1000), color='grey', size=0)
    plt.ylim(0, limit)

    # Plot data
    color = 'green'
    ax.plot(angles, values, linewidth=1, linestyle='solid', color=color)

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.savefig(img)
    # plt.show()