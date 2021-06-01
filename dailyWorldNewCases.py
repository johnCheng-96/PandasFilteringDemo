""" What is the daily global new cases? (using Str accessor approach) """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ''' read data from csv '''
    covidDf = pd.read_csv("resources/owid-covid-data.csv")

    ''' select "World" in 'location' column '''
    ''' using str accessor approach here '''
    worldDF = covidDf[covidDf.location.str.contains("World")]

    worldNewCases = worldDF[['date', 'new_cases']]

    plt.plot(worldNewCases['date'], worldDF['new_cases'])
    plt.title("World Daily New COVID Cases")
    plt.show()

