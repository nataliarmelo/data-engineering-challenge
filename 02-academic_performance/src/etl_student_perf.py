
#### Bibliotecas
import pandas as pd
import os
from pathlib import Path
import shutil
import kagglehub
from kagglehub import KaggleDatasetAdapter


#### Download do dataset do Kaggle
path = kagglehub.dataset_download("sadiajavedd/students-academic-performance-dataset")
print("Dataset baixado em:", path)

# Salva os arquivos na pasta raw
dest_dir = r"C:\workspace\data-engineering-challenge\02-academic_performance\data\raw" 
os.makedirs(dest_dir, exist_ok=True)

for root, dirs, files in os.walk(path):
    for file_name in files:
        src = os.path.join(root, file_name)
        dst = os.path.join(dest_dir, file_name)
        shutil.copy(src, dst)

print("Arquivos copiados para:", dest_dir)


#### ETL - Carregamento dos dados
RAW_PATH = Path('02-academic_performance/data/raw/studentsPerformance.csv')

df = pd.read_csv(RAW_PATH)
print("Dados carregados com sucesso!")

 # renomeia colunas para snake case
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_"))

# corrige tipos
numeric_cols = ["math_score", "reading_score", "writing_score"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# drop linhas 
df = df.dropna(subset=numeric_cols)


#### Salvamento dos dados tratados                  
processed = Path('02-academic_performance/data/processed')
processed.mkdir(parents=True, exist_ok=True)

PROCESS_PATH = processed / "students_performance.parquet"
df_to_save = df.reset_index(drop=True).copy()

df_to_save.to_parquet(str(PROCESS_PATH), engine="fastparquet", index=False)
PROCESS_PATH
print("Dados tratados salvos em:", PROCESS_PATH)


### Métricas para uso na análise posterior

# Criação de colunas com médias e status de aprovação
df["avg_score"] = df[numeric_cols].mean(axis=1)
df["passed"] = df["avg_score"] >= 60

df_cur = df[[
    "gender",
    "race/ethnicity",
    "parental_level_of_education",
    "lunch",
    "test_preparation_course",
    "math_score",
    "reading_score",
    "writing_score",
    "avg_score",
    "passed"
]]


curated = Path('02-academic_performance/data/curated')
curated.mkdir(parents=True, exist_ok=True)

CURATED_PATH = curated / "students_performance.parquet"
df_to_save = df.reset_index(drop=True).copy()

df_to_save.to_parquet(str(CURATED_PATH), engine="fastparquet", index=False)
CURATED_PATH
print("Dados tratados salvos em:", CURATED_PATH)
