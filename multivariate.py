import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

loansData = pd.read_csv('https://resources.lendingclub.com/LoanStats3c.csv', index_col=0)

df['homeOwnership_ord'] = pd.Categorical(df.home_ownership).labels
est = smf.ols(formula='annual_inc ~ int_rate + C(homeOwnership_ord)', data=df).fit()
est.summary()
