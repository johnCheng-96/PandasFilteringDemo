"""Countries with 5M or more total cases ( > operator, query and groupby)"""

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

    print(countriesDfUpToDate.query('total_cases > 5_000_000')[['location', 'total_cases']])