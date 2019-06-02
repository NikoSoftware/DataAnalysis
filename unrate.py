import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    unrate = pd.read_csv("file/UNRATE.csv")
    unrate['DATE'] = pd.to_datetime(unrate['DATE'])
    first_twelve = unrate[0:100]
    plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
    plt.xticks(rotation=30)
    plt.show()


if __name__ == '__main__':
    main()
