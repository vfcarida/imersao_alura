"""
Módulo responsável por carregamento e transformação de dados.
Implementa cache do Streamlit e tratamento de exceções.
"""
import logging
import pandas as pd
import streamlit as st
from src.config import DATA_URL

logger = logging.getLogger(__name__)

@st.cache_data(ttl=3600)
def load_data() -> pd.DataFrame:
    """
    Faz o fetch dos dados salariais em CSV via URL.
    Utiliza cache do Streamlit para evitar downloads redundantes em cada re-render,
    resolvendo o gargalo de performance do app original.

    Returns:
        pd.DataFrame: DataFrame contendo os dados carregados ou vazio em caso de erro.
    """
    try:
        logger.info(f"Iniciando download dos dados de: {DATA_URL}")
        df = pd.read_csv(DATA_URL)
        logger.info(f"Dados carregados com sucesso: {df.shape[0]} linhas e {df.shape[1]} colunas.")
        return df
    except Exception as e:
        logger.error(f"Erro ao carregar os dados: {e}", exc_info=True)
        st.error(f"Falha ao carregar os dados. Detalhes: {e}")
        return pd.DataFrame() # Retorna um DataFrame vazio para não quebrar a aplicação
