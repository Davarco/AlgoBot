import pandas as pd
import statsmodels.api as sm
import pylab as pl

df = pd.read_csv("NEW.csv")
print(df.head())
df.columns  = ["Undervalued", "200avg", "100avg", "50avg"]
print(df.columns)
print(df.describe)

df.hist()
pl.show()


cols_to_keep = ['Undervalued', '200avg', '100avg', '50avg']
data = df[cols_to_keep]
print(data.head())

data['intercept'] = 1.0

train_cols = data.columns[1:]

logit = sm.Logit(data['Undervalued'], data[train_cols])

result = logit.fit()

print(result.summary())


print(result.predict([0.8, 0.9, 0.95, 1]))
