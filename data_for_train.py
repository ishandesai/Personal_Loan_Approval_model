"""
we need to drop unncessery column for input and output
so for input:we need every column of dataframe except Personal Loan
output: only Personal Loan column needed
make output inform of array
X_input: to give every input viarble same value so we can make our model accuracally
split data testing:22.5% and training:77.5%
"""
from data_analysis import *

print(dataframe_loan.columns)

X_input=dataframe_loan.drop(columns='Personal Loan')

print(X_input)

y_output=dataframe_loan['Personal Loan']

y_output = to_categorical(y_output)

print(y_output)

scaler_x = StandardScaler()

X_input = scaler_x.fit_transform(X_input)

X_trn,X_tst,y_trn,y_tst=train_test_split(X_input,y_output,test_size=0.225)

print(X_trn.shape,X_tst.shape,y_trn.shape,y_tst.shape)
