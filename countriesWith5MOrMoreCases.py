# TODO: Countries with 5M or more total cases ( > operator)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    ''' read data from csv '''
    covidVaccineDf = pd.read_csv("resources/owid-covid-data.csv")