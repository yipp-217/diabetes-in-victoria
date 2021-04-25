# `govt_profiles.py`
"""the script is used to pre-process '2015 Local Government Area Profiles' data from <https://discover.data.vic.gov.au/dataset/2015-local-government-area-profiles>"""
# written by Ed Peng for COMP20008 Assignment 2 in 2021

import pandas as pd
import re

lga = pd.read_excel("2015-Local_Government_Area_Profiles.xlsx", sheet_name='LGAs')
profiles = lga[['LGA Name', 'Area of LGA (km2)', 'People reporting type 2 diabetes', 'People reporting type 2 diabetes (rank)', 'People reporting being obese', 'People reporting being obese (rank)', 'People reporting being pre-obese', 'People reporting being pre-obese (rank)', 'People who do not meet dietary guidelines for either fruit or vegetable consumption', 'People who do not meet dietary guidelines for either fruit or vegetable consumption (rank)', 'People who do not meet physical activity guidelines', 'People who do not meet physical activity guidelines (rank)', 'People who are members of a sports group', 'People who are members of a sports group (rank)']]
profiles = profiles.iloc[:79]    # row 79 is Victoria
profiles = profiles.sort_values('LGA Name')

Name = profiles['LGA Name']
govt = []
status = []
for name in Name:
    if '(C)' in name:
        status.append('City')
    elif '(RC)' in name:
        status.append('Rural City')
    elif '(B)' in name:
        status.append('Borough')
    else: 
        status.append('Shire')
    name = re.sub(r'\W*\(\w*\)', '', name)
    govt.append(name)

profiles['LGA Name'] = govt
profiles.insert(1, 'LGA status', status)

profiles.to_csv("csv-profiles.csv", index=False)
