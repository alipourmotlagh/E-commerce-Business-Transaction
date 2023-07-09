# Functions for me :)


def data_report(dataframe):
    """ Function to get a dataframe review """
    print(dataframe.info())
    print("\n")
    print(dataframe.describe())
    print("\n")
    print(dataframe.isnull().sum())