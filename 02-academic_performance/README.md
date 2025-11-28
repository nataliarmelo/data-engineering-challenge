# 🎯 Desafio 02 — Análise de performance acadêmica (Python puro + engenharia de dados + insights)
## 📘 Dataset

**Kaggle:** Students Academic Performance Dataset 
(https://www.kaggle.com/datasets/sadiajavedd/students-academic-performance-dataset)

Ele possui variáveis como:

- Gênero
- Horas de estudo
- Participação em atividades
- Notas por disciplina
- Status de saúde
- Presença 
- Nível de estresse 

> 🔗 Ou seja: dá para explorar comportamento estudantil vs performance final.

## 🧠 Objetivo geral do desafio

Criar um pipeline completo de engenharia de dados em Python puro, carregando, tratando e analisando o dataset para entender como fatores externos impactam o desempenho escolar.

## 🚀 Saída esperada (em alto nível)

✔️ Um script python (etl_student_perf.py) que:

- Lê o CSV original
- trata valores vazios
- padroniza colunas
- salva em parquet (camada curated)

✔️ Um script separado de análise (analysis_student_perf.py) que:

- lê esse parquet
- faz perguntas analíticas exploratórias
- gera métricas e produz conclusões

💡 Ao final, você terá algo profissional, modular e replicável.