"""
Componente Visual: KPIs e Métricas Principais.
"""
import streamlit as st
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def render_metrics(df_filtrado: pd.DataFrame) -> None:
    """
    Renderiza as métricas (KPIs) no topo da página.
    Corrige o bug da versão anterior onde variáveis de fallback não coincidiam.

    Args:
        df_filtrado (pd.DataFrame): O DataFrame já filtrado pelas seleções do usuário.
    """
    st.subheader("Métricas gerais (Salário anual em USD)")

    # Fallbacks estruturados caso o filtro retorne vazio
    salario_medio = 0
    salario_maximo = 0
    total_registros = 0
    cargo_mais_frequente = "N/A"

    if not df_filtrado.empty:
        try:
            salario_medio = df_filtrado['usd'].mean()
            salario_maximo = df_filtrado['usd'].max()
            total_registros = df_filtrado.shape[0]
            # mode() pode retornar série vazia, tratamos isso de forma segura
            modas_cargo = df_filtrado["cargo"].mode()
            if not modas_cargo.empty:
                cargo_mais_frequente = modas_cargo.iloc[0]
        except KeyError as e:
            logger.error(f"Erro ao calcular métricas: Coluna não encontrada {e}", exc_info=True)
            st.error("Não foi possível calcular as métricas devido a dados ausentes.")
        except Exception as e:
            logger.error(f"Erro inesperado ao calcular métricas: {e}", exc_info=True)
            st.error("Erro ao calcular as métricas.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Salário médio", f"${salario_medio:,.0f}")
    col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
    col3.metric("Total de registros", f"{total_registros:,}")
    col4.metric("Cargo mais frequente", cargo_mais_frequente)
