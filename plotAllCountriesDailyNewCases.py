# TODO: display all countries daily new cases in one plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    ''' read data from csv '''
    covidDf = pd.read_csv("resources/owid-covid-data.csv")

    countriesDf = covidDf[covidDf.continent.notna()][['date', 'location', 'new_cases']]

    countriesNames = countriesDf['location'].unique()

    for name in countriesNames:
        curCountry = countriesDf[countriesDf.location.isin(name.split('\b'))]
        plt.plot(curCountry.date, curCountry.new_cases, linewidth=0.2, label=name)


    lgd = plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='xx-small', ncol=7)


    plt.savefig("allCountriesDailyNewCases.png", dpi=1000, bbox_inches='tight')

    # TODO: sort countries and plot top 10 only

    ''' sum all new cases group by each country '''









