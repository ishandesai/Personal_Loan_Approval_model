from data_for_train import *
"""
we have used ANN model for our project
each neural of this model is independent so we would get multiple inputs one output
"""

bank_loan_approval_model=keras.Sequential()

bank_loan_approval_model.add(Dense(250, input_dim=13,kernel_initializer='normal',activation='relu'))

bank_loan_approval_model.add(Dense(500,activation='relu'))

bank_loan_approval_model.add(Dense(500,activation="linear"))

bank_loan_approval_model.add(Dropout(0.5))

bank_loan_approval_model.add(Dense(300,activation="linear"))

bank_loan_approval_model.add(Dropout(0.5))

bank_loan_approval_model.add(Dense(400,activation="linear"))

bank_loan_approval_model.add(Dropout(0.43))

bank_loan_approval_model.add(Dense(300,activation="linear"))

bank_loan_approval_model.add(Dropout(0.5))


bank_loan_approval_model.add(Dense(100,activation="linear"))

bank_loan_approval_model.add(Dropout(0.5))

bank_loan_approval_model.add(Dense(2,activation="softmax"))

bank_loan_approval_model.summary()
