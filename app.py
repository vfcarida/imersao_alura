"""
Ponto de entrada do aplicativo Streamlit.
Orquestra o carregamento de dados, filtros e renderização dos componentes.
"""
import streamlit as st
from src.config import PAGE_TITLE, PAGE_ICON, LAYOUT
from src.data_loader import load_data
from src.filters import apply_filters
from src.components.sidebar import render_sidebar
from src.components.metrics import render_metrics
from src.components.charts import render_charts

def main() -> None:
    """Função principal que orquestra e renderiza o app."""
    # --- Configuração da Página ---
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=LAYOUT,
    )

    # --- Carregamento dos dados com Cache ---
    df = load_data()

    # --- Barra Lateral (Filtros) ---
    anos_sel, sen_sel, cont_sel, tam_sel = render_sidebar(df)

    # --- Filtragem ---
    df_filtrado = apply_filters(df, anos_sel, sen_sel, cont_sel, tam_sel)

    # --- Conteúdo Principal ---
    st.title(f"{PAGE_ICON} {PAGE_TITLE}")
    st.markdown(
        "Explore os dados salariais na área de dados nos últimos anos. "
        "Utilize os filtros à esquerda para refinar sua análise."
    )

    # Renderiza as Métricas (KPIs)
    render_metrics(df_filtrado)
    st.markdown("---")

    # Renderiza os Gráficos
    render_charts(df_filtrado)

    # Tabela de Dados Detalhados
    st.subheader("Dados Detalhados")
    if not df_filtrado.empty:
        st.dataframe(df_filtrado)
    else:
        st.info("Utilize os filtros para visualizar os dados detalhados.")

if __name__ == "__main__":
    main()
