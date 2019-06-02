import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def main():
    sns.set()
    sinplot()
    sns.despine(left=True)
    plt.show()


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


def colors():
    sns.set()
    sns.despine(left=True)
    sns.palplot(sns.color_palette("hls"), 12)
    plt.show()




if __name__ == '__main__':
    colors()
