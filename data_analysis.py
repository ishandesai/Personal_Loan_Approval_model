"""
 to analysis data
"""
from load_dataset import *

print(dataframe_loan.info())

print(dataframe_loan.describe())

print(dataframe_loan.describe().T)

print(dataframe_loan.isnull().sum())
