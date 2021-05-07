# `visualisation-template.py`
"""the script is be used as a template of visualisation"""
# written by Zimo Peng for COMP20008 Assignment 2 in 2021

import pandas as pd
import argparse
import matplotlib.pyplot as plt

#this program was used to produce all 8 plots, but different variables and values were changed for each different variable

#check if value is NaN
def isNaN(string):
    return string != string

#reading csv file
df_diabetes = pd.read_csv('LGA_diabetes_profiles.csv', encoding = 'ISO-8859-1')

#slicing the dataframe into the columns LGA status, people reporting type 2 diabetes, and the 2nd variable
df_recreation = df_diabetes.loc[:,["LGA status","People reporting type 2 diabetes","People who do not meet dietary guidelines for either fruit or vegetable consumption"]]

#removing the percentage signs, and turning them into float values so that they can be processed
df_recreation["People reporting type 2 diabetes"] = df_recreation["People reporting type 2 diabetes"].apply(lambda x: float(str(x)[0:-1]) if not isNaN((x)) else 0)

#removing the percentage signs, and turning them into float values so that they can be processed 
df_recreation["People who do not meet dietary guidelines for either fruit or vegetable consumption"] = df_recreation["People who do not meet dietary guidelines for either fruit or vegetable consumption"].apply(lambda x: float(str(x)[0:-1]) if not isNaN((x)) else 0)

#creating 4 dataframe variables for each LGA status
df_shire = df_recreation.loc[df_diabetes["LGA status"] == "Shire"]
df_rural = df_recreation.loc[df_diabetes["LGA status"] == "Rural City"]
df_city = df_recreation.loc[df_diabetes["LGA status"] == "City"]
df_borough = df_recreation.loc[df_diabetes["LGA status"] == "Borough"]

#each colour will represent a different LGA status
colours = ('g', 'r', 'b', 'm')
status_list = [df_shire, df_rural, df_city, df_borough]

#creating the scatter plot from both variables
for status, c in zip(status_list, colours):
    name = status["LGA status"].values[0]
    plt.scatter(status["People reporting type 2 diabetes"], status["People who do not meet dietary guidelines for either fruit or vegetable consumption"], color = c, label = name )
    

plt.ylabel("People who do not meet dietary guidelines for either \nfruit or vegetable consumption(%)")
plt.xlabel("People registering type 2 diabetes with DHHS(%)")
plt.title("People who do not meet dietary guidelines(%) vs People registering \ntype 2 diabetes with DHHS(%)")
plt.xlim(0,10)     #x-axis range
plt.ylim(0,100)    #y-axis range
plt.grid(True)
plt.legend()
plt.show()

#saving the plot to a .png file
plt.savefig('dietary_guidelines_vs_diabetes(DHHS).png')
