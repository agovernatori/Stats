import pandas as pd

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split('.') for i in data]
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
df['Alcohol'].mean()

Print "The range for the Alcohol dataset is " + max(df['Alcohol']) - min(df['Alcohol'])
Print "The mean for the Alcohol dataset is " + df['Alcohol'].mean()
Print "The median for the Alcohol dataset is " + df['Alcohol'].median()
Print "The variance for the Alcohol dataset is " + df['Alcohol'].var()
Print "The standard deviation for the Alcohol dataset is " + df['Alcohol'].std()

Print "The range for the Tobacco dataset is " + max(df['Tobacco']) - min(df['Tobacco'])
Print "The mean for the Tobacco dataset is " + df['Tobacco'].mean()
Print "The median for the Tobacco dataset is " + df['Tobacco'].median()
Print "The variance for the Tobacco dataset is " + df['Tobacco'].var()
Print "The standard deviation for the Tobacco dataset is " + df['Tobacco'].std()