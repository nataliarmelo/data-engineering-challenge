# Desafio 01 – Ingestão e Padronização de Dados do IPCA-15 (IBGE / SIDRA)

Fonte: Tabela 1705 do SIDRA – IPCA15 - Variação mensal, acumulada no ano, 
acumulada em 12 meses e peso mensal, para o índice geral, grupos, subgrupos, 
itens e subitens de produtos e serviços (a partir de fev/2012).

Neste desafio vamos:

1. Consumir a API do SIDRA (tabela 1705) via HTTP (JSON);
2. Coletar a série mensal de jan/2019 a dez/2019 (Brasil, índice geral);
3. Padronizar o DataFrame (tipos, nomes de colunas);
4. Salvar dados brutos e tratados em `data/raw`, `data/processed` e `data/curated`.

