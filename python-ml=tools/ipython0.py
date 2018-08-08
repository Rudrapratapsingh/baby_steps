import pandas as pd
temp1 = pd.read_csv("/root/Desktop/data/template.csv")
temp1 = temp1[['COUNTRY','CODE']]
temp1.columns = ['Country','Code']
temp1.head()
print temp1

