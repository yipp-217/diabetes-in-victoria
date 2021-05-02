# `visualisation-scatterplot.py`
"""the script is used to visualise data to observe patterns"""
# written by Ed Peng for COMP20008 Assignment 2 in 2021

import pandas as pd
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('seaborn');

# scaffolding
df = pd.read_csv("LGA_diabetes_profiles.csv")
ndss = ['LGA Name', 'LGA status', 'People registering type 2 diabetes with NDSS']
dhhs = ['LGA Name', 'LGA status', 'People reporting type 2 diabetes']
factor = { 'name'    : 'LGA Name',
           'status'  : 'LGA status',
           'dndss'   : 'People registering type 2 diabetes with NDSS',
           'ddhhs'   : 'People reporting type 2 diabetes',
           'facility': 'LGA sport and recreational facilities count', 
           'sport'   : 'People who are members of a sports group',
           'physical': 'People who do not meet physical activity guidelines',
           'dietary' : 'People who do not meet dietary guidelines for either fruit or vegetable consumption'
          }
percentage = [v for k,v in factor.items() if v.startswith('People')]
ndss_facility = ndss + [factor['facility']]
ndss_sport    = ndss + [factor['sport']]
ndss_physical = ndss + [factor['physical']]
ndss_dietary  = ndss + [factor['dietary']]
dhhs_facility = dhhs + [factor['facility']]
dhhs_sport    = dhhs + [factor['sport']]
dhhs_physical = dhhs + [factor['physical']]
dhhs_dietary  = dhhs + [factor['dietary']]

# process numerical str-data to a sutiable dtype and drop a null record 
db = df[factor.values()].dropna()
for p in percentage:
    db[p] = db[p].str.rstrip('%').astype('float')

# know the min and max for each field for setting plot's boundaries 
# print(db.describe())

# use to differentiate the LGA status for each record in a given scatterplot
colour = []
for i in db[factor['status']]:
    if   i == 'Shire': colour.append(0);
    elif i == 'Rural City': colour.append(1);
    elif i == 'City': colour.append(2);
    elif i == 'Borough': colour.append(3);
db['colour'] = colour

# ------------------------------------------------------------------------------- #
# NDSS diabetes scatter plot with four factors
fig_ndss, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=4, figsize=(30, 5))

# NDSS diabetes v. facility count
scatter = ax0.scatter(
                    x=db[factor['facility']],
                    y=db[factor['dndss']],
                    c=db['colour'],cmap='seismic');
ax0.set(title="The influence of facility accessibility on diabetes",
       xlabel=factor['facility']+' (unit)',
       ylabel=factor['dndss']+' (%)');
ax0.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax0.set_ylim([0,10]);
ax0.set_xlim([0,200]);

# NDSS diabetes v. sport-group participation
scatter = ax1.scatter(
                    x=db[factor['sport']],
                    y=db[factor['dndss']],
                    c=db['colour'],cmap='seismic');
ax1.set(title="The influence of sports participation on diabetes",
       xlabel=factor['sport']+' (%)',
       ylabel=factor['dndss']+' (%)');
ax1.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax1.set_ylim([0,10]);

# NDSS diabetes v. sport-group participation
scatter = ax2.scatter(
                    x=db[factor['physical']],
                    y=db[factor['dndss']],
                    c=db['colour'],cmap='seismic');
ax2.set(title="The influence of physical activity on diabetes",
       xlabel=factor['physical']+' (%)',
       ylabel=factor['dndss']+' (%)');
ax2.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax2.set_ylim([0,10]);

# NDSS diabetes v. dietary guidelines
scatter = ax3.scatter(
                    x=db[factor['dietary']],
                    y=db[factor['dndss']],
                    c=db['colour'],cmap='seismic');
ax3.set(title="The influence of dietary on diabetes",
       xlabel=factor['dietary']+' (%)',
       ylabel=factor['dndss']+' (%)');
ax3.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax3.set_ylim([0,10]);

fig_ndss.savefig("plot-ndss-diabetes-4factors")
# =============================================================================== #
# DHHS diabetes scatter plot with four factors
fig_dhhs, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=4, figsize=(30, 5))

# NDSS diabetes v. facility count
scatter = ax0.scatter(
                    x=db[factor['facility']],
                    y=db[factor['ddhhs']],
                    c=db['colour'],cmap='spring');
ax0.set(title="facility accessibility factor",
       xlabel=factor['facility']+' (unit)',
       ylabel=factor['ddhhs']+' by DHHS (%)');
ax0.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax0.set_ylim([0,10]);
ax0.set_xlim([0,200]);

# NDSS diabetes v. sport-group participation
scatter = ax1.scatter(
                    x=db[factor['sport']],
                    y=db[factor['ddhhs']],
                    c=db['colour'],cmap='spring');
ax1.set(title="sports participation factor",
       xlabel=factor['sport']+' (%)',
       ylabel=factor['ddhhs']+' by DHHS (%)');
ax1.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax1.set_ylim([0,10]);

# NDSS diabetes v. sport-group participation
scatter = ax2.scatter(
                    x=db[factor['physical']],
                    y=db[factor['ddhhs']],
                    c=db['colour'],cmap='spring');
ax2.set(title="physical activity factor",
       xlabel=factor['physical']+' (%)',
       ylabel=factor['ddhhs']+' by DHHS (%)');
ax2.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax2.set_ylim([0,10]);

# NDSS diabetes v. dietary guidelines
scatter = ax3.scatter(
                    x=db[factor['dietary']],
                    y=db[factor['ddhhs']],
                    c=db['colour'],cmap='spring');
ax3.set(title="dietary factor",
       xlabel=factor['dietary']+' (%)',
       ylabel=factor['ddhhs']+' by DHHS (%)');
ax3.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax3.set_ylim([0,10]);

fig_dhhs.savefig("plot-dhhs-diabetes-4factors")
# ------------------------------------------------------------------------------- #

# Facility count influencing other factors
fig_facility, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(20, 5))

# NDSS diabetes v. facility count
scatter = ax0.scatter(
                    x=db[factor['facility']],
                    y=db[factor['sport']],
                    c=db['colour'],cmap='seismic');
ax0.set(title="The influence of facility accessibility on sports participation in consideration of LGA status",
       xlabel=factor['facility']+' (unit)',
       ylabel=factor['sport']+' (%)');
ax0.legend(*scatter.legend_elements(), title='LGA status', loc='upper right')
ax0.set_xlim([0,200]);
ax0.set_ylim([10,55]);

# NDSS diabetes v. sport-group participation
scatter = ax1.scatter(
                    x=db[factor['facility']],
                    y=db[factor['physical']],
                    c=db['colour'],cmap='seismic');
ax1.set(title="The influence of facility accessibility on physical activity in consideration of LGA status",
       xlabel=factor['facility']+' (unit)',
       ylabel=factor['sport']+' (%)');
ax1.legend(*scatter.legend_elements(), title='LGA status', loc='lower right')
ax1.set_xlim([0,200]);
ax1.set_ylim([30,75]);

fig_facility.savefig("plot-facility-influence")
