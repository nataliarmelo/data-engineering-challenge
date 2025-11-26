# Desafio 01 – Ingestão e Padronização de Dados para Análise Empregados do setor de Tecnologia no Brasil (IBGE / SIDRA)
## 📌 Visão Geral

Este projeto investiga o setor de Tecnologia da Informação no Brasil (CNAE 62) ao longo de 2016–2021, com base em microdados oficiais do Cadastro Central de Empresas (CEMPRE) via API pública do IBGE (SIDRA v3).

O foco principal é entender:

1. Estrutura empresarial
2. Distribuição de emprego
3. Remuneração por gênero
4. Evolução salarial no setor

A abordagem combina engenharia de dados + análise exploratória aplicada ao mercado real. 
O setor de tecnologia está entre os que mais crescem no Brasil, e apesar do crescimento, o mercado ainda carrega sinais clássicos de desigualdade salarial e baixa representação feminina em posições técnicas e gerenciais.

Este projeto busca transformar dados públicos em interpretação econômica relevante e transparente.

## 📡 Fonte de dados

📊 Sistema IBGE de Recuperação Automática — SIDRA v3

API oficial:
https://servicodados.ibge.gov.br/api/docs/agregados?versao=3


## 🛠️ Pipeline de Engenharia de Dados
1️⃣ Ingestão (Data Lake - RAW)
- Construção de URL via Query Builder da SIDRA
- Download direto via requests
- Conversão JSON → DataFrame Pandas
- Persistência em /data/raw

2️⃣ Processamento (Data Warehouse - Processed)
- Padronização de colunas (snake_case)
- Remoção de redundâncias (Brasil, metadados)
- Conversão de tipos (int64, float, string)
- Exportação para Parquet 

3️⃣ Curadoria (Data Mart - Curated)
Seleção de colunas relevantes:
    - ano
    - cnae_codigo
    - cnae_nome
    - faixa_ocupados_codigo
    - faixa_ocupados_nome
    - variavel_codigo
    - variavel_nome
    - valor
Mantivemos o Total dos agregados para comparações proporcionais.


## 🔬 Análise do Setor de Tecnologia (CNAE 62)

Filtramos os dados para:
- 62 — Atividades dos serviços de tecnologia da informação

Em seguida calculamos:
- Massa salarial por gênero
- Número de assalariados por gênero
- Salário médio

## 🧠 Insights (interpretáveis e aplicáveis)
### 💰 1. O setor de TI remunera acima da média nacional

Os salários médios começam em R$ 72k–R$ 88k/ano para homens
e R$ 51k–R$ 62k/ano para mulheres.

> Isso sugere alta qualificação e escassez de mão de obra especializada.

### 📈 2. Crescimento consistente — mesmo durante crise

De 2016 a 2021 o salário médio cresce ~22% para homens e ~20% para mulheres, incluindo período pandêmico.

> Tecnologia manteve investimento e absorção de profissional durante a crise.

### 🔥 3. Gap salarial estrutural

Mesmo com crescimento conjunto, a diferença permanece:

💡 De 20% a 30% a favor de trabalhadores homens, todos os anos.

Isso sugere:
- Acesso desigual a funções técnicas ou gerenciais
- Senioridade média maior no segmento masculino
- Concentração feminina em subsegmentos administrativos / suporte

### 🧭 4. A curva de remuneração é suave

Não há saltos abruptos → o setor cresce de forma orgânica e atrativa:
 - Mais vagas técnicas
 - Projetos de produto digital
 - Expansão de consultorias


## 📂 Reprodutibilidade

O notebook está disponível em: 
📁 /notebook/challenge_01.ipynb

Contém:
- Ingestão via API
- Normalização
- Pivots
- Cálculos de Médias
- Análises setoriais 


## ❤️ Contribuições

PRs e melhorias são bem-vindos.
Sinta-se livre para abrir issues ou sugestões.