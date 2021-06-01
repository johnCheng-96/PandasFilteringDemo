""" show all column Names """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    ''' read data from csv '''
    covidDf = pd.read_csv("resources/owid-covid-data.csv")

    for col in covidDf.columns:
        print(col)