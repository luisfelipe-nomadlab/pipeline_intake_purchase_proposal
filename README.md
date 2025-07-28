# Customer Purchase API

API desenvolvida com **FastAPI** para análise, validação e enriquecimento de dados relacionados ao comportamento de compra de clientes. O pipeline processa arquivos CSV e retorna informações estruturadas sobre o dataset, aplicando engenharia de atributos para uso posterior em modelos de machine learning.

---

## Funcionalidades

- Análise estrutural da base (linhas, colunas, tipos, missing)
- Diagnóstico de colunas categóricas (valores únicos)
- Verificação de inconsistências na variável alvo `Purchased`
- Criação de novas features a partir de atributos existentes

---

## Exemplo de Fluxo de Processamento

O endpoint `/processar/` recebe um arquivo `.csv` e executa:

1. `composicao_base`: informações gerais da base
2. `tipagem_df`: análise de colunas categóricas
3. `target_check`: verificação de valores inválidos na variável alvo
4. `feature_engineering`: criação de novas variáveis (`Income_per_Age`, `Age_x_Score`, dummies)

---

## Estrutura do Projeto

📁 app/
├── main.py # API com FastAPI
└── pipeline.py # Funções de pré-processamento
---

## Endpoints

### `GET /`
Teste básico da API  
**Resposta:**
```json
{"message": "API está funcionando!"}



