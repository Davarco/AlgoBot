import pandas as pd
import statsmodels.api as sm
import numpy as np


def train():

    # Get data
    df = pd.read_csv("input/train.csv")
    df.columns = ["200avg", "100avg", "50avg", "Undervalued"]
    # print(df.head())

    # Redistribute the data
    df.insert(0, 'Intercept', 1)
    # print(df.head())

    # Train the data
    train_cols = df.columns[0:4]
    # print(df[train_cols].head())
    # print(df['Undervalued'].head())
    logistic = sm.Logit(df['Undervalued'], df[train_cols])
    result = logistic.fit()

    # Show results
    print(result.summary())
    return result


def test(params):
    
    # Get csv data
    df = pd.read_csv("input/test.csv")
    df.columns = ["200avg", "100avg", "50avg", "Undervalued"]
    matrix = np.matrix(df)

    # Store data
    acc = 0
    total = 0

    # Go through matrix and make predictions
    for row in matrix:
        ma_200 = row[0, 0]
        ma_100 = row[0, 1]
        ma_50 = row[0, 2]
        result = row[0, 3]
        pred = params.predict([ma_200, ma_100, ma_50, 1])[0]

        # Add to count if accurate
        if pred > 0.5 and result == 1:
            acc += 1
        if pred < 0.5 and result == 0:
            acc += 1
        total += 1

    # Get percent correct
    percent = acc/total
    print(percent)


def main():

    # Train data
    params = train()

    # Test data
    test(params)


if __name__ == '__main__':
    main()
