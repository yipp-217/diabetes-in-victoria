# The impact of the accessibility of sport and recreational facilities on the prevalence of diabetes in Victoria’s local government areas
- Please view the analysis [report](https://github.com/yipp-217/diabetes-in-victoria/blob/main/Report.pdf) on the subject matter
- Contributors: Ed Yi-Hsuan Peng, Jett Miller, Brandon Widjaja, Zimo Peng


## Research
### This data analysis report investigates:
- diabetes and exercise in relation to the accessibility of sport and recreational facilities
- facilities with people’s 
    - physical activity habits
    - sports participation rates
- in the granularity of Victorian local government area (LGA)

### The report aims to give insights into:
  - the interplay between public health and infrastructure 
    - diabetes disease
    - facility accessibility
  - Victorian communities’
    - health 
    - liveability
    - inclusiveness


## Data Sources
### NDSS: [Australian Diabetes Map](https://www.ndss.com.au/about-the-ndss/diabetes-facts-and-figures/australian-diabetes-map/)
The Australian Diabetes Map is a national map monitoring the prevalence of diabetes in Australia, and shows people diagnosed with diabetes who are registered on the National Diabetes Services Scheme.

### Data Vic: [Sport and Recreational Facilities List](https://discover.data.vic.gov.au/dataset/sport-and-recreational-facilities-list)
The Sport and Recreational Facilities List is a Victorian government dataset which identifies all recreational facilities within the state.

### DHHS: [2015 Local Government Area Profiles](https://discover.data.vic.gov.au/dataset/2015-local-government-area-profiles)
The Department of Health and Human Services data on each Victorian local government.


## Analysis Techniques:
1. Creating multiple scatter plots and classing each datapoint in their respected LGA status – shire, rural city, city, or borough.
2. Using simple linear regression to analyse the data to model the relationship between the variables 
3. Performing residual analysis on each plot to confirm that errors are random and independent
- Process the datasets using `argparse`, `re`, `os`, and `pandas`
- Visualise and Analyses the cleaned data using `matplotlib`, `numpy` and `seaborn`

