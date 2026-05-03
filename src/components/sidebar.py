"""
Componente Visual: Barra Lateral (Sidebar) de filtros.
"""
import streamlit as st
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def render_sidebar(df: pd.DataFrame) -> tuple[list[int], list[str], list[str], list[str]]:
    """
    Renderiza os controles de filtro na sidebar e retorna as opções selecionadas.
    
    Args:
        df (pd.DataFrame): DataFrame original (usado para popular os valores possíveis).

    Returns:
        tuple: (anos selecionados, senioridades selecionadas, contratos selecionados, tamanhos de empresa selecionados)
    """
    st.sidebar.header("🔍 Filtros")

    if df.empty:
        st.sidebar.warning("Sem dados para filtrar.")
        return [], [], [], []

    # Extrai opções únicas com tratamento de erro
    try:
        anos_disp = sorted(df['ano'].unique())
        sen_disp = sorted(df['senioridade'].unique())
        cont_disp = sorted(df['contrato'].unique())
        tam_disp = sorted(df['tamanho_empresa'].unique())
    except KeyError as e:
        logger.error(f"Erro ao extrair filtros: Coluna não encontrada {e}", exc_info=True)
        st.sidebar.error("Dados incompletos para carregar todos os filtros.")
        return [], [], [], []

    # Controles multiselect
    anos_sel = st.sidebar.multiselect("Ano", anos_disp, default=anos_disp)
    sen_sel = st.sidebar.multiselect("Senioridade", sen_disp, default=sen_disp)
    cont_sel = st.sidebar.multiselect("Tipo de Contrato", cont_disp, default=cont_disp)
    tam_sel = st.sidebar.multiselect("Tamanho da Empresa", tam_disp, default=tam_disp)

    return anos_sel, sen_sel, cont_sel, tam_sel
