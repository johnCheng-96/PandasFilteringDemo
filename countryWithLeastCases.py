"""The Country with the least cases(date filtering and nsmallest)"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    ''' read data from csv '''
    covidDf = pd.read_csv("resources/owid-covid-data.csv")

    ''' remove "World" and Continent data first '''

    countriesDf = covidDf[covidDf.continent.notna()]

    print(countriesDf.to_markdown)

    ''' get the row for each country with its max date '''

    countriesDfUpToDate = countriesDf.groupby(by=['location']).apply(lambda x: x[x['date'] == x['date'].max()])

    countryWithLeastCase = countriesDfUpToDate.nsmallest(1, "total_cases").location.item()
    numOfCasesInCountryWithLeastCase = countriesDfUpToDate.nsmallest(1, "total_cases").total_cases.item()

    print("Country with the least cases is : " + countryWithLeastCase + " with " + str(int(numOfCasesInCountryWithLeastCase)) + " cases")







