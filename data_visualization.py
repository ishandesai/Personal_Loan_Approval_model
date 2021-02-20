"""
plot data so we can analysis graph and make some assumptions about our models

"""
from load_dataset import *

plot.figure(figsize=(10,10))

sns.countplot(x=dataframe_loan["Personal Loan"])
plot.show()

plot.plot(figsize=(10,10))

sns.countplot(x=dataframe_loan["Education"])
plot.show()

plot.figure(figsize=(20,10))

sns.countplot(x=dataframe_loan["Age"])
plot.show()

plot.figure(figsize=(15,10))

sns.countplot(x=dataframe_loan["CreditCard"])
plot.show()

plot.figure(figsize=(20,10))

sns.distplot(x=dataframe_loan["Income"])
plot.show()

accepted_loans=dataframe_loan[dataframe_loan['Personal Loan']==1]

rejected_loans=dataframe_loan[dataframe_loan['Personal Loan']==0]

print(accepted_loans)

print(rejected_loans)

print(accepted_loans.describe())

print(rejected_loans.describe())

plot.figure(figsize=(20,10))

sns.distplot(x=accepted_loans['Income'],color="white")


sns.distplot(x=rejected_loans['Income'],color="blue")

plot.show()

plot.figure(figsize=(100,100))

sns.pairplot(dataframe_loan)
plot.show()

plot.figure(figsize=(20,20))

cm=dataframe_loan.corr()

sns.heatmap(cm,annot=True)
plot.show()


sns.distplot(accepted_loans['CCAvg'],color="pink")


sns.distplot(rejected_loans["CCAvg"],color="purple")
plot.show()
