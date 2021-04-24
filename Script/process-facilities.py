# `facilities.py`
"""this script is used to pre-process 'Sport and Recreational Facilities list' data from <https://discover.data.vic.gov.au/dataset/sport-and-recreational-facilities-list> Data Vic"""
# written by Ed Peng for COMP20008 Assignment 2 in 2021

import pandas as pd
import re

facility = pd.read_excel("srv_ifmd_all-facilities.xlsx")
fy = facility[['LGA Name', 'Facility ID', 'Facility Name']]
fy = fy.drop_duplicates()
fy = fy.reset_index()
fy = fy[['LGA Name','Facility ID','Facility Name']]

# byID – each facility
fy.to_csv("facilities-byID.csv")

# byCouncil – each local govt
missing = []
index = 0
for na in fy['LGA Name'].isna().values:
    if na: missing.append(index);
    index += 1;

### based on the Sports and Recreation Facility ID
### the Bermont South Club is registered under 'Mitchell Shire Council'
fy['LGA Name'][missing] = 'Mitchell Shire Council'

fyc = fy[['LGA Name','Facility ID']]
fyc = fyc.groupby('LGA Name').count().reset_index()
fyc.to_csv("facilities-byCouncil.csv")

# byLGA – facility count in each govt area
count = dict()
for i in fyc.values:
    i[0] = i[0].casefold()
    i[0] = re.sub('city council', '', i[0])
    i[0] = re.sub('shire council', '', i[0])
    i[0] = re.sub('rural', '', i[0])
    i[0] = i[0].strip()
    i[0] = i[0].title()
    if i[0] in count.keys():
        count[i[0]] += i[1]
    else:
        count[i[0]] = i[1]

facility_count = pd.DataFrame.from_dict(count, orient='index', columns=['Facility Count'])
facility_count.index.name = 'Govt Area'
facility_count.sort_values('Govt Area').reset_index()
facility_count.to_csv("facilities-byGovt.csv")
