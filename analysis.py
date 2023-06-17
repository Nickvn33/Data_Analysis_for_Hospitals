# write your code here
import pandas as pd
import matplotlib.pyplot as plt

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
# pd.set_option('display.max_columns', 8)
# print(f'Data shape: ({hospital_df.shape[0]}, {hospital_df.shape[1]})' )
# print(pd.DataFrame.sample(hospital_df, n=20, random_state=30))

# Workings to answer Stage 4's 1st question (Which hospital has the highest number of patients?):
# print(hospital_df.hospital.value_counts())

# Workings to answer Stage 4's 2nd question (What share of the patients in the general hospital suffers from
# stomach-related issues? Round the result to the third decimal place.):
general_stomach_share = (hospital_df.loc[hospital_df.hospital == 'general'].diagnosis.value_counts().loc['stomach'] /
                         hospital_df.loc[hospital_df.hospital == 'general'].hospital.count())\
                         .round(3)

# Workings to answer Stage 4's 3rd question (What share of the patients in the sports hospital suffers from
# dislocation-related issues? Round the result to the third decimal place.):
sports_dislocation_share = (hospital_df.loc[hospital_df.hospital == 'sports'].diagnosis.value_counts().loc['dislocation'] /
                         hospital_df.loc[hospital_df.hospital == 'sports'].hospital.count())\
                         .round(3)

# Workings to answer Stage 4's 4th question (What is the difference in the median ages of the patients in the general
# and sports hospitals?):
median_age_general = hospital_df.loc[hospital_df.hospital == 'general'].age.median()
median_age_sports = hospital_df.loc[hospital_df.hospital == 'sports'].age.median()
median_age_difference = abs(median_age_general - median_age_sports)

# Workings to answer Stage 4's 5th question (After data processing at the previous stages, the blood_test column has
# three values: t = a blood test was taken, f = a blood test wasn't taken, and 0 = there is no information. In which
# hospital the blood test was taken the most often (there is the biggest number of t in the blood_test column among all
# the hospitals)? How many blood tests were taken?):
# print(hospital_df.pivot_table(index='hospital', columns='blood_test', aggfunc='count'))

# Printout for Stage 4:
# print('The answer to the 1st question is general')
# print(f'The answer to the 2nd question is {general_stomach_share}')
# print(f'The answer to the 3rd question is {sports_dislocation_share}')
# print(f'The answer to the 4th question is {median_age_difference}')
# print(f'The answer to the 5th question is prenatal, 325 blood tests')

# Workings to answer Stage 5's 1st question (What is the most common age of a patient among all hospitals? Plot a
# histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.):
hospital_df.plot(y='age', kind='hist', bins=[0, 15, 35, 55, 70, 80])
plt.show()

# Workings to answer Stage 5's 2nd question (What is the most common diagnosis among patients in all hospitals?
# Create a pie chart.):
diagnosis = hospital_df.groupby(['diagnosis'])
plt.pie(hospital_df.groupby(['diagnosis']).hospital.count(), labels=diagnosis.groups.keys())
plt.show()

# Workings to answer Stage 5's 3rd question (Build a violin plot of height distribution by hospitals.
# Try to answer the questions. What is the main reason for the gap in values? Why there are two peaks,
# which correspond to the relatively small and big values? No special form is required to answer this question.):
general_height = hospital_df.loc[hospital_df.hospital == 'general'].height
prenatal_height = hospital_df.loc[hospital_df.hospital == 'prenatal'].height
sports_height = hospital_df.loc[hospital_df.hospital == 'sports'].height * 0.3048
plt.violinplot([general_height, prenatal_height, sports_height])
plt.show()

# Printout for Stage 5:
print('The answer to the 1st question: 15-35')
print('The answer to the 2nd question: pregnancy')
print("The answer to the 3rd question: The main reason for the difference in violin plots could be explained by "
      "prevalance of gender when it comes to those admitted to each hospital. For example, prenatal patients are"
      "exclusively female, and hence trends to have a lower violin plot compared to general and sports as the average"
      "female height is lower than male. Sports' average height tends to be higher as the patients are more likely to "
      "be male and/or more athletic, both of which correlate with greater height. The presence of two peaks on the "
      "general and sports plots are caused by the difference in average height between males and females.")