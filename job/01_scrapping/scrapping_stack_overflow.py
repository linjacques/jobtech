import pandas as pd


df = pd.read_csv("/opt/airflow/source/survey_results_public.csv")

df["WantToWorkWith"] = df["LanguageWantToWorkWith"].fillna("")


tech_wanted = df["WantToWorkWith"].str.split(";").explode().value_counts()
top_tech = tech_wanted.head(150)


top_tech.to_csv("/opt/airflow/data/raw/top_technos_voulues.csv", header=["Number"])

print(" Export des technologies les plus recherchées dans 'top_technos_voulues.csv'")


stack_columns = [
    ("DatabaseHaveWorkedWith", "/opt/airflow/data/raw/bases_de_donnees.csv"),
    ("PlatformHaveWorkedWith", "/opt/airflow/data/raw/plateformes.csv"),
    ("WebframeHaveWorkedWith", "/opt/airflow/data/raw/frameworks_web.csv")
]

for col_name, filename in stack_columns:
    df[col_name] = df[col_name].fillna("")
    exploded = df[col_name].str.split(";").explode().value_counts().head(150)
    exploded.to_csv(filename, header=["Number"])
    print(f" Export de la stack {col_name} dans '{filename}'")
