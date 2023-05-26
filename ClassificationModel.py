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

        self.x = self.cv.fit_transform(self.data[''].apply(lambda x: np.str_(self.x)))

        self.x_train, self.x_test, self.y_train, self.y_test=train_test_split(self.x, self.y, test_size=0.2)

        self.model=MultinomialNB()

        self.model.fit(self.x_train, self.y_train)

        self.result=self.model.score(self.x_test, self.y_test)

        self.result=self.result*100

        print(self.result)

        self.predictions = self.model.predict(self.x_test)

        self.cm = confusion_matrix(self.y_test, self.predictions, labels=self.model.classes_)
        self.disp = ConfusionMatrixDisplay(confusion_matrix=self.cm,
                                      display_labels=self.model.classes_)
        self.disp.plot()
        plt.show()

        pickle.dump(self.model, open("tsf.pkl","wb"))

        pickle.dump(self.cv, open("vectorizer.pkl","wb"))