from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pickle

class cModel():

    def Model(self, data):

        self.x_train, self.x_test, self.y_train, self.y_test = data

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