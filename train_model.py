"""
compile and train model for 10 epochs
and plot training loss graph

"""
from build_model import *

bank_loan_approval_model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=['accuracy'])

history = bank_loan_approval_model.fit(X_trn,y_trn,epochs=3,validation_split=0.1,verbose=1)

plot.plot(history.history['loss'])
plot.plot(history.history['val_loss'])
plot.title('Model loss')
plot.ylabel('loss')
plot.xlabel('epoch')
plot.legend(['train_loss','val_loss'],loc = 'upper right')
plot.show()
