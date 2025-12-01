import pandas as pd
import os
from pathlib import Path

CURATED_PATH = Path(r"C:/workspace/data-engineering-challenge/02-academic_performance/data/curated/students_performance.parquet")
df = pd.read_parquet(CURATED_PATH, engine="fastparquet")

print("\n Tamanho da base:", df.shape)

print("\n Estatísticas descritivas:")
print(df.describe())

##### Análise exploratória

# Cria colunas de gap entre matérias
df["gap_math_reading"] = df["math_score"] - df["reading_score"]
df["gap_math_writing"] = df["math_score"] - df["writing_score"]

print("\n Estatísticas dos gaps (math - reading / math - writing):")
print(df[["gap_math_reading", "gap_math_writing"]].describe())

# Ver relação aproximada com aprovação -> criei um score médio de aprovação acima de 60
print("\n Gap médio por status de aprovação:")
print(
    df.groupby("passed_flag")[["gap_math_reading", "gap_math_writing"]]
      .mean()
      .rename(index={0: "reprovado", 1: "aprovado"})
)


### Nível educacional dos pais × curso preparatório
print("\n Média de nota por educação dos pais e curso preparatório:")
tabela_pais_prep = (
    df
    .groupby(["parental_level_of_education", "test_preparation_course"])["avg_score"]
    .mean()
    .unstack()
    .sort_index()
)
print(tabela_pais_prep)

print("\n Taxa de aprovação por educação dos pais e curso preparatório:")
tabela_aprov_pais_prep = (
    df
    .groupby(["parental_level_of_education", "test_preparation_course"])["passed"]
    .mean()  # média de 0/1 = taxa
    .unstack()
    .sort_index()
)
print(tabela_aprov_pais_prep)



#### Diferenças de gênero × curso preparatório

print("\n Média por gênero e curso preparatório:")
tabela_genero_prep = (
    df
    .groupby(["gender", "test_preparation_course"])["avg_score"]
    .mean()
    .unstack()
)
print(tabela_genero_prep)

print("\n Taxa de aprovação por gênero e curso preparatório:")
tabela_aprov_genero_prep = (
    df
    .groupby(["gender", "test_preparation_course"])["passed_flag"]
    .mean()
    .unstack()
)
print(tabela_aprov_genero_prep)