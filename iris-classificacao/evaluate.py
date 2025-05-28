# evaluate.py

from sklearn.metrics import accuracy_score

def avaliar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    print(f"Acurácia do modelo: {acuracia:.2f}")
