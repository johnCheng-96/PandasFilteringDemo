'''
which country has the highest accumulated covid cases?
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    covidDf = pd.read_csv("resources/owid-covid-data.csv")

    ''' need to get rid of the world and continent data '''
    ''' by removing rows with null value in 'continent' column '''
    totalCasesAtLocation = covidDf[covidDf.continent.notna()][['date', 'location', 'total_cases']]


    ''' Here just need to find the max number of total cases of all data '''
    ''' then we know the location with the most accumulated Covid cases '''
    maxNumOfCases = totalCasesAtLocation.total_cases.max()

    print(totalCasesAtLocation[totalCasesAtLocation.total_cases == maxNumOfCases])

