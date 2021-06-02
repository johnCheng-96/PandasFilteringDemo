""" topTenCountriesDailyNewCases(groupby, agg and sort_values)"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ''' read data from csv '''
    covidDf = pd.read_csv("resources/owid-covid-data.csv")

    countriesDf = covidDf[covidDf.continent.notna()][['date', 'location', 'new_cases', 'total_cases']]

    topTenCountries = countriesDf.groupby(['location']).agg({'total_cases': max}).sort_values('total_cases',
                                                                                              ascending=False).head(10)



    for name in topTenCountries.index:
        curCountry = countriesDf[countriesDf.location.isin(name.split('\b'))]
        plt.plot(curCountry.date, curCountry.new_cases, linewidth=0.4, label=name)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig("topTenCountriesDailyNewCases.png", dpi=1000, bbox_inches='tight')



