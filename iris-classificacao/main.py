# main.py

from data import carregar_dados
from train import treinar_modelo
from evaluate import avaliar_modelo

def main():
    print("🔍 Iniciando o pipeline de classificação da Iris...")

    # 1. Carregar os dados
    X_train, X_test, y_train, y_test = carregar_dados()

    # 2. Treinar o modelo
    modelo = treinar_modelo(X_train, y_train)

    # 3. Avaliar o modelo
    avaliar_modelo(modelo, X_test, y_test)

if __name__ == "__main__":
    main()
