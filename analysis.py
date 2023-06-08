# write your code here
import pandas as pd

general_df = pd.read_csv('test/general.csv')
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')

prenatal_df.rename(columns={'HOSPITAL': 'hospital',
                            'Sex': 'gender'}, inplace=True)
sports_df.rename(columns={'Hospital': 'hospital',
                          'Male/female': 'gender'}, inplace=True)

hospital_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
hospital_df.drop(columns='Unnamed: 0', inplace=True)
hospital_df.dropna(axis=0, how='all', inplace=True)
hospital_df.gender.replace(['male', 'man', 'female', 'woman'], ['m', 'm', 'f', 'f'], inplace=True)
hospital_df.loc[hospital_df.hospital == 'prenatal', 'gender'] = \
    hospital_df.loc[hospital_df.hospital == 'prenatal', 'gender'].fillna('f')
for col in ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']:
    hospital_df[col].fillna(0, inplace=True)
pd.set_option('display.max_columns', 8)
print(f'Data shape: ({hospital_df.shape[0]}, {hospital_df.shape[1]})' )
print(pd.DataFrame.sample(hospital_df, n=20, random_state=30))