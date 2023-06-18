import pandas as pd
import numpy as np
import seaborn as sns


base_credit = pd.read_csv('Processamento_Dados\credit_data.csv')

#print(base_credit.head(10))

#print(base_credit.tail(10))

#print(base_credit.describe())

#print(base_credit[base_credit['income'] >= 69995.685578 ])

#print(base_credit[base_credit['loan'] <= 1.377630 ])

sns.countplot(x = base_credit['default'])