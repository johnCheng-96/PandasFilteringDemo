"""What is the daily global new vaccinations? (using Isin approach)"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    covidDf = pd.read_csv("resources/owid-covid-data.csv")

    # contains the whole word 'World'
    names = ['World']
    worldDf = covidDf[covidDf.location.isin(names)]

    worldDate = worldDf.date

    worldNewVaccinations = worldDf.new_vaccinations

    plt.plot(worldDate, worldNewVaccinations)
    plt.title("Daily World New Vaccinations")
    plt.show()

