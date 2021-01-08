import pandas
import numpy as np

class csvToDFUtil():
    def get(self):
        return csvToDF()



def csvToDF():
    # bring in the data#
    url = "./exercise01.csv"
    df = pandas.read_csv(url)
    df.shape


    #clean data#
    attributes = df.columns
    for att in attributes:
        df[att] = df[att].replace("?", "No Value")

        #get an idea of how many null values#
    df.isnull().sum().sum()
        #6465 NaNs, if we removed rows based on null values we could lose almost 10% of data#
        # dont remove rows #

        #stumbled upon this article that recommends discretisation of the marital status column#
        # https://towardsdatascience.com/designing-a-machine-learning-model-and-deploying-it-using-flask-on-heroku-9558ce6bde7b #
        # I agree, I think there is minimal information to be gained by keeping them as separate values and it makes it easier to work with#

    df.replace(['Divorced', 'Married-AF-spouse', 'Married-civ-spouse', 'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed'], ['divorced', 'married', 'married', 'married', 'not married', 'not married', 'not married'], inplace=True)

    return df
