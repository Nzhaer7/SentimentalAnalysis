import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class Prep():
    def PrepData(self, path):
        self.Path=path

        def read_data():
            self.data=pd.read_csv(self.Path, 
                             encoding='utf-8', 
                             sep=',', 
                             skipinitialspace=True, 
                             index_col=-1,
                             header=0,
                             )

            return self.data

        def features_labels(self, data):
            self.arr = np.array(data, dtype=np.float)
            self.X,self.y=arr[:,:-1], arr[:,-1]
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)
            self.scaler = StandardScaler()
            self.scaler.fit(self.X_train)
            self.X_train = self.scaler.transform(self.X_train)
            self.X_test = self.scaler.transform(self.X_test)

            return self.X_train, self.X_test, self.y_train, self.y_test