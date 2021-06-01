""" which country has the highest accumulated covid cases? (Tilde operator and Nlargest) """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    covidDf = pd.read_csv("resources/owid-covid-data.csv")

    ''' need to get rid of the world and continent data '''
    ''' by removing rows with null value in 'continent' column '''

    ''' ~ and isna() approach is same as notna(), this is for showcase purposes '''
    totalCasesAtLocation = covidDf[~covidDf.continent.isna()][['date', 'location', 'total_cases']]



    ''' Here just need to find the max number of total cases of all data '''
    ''' then we know the location with the most accumulated Covid cases '''
    maxNumOfCases = totalCasesAtLocation.total_cases.max()

    countryWithMostCases = totalCasesAtLocation[totalCasesAtLocation.total_cases == maxNumOfCases].location.item()

    numOfCasesFromCountryWithMostCases = totalCasesAtLocation[totalCasesAtLocation.total_cases == maxNumOfCases].total_cases.item()

    print("Country with the most cases is : " + countryWithMostCases + " with " + str(int(numOfCasesFromCountryWithMostCases)) + " cases")

