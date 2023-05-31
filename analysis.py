# write your code here
import pandas as pd

general_df = pd.read_csv('test/general.csv')
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')

print(general_df.head(20))
print(prenatal_df.head(20))
print(sports_df.head(20))