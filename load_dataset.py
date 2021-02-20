"""
using pandas created  dataframe for UniversalBank load datasets
"""
from import_libs import *

dataframe_loan=pd.read_csv("UniversalBank.csv")

print(dataframe_loan.head())

print(dataframe_loan.head(10))

print(dataframe_loan.tail(10))
