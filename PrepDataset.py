import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

pah=""

def read_data():
    data=pd.read_csv(path, 
                     encoding='utf-8', 
                     sep=',', 
                     skipinitialspace=True, 
                     index_col=-1,
                     header=0,
                     )

    return data

def features_labels(data):
    arr = np.array(data, dtype=np.float)
    X.y=arr[:,:-1], arr[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test