import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':

    covidVaccineDf = pd.read_csv("resources/owid-covid-data.csv")

    # print(covidVaccineDf)

    # Eight ways to filter dataframe

    # extract three columns
    onlyPlaceVaccinated = covidVaccineDf[covidVaccineDf.location == "Hong Kong"][["date", "new_cases", "new_vaccinations"]]
    # print(onlyPlaceVaccinated)

    # dfg.show(onlyPlaceVaccinated)

    print(onlyPlaceVaccinated)

    for col in covidVaccineDf.columns:
        print(col)

    fig, ax_left = plt.subplots()
    ax_right = ax_left.twinx()

    ax_left.plot(onlyPlaceVaccinated["date"], onlyPlaceVaccinated["new_cases"], label="new_cases", color='red')

    ax_right.plot(onlyPlaceVaccinated["date"], onlyPlaceVaccinated["new_vaccinations"], label="new_vaccinations")

    plt.title("Covid Situation In Hong Kong Over Time", loc='left')
    fig.legend()

    plt.show()

    # TODO: filter one or more value

    # TODO: filter one or more range of values

    # TODO: np.where to filter

    # TODO: process data

    # TODO: cleaning data










