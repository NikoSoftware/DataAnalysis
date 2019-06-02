import pandas as pd


def main():
    food_info = pd.read_csv("file/food_info.csv")
    #print(type(food_info))
    #print(food_info.dtypes)
    print(food_info.head(5))
    print(food_info.shape)
    print(food_info.loc[0:3])  #0到3行


if __name__ == '__main__':
    main()
