import pandas as pd
import matplotlib.pyplot as plt


def main():
    unrate = pd.read_csv("file/UNRATE.csv")
    unrate['DATE'] = pd.to_datetime(unrate['DATE'])
    plt.plot(unrate[0:5]['DATE'], unrate[0:5]['VALUE'], c='red')
    plt.plot(unrate[5:10]['DATE'], unrate[5:10]['VALUE'], c='blue')
    plt.show()


def scatter():
    unrate = pd.read_csv("file/UNRATE.csv")
    unrate['DATE'] = pd.to_datetime(unrate['DATE'])
    first_data = unrate[0:12]
    fig, ax = plt.subplots()
    ax.scatter(first_data['DATE'], first_data['VALUE'])
    ax.set_xlabel('DATE')
    ax.set_ylabel('VALUE')
    plt.show()


def main1():
    fig = plt.figure(figsize=(10, 6))
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 4)

    plt.show()


if __name__ == '__main__':
    scatter()
