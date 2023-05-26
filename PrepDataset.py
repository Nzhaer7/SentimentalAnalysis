import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

class Prep():
    def PrepData(self, Rdata):
        self.raw_data=Rdata

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

        return self.x_train, self.x_test, self.y_train, self.y_test