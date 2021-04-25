# `LGA_diabetes_profiles.py`
"""the script is used to combine and process the three processed datasets"""
# written by Ed Peng for COMP20008 Assignment 2 in 2021

import pandas as pd
import re

# load the datasets
profiles = pd.read_csv("csv-profiles.csv")
diabetes = pd.read_csv("csv-diabetes.csv")
facilities = pd.read_csv("csv-facilities.csv")
diabetes.sort_values('Govt Area', inplace=True)

# process the diabetes dataset
Govt = []
Area = diabetes['Govt Area']
for area in Area:
    area = area.rstrip(' ')
    Govt.append(area)
diabetes['Govt Area'] = Govt

# rename and join 'diabetes' and 'profiles' datasets
diabetes.rename(columns={'Govt Area':'LGA Name'},inplace=True)
diabetes_profiles = pd.merge(diabetes, profiles, on='LGA Name', how='left')

# process the facilities dataset
Govt = []
Area = facilities['Govt Area']
Greater = ['Bendigo', 'Dandenong', 'Geelong', 'Shepparton']
for area in Area:
    if area == 'Borough Of Queenscliffe':
        Govt.append('Queenscliffe')
    elif area == 'Colac Otway':
        Govt.append('Colac-Otway')
    elif area in Greater:
        Govt.append('Greater '+area)
    else: Govt.append(area)
facilities['Govt Area'] = Govt

# rename and join 'diabetes_profiles' and 'facilities' dataframes
facilities.rename(columns={'Govt Area':'LGA Name'},inplace=True)
diabetes_profiles = pd.merge(diabetes_profiles, facilities, on='LGA Name', how='left')

# presentation and organisation 
diabetes_profiles['% Registered'] = [(str(round(r, 1))+'%') for r in diabetes_profiles['% Registered']]

LGA_diabetes_profiles = diabetes_profiles.rename(
    columns={
                'Registered': 'Number of NDSS type 2 diabetes registrant',
                'Population': 'LGA population',
                '% Registered': 'People registering type 2 diabetes with NDSS',
                'Facility Count': 'LGA sport and recreational facilities count'
                })

sequence = ['LGA Name', 'LGA status', 'Area of LGA (km2)', 'LGA population', 
            'Number of NDSS type 2 diabetes registrant',
            'People registering type 2 diabetes with NDSS',
            'People reporting type 2 diabetes',
            'People reporting type 2 diabetes (rank)',
            'People reporting being obese', 
            'People reporting being obese (rank)',
            'People reporting being pre-obese',
            'People reporting being pre-obese (rank)',
            'People who do not meet dietary guidelines for either fruit or vegetable consumption',
            'People who do not meet dietary guidelines for either fruit or vegetable consumption (rank)',
            'People who do not meet physical activity guidelines',
            'People who do not meet physical activity guidelines (rank)',
            'People who are members of a sports group',
            'People who are members of a sports group (rank)',
            'LGA sport and recreational facilities count']

LGA_diabetes_profiles = LGA_diabetes_profiles[sequence]
LGA_diabetes_profiles.to_csv("LGA_diabetes_profiles.csv",index=False)
