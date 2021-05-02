#------------------------------------------------------------------------------
#Diabetes Type 2 by Local Government Areas (Preprocessing)
#written by Brandon Widjaja for C0MP2008 Assignment 2
#------------------------------------------------------------------------------

#import libraries
import pandas as pd
import os
import re

#create dataframe to store data for Government areas, population, number
#of people with type 2 diabetes as well as the percentage with diabetes
df = pd.DataFrame(columns = ['Govt Area', 'Registered', 'Population', 
                             '% Registered'])

#regex for removing paranthesis and the text inside for example:
#Yarra Ranges (S) we remove (S)
pattern = r'\([^)]*\)'

#search every file ending with ".csv" in the "LocalGovt" folder
for filename in os.listdir('LocalGovt'):
    if filename.endswith(".csv"):
        #read in each csv
        with open('LocalGovt'+'/'+ filename) as file:
            csv = pd.read_csv(file)
            
        #extract the name of the area (remove the text within paranthesis)
        area = csv['Area'].iloc[0]
        area = re.sub(pattern, '', area)
        #extract number of people who registered as diabetes type 2
        registered = int(csv['Registrants'].iloc[4])
        #extract the population of the area
        population = int(csv['Population'].iloc[0])
        #calculate the percentage of population with diabetes type 2 in that area
        percent_type2 = round(int(registered)/int(population)*100, 4)
        #compile all data into csv
        df.loc[len(df.index)] = [area, registered, population, percent_type2]
        
        continue
    else:
        continue
        
#sort csv by first column alphabetically
df.sort_values(by=['Govt Area'], inplace=True)
#export csv
df.to_csv("GovtDiabetes.csv", index = False)
