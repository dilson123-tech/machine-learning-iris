# Projeto ML Avançado - Classificação Iris

🚀 **Descrição:**  
Projeto de machine learning que implementa um pipeline completo para classificação do famoso dataset Iris utilizando Decision Tree. O código está modularizado em arquivos para facilitar manutenção, testes e extensibilidade.

---

## Estrutura do Projeto

- `data.py` — carregamento e pré-processamento dos dados  
- `train.py` — treinamento do modelo Decision Tree  
- `evaluate.py` — avaliação da performance do modelo  
- `main.py` — orquestrador que executa todo o pipeline  
- `requirements.txt` — dependências do projeto  
- `README.md` — documentação do projeto  

---

## Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/projeto_ml_avancado.git
   cd projeto_ml_avancado/iris-classificacao

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

pip install -r requirements.txt

python main.py

python main.py

Resultados esperados
Saída no console mostrando a acurácia do modelo

Gráfico gerado com a visualização das classes do dataset Iris

Tecnologias
Python 3.8+

scikit-learn

pandas

matplotlib

Próximos passos / melhorias
Adicionar testes automatizados (pytest)

Implementar logging e tratamento de exceções

Containerizar com Docker

Automatizar pipeline com GitHub Actions

Contato
Dilson Pereira
Email: dilsonpereira231@gmail.com