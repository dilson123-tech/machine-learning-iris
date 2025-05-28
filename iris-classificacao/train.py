# train.py

from sklearn.tree import DecisionTreeClassifier

def treinar_modelo(X_train, y_train):
    modelo = DecisionTreeClassifier()
    modelo.fit(X_train, y_train)
    return modelo
