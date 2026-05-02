"""
Módulo de regras de negócio para filtragem.
Isola a lógica de manipulação do DataFrame da lógica de interface.
"""
import pandas as pd

def apply_filters(
    df: pd.DataFrame, 
    anos: list[int], 
    senioridades: list[str], 
    contratos: list[str], 
    tamanhos: list[str]
) -> pd.DataFrame:
    """
    Aplica as seleções do usuário para filtrar o dataframe principal.

    Args:
        df (pd.DataFrame): O DataFrame original completo.
        anos (list[int]): Lista de anos selecionados.
        senioridades (list[str]): Lista de senioridades selecionadas.
        contratos (list[str]): Lista de tipos de contrato selecionados.
        tamanhos (list[str]): Lista de tamanhos de empresa selecionados.

    Returns:
        pd.DataFrame: DataFrame filtrado.
    """
    if df.empty:
        return df
        
    df_filtrado = df[
        (df['ano'].isin(anos)) &
        (df['senioridade'].isin(senioridades)) &
        (df['contrato'].isin(contratos)) &
        (df['tamanho_empresa'].isin(tamanhos))
    ]
    return df_filtrado
