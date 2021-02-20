from train_model import *
"""
now we would get our model accuracy by comparing our model testing results with testing data we have
"""
prediction =bank_loan_approval_model.predict(X_tst)

predict_lst=[]

for ind in prediction:
    predict_lst.append(np.argmax(ind))
result =bank_loan_approval_model.evaluate(X_tst,y_tst)

print("Accuracy of our model is:",result[1])

y_original=[]

for ind in y_tst:
    y_original.append(np.argmax(ind))

cm=metrics.confusion_matrix(y_original,predict_lst)

plot.figure(figsize=(25,25))

sns.heatmap(cm , annot=True)

plot.show()



print(classification_report(y_original,predict_lst))

bank_loan_approval_model.save("/Users/ishan/Downloads")
