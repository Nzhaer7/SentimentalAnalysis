import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pickle

class cModel():

    def Model(self):
        self.data = pd.read_csv("data.csv")

        self.cv = CountVectorizer()

        self.data[''] = self.data[''].map({'':,'':,'':})

        self.data = self.data.fillna(0)

        self.x = data['']
        self.y = data['']

        self.x = self.x.replace([np.inf, -np.inf], np.nan, inplace=True)
        self.x = self.x.dropna()
        self.x = self.x.reset_index()

        self.y = self.y.replace([np.inf, -np.inf], np.nan)
        self.y = self.y.dropna()
        self.y = self.y.reset_index()

        self.x = self.cv.fit_transform(self.data[''].apply(lambda self.x: np.str_(self.x)))

        self.x_train, self.x_test, self.y_train, self.y_test=train_test_split(self.x, self.y, test_size=0.2)

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