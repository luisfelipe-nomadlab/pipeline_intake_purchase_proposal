import pandas as pd
import numpy as np


def composicao_base(df: pd.DataFrame):
    return {
        "linhas": df.shape[0],
        "colunas": df.shape[1],
        "tipos_dados": df.dtypes.astype(str).to_dict(),
        "colunas": df.columns.tolist(),
        "missing": df.isnull().sum().to_dict()
    }


def tipagem_df(df: pd.DataFrame):
    resumo = {}
    for coluna in df.select_dtypes(include="object").columns:
        resumo[coluna] = {
            "quantidade_unicos": df[coluna].nunique(),
            "valores_unicos": df[coluna].unique().tolist()
        }
    return resumo


def target_check(df: pd.DataFrame):
    inconsistentes = df[(df["Purchased"] < 0) | (df["Purchased"] > 1)]
    return {
        "quantidade_inconsistente": len(inconsistentes),
        "registros": inconsistentes.to_dict(orient="records")
    } if not inconsistentes.empty else {"mensagem": "Dados regulares na coluna 'Purchased'"}


def feature_engineering(df: pd.DataFrame):
    df_copy = df.copy()
    df_copy["Income_per_Age"] = df_copy["Income"] / df_copy["Age"].replace(0, np.nan)
    df_copy["Age_x_Score"] = df_copy["Age"] * df_copy["Score"]
    df_copy = pd.get_dummies(df_copy, columns=["Marital_Status", "City"], drop_first=True)
    return df_copy
