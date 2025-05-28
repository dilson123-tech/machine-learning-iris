from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Carregar dataset Iris
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Treinar modelo
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Previsão e avaliação
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Acurácia do modelo: {accuracy:.2f}")

    # Visualização
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y

    plt.figure(figsize=(10, 6))
    for i, target_name in enumerate(target_names):
        subset = df[df['target'] == i]
        plt.scatter(subset[feature_names[0]], subset[feature_names[1]], label=target_name)

    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.title("Visualização do Dataset Iris")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
