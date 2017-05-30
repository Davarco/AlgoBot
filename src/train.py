import pandas as pd
import statsmodels.api as sm
import pylab as pl


def main():

    # Get data 
    df = pd.read_csv("input/train.csv")
    print(df.head())
    df.columns = ["Undervalued", "200avg", "100avg", "50avg"]
    print(df.columns)
    print(df.describe)

    # Show data
    df.hist()
    pl.show()

    # Redistribute the data
    cols_to_keep = ['Undervalued', '200avg', '100avg', '50avg']
    data = df[cols_to_keep]
    print(data.head())
    data['intercept'] = 1.0

    # Train the data
    train_cols = data.columns[1:]
    logit = sm.Logit(data['Undervalued'], data[train_cols])
    result = logit.fit()

    # Show results
    print(result.summary())
    print(result.predict([0.8, 0.9, 0.95, 1]))

if __name__ == '__main__':
    main()
