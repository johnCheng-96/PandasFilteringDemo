""" Hong Kong daily new cases vs daily new vaccinations (query approach) """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    ''' read data from csv '''
    covidVaccineDf = pd.read_csv("resources/owid-covid-data.csv")

    '''
    ### 

    1. Only get data that matches "Hong Kong" in 'location' column
    2. Then, extract three columns from dataframe: 'date', 'new_cases', 'new_vaccinations'
    '''
    # hongKongNewCasesVsNewVaccinationsDf = covidVaccineDf[covidVaccineDf.location == "Hong Kong"][["date", "new_cases", "new_vaccinations"]]

    ''' query approach '''

    hongKongNewCasesVsNewVaccinationsDf = covidVaccineDf.query('location == "Hong Kong"')[["date", "new_cases", "new_vaccinations"]]

    print(hongKongNewCasesVsNewVaccinationsDf)


    '''
    3. Since there is a lot of null data for new_vaccinations, use fillna() to fill the null data
    '''
    hongKongNewCasesVsNewVaccinationsDf = hongKongNewCasesVsNewVaccinationsDf.fillna(0)


    '''
    4. plot the data for showcase
    '''
    fig, ax_left = plt.subplots()
    ax_right = ax_left.twinx()

    ax_left.plot(hongKongNewCasesVsNewVaccinationsDf["date"], hongKongNewCasesVsNewVaccinationsDf["new_cases"],
                 label="new_cases", color='red')

    ax_right.plot(hongKongNewCasesVsNewVaccinationsDf["date"], hongKongNewCasesVsNewVaccinationsDf["new_vaccinations"],
                  label="new_vaccinations")

    plt.title("Covid Situation In Hong Kong Over Time", loc='left')
    fig.legend()

    plt.show()


    # TODO: What is the daily global new cases? (using Str accessor approach)

    # TODO: What is the daily global new vaccinations? (using Isin approach)

    # TODO: What is the Hong Kong accumulated covid cases in 2020?

    # TODO: query() use it some where






