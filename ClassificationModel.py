import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pickle


data=pd.read_csv("data.csv")

cv=CountVectorizer()

data['']=data[''].map({'':,'':})

data=data.fillna(0)

x=data['']
y=data['']

x=x.replace([np.inf, -np.inf], np.nan, inplace=True)
x=x.dropna()
x=x.reset_index()

y = y.replace([np.inf, -np.inf], np.nan)
y = y.dropna()
y = y.reset_index()

x = cv.fit_transform(data[''].apply(lambda x: np.str_(x)))

x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2)

model=MultinomialNB()

model.fit(x_train, y_train)

result=model.score(x_test, y_test)

result=result*100

print(result)

predictions = model.predict(x_test)

cm = confusion_matrix(y_test, predictions, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=model.classes_)
disp.plot()
plt.show()

pickle.dump(model, open("tsf.pkl","wb"))

pickle.dump(cv, open("vectorizer.pkl","wb"))