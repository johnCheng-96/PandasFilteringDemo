import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    covidVaccineDf = pd.read_csv("resources/owid-covid-data.csv")

    # print(covidVaccineDf)

    # TODO: Eight ways to filter dataframe

    # TODO: Hong Kong daily new cases vs daily new vaccinations

    # extract three columns
    hongKongNewCasesVsNewVaccinationsDf = covidVaccineDf[covidVaccineDf.location == "Hong Kong"][
        ["date", "new_cases", "new_vaccinations"]]
    # print(hongKongNewCasesVsNewVaccinationsDf)

    # dfg.show(hongKongNewCasesVsNewVaccinationsDf)

    # fillna()
    hongKongNewCasesVsNewVaccinationsDf = hongKongNewCasesVsNewVaccinationsDf.fillna(0)

    print(hongKongNewCasesVsNewVaccinationsDf)

    for col in covidVaccineDf.columns:
        print(col)

    fig, ax_left = plt.subplots()
    ax_right = ax_left.twinx()

    ax_left.plot(hongKongNewCasesVsNewVaccinationsDf["date"], hongKongNewCasesVsNewVaccinationsDf["new_cases"],
                 label="new_cases", color='red')

    ax_right.plot(hongKongNewCasesVsNewVaccinationsDf["date"], hongKongNewCasesVsNewVaccinationsDf["new_vaccinations"],
                  label="new_vaccinations")

    plt.title("Covid Situation In Hong Kong Over Time", loc='left')
    fig.legend()

    plt.show()

    # isna() or isnull()

    print(hongKongNewCasesVsNewVaccinationsDf.isnull().head())

    # notna()
    print(hongKongNewCasesVsNewVaccinationsDf[hongKongNewCasesVsNewVaccinationsDf.new_vaccinations.notna()].head())

    # isna().mean()
    print(hongKongNewCasesVsNewVaccinationsDf.isna().mean())

    # to_markdown()

    print(hongKongNewCasesVsNewVaccinationsDf.to_markdown())

    # all(1)
    sub_set = hongKongNewCasesVsNewVaccinationsDf[['new_vaccinations']]
    print(hongKongNewCasesVsNewVaccinationsDf[sub_set.isna().all(1)])

    # describe()
    print(hongKongNewCasesVsNewVaccinationsDf.describe())

    # idxmax() and loc[] : when does Hong Kong have the highest number of new cases?
    print(hongKongNewCasesVsNewVaccinationsDf.loc[hongKongNewCasesVsNewVaccinationsDf[['new_cases']].idxmax()])

    # TODO: filter one or more value
    # TODO: which country has the highest accumulated covid cases?


    # TODO: filter one or more range of values

    # TODO: np.where to filter

    # TODO: process data

    # TODO: cleaning data
