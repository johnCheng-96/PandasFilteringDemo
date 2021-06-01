# TODO: What is the Hong Kong daily new covid cases in 2020? (filtering date)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    covidDf = pd.read_csv("resources/owid-covid-data.csv")


    hongKongDf = covidDf[covidDf.location.str.contains(r"\bHong Kong\b")]

    start_date = "2020-1-1"

    end_date = "2020-12-31"

    hongKongDate = hongKongDf['date']

    after_start_date = hongKongDate >= start_date

    before_end_date = hongKongDate <= end_date

    hongKongDfIn2020 = hongKongDf.loc[after_start_date & before_end_date]

    hongKongNewCasesIn2020 = hongKongDfIn2020[['date', 'new_cases']]

    ''' markdown showcase '''
    print(hongKongNewCasesIn2020.to_markdown())

    ''' plot '''

    plt.xticks(rotation=90)
    # plt.tick_params(axis='x', which='major', labelsize=3)

    plt.plot(hongKongNewCasesIn2020['date'], hongKongDfIn2020['new_cases'])

    plt.show()





