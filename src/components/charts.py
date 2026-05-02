"""
Componente Visual: Gráficos construídos com Plotly.
"""
import streamlit as st
import pandas as pd
import plotly.express as px

def render_charts(df_filtrado: pd.DataFrame) -> None:
    """
    Renderiza os gráficos principais do dashboard.

    Args:
        df_filtrado (pd.DataFrame): O DataFrame já filtrado para plotagem.
    """
    st.subheader("Gráficos")

    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        if not df_filtrado.empty:
            top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
            grafico_cargos = px.bar(
                top_cargos,
                x='usd',
                y='cargo',
                orientation='h',
                title="Top 10 cargos por salário médio",
                labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
            )
            grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(grafico_cargos, use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico de cargos.")

    with col_graf2:
        if not df_filtrado.empty:
            grafico_hist = px.histogram(
                df_filtrado,
                x='usd',
                nbins=30,
                title="Distribuição de salários anuais",
                labels={'usd': 'Faixa salarial (USD)', 'count': ''}
            )
            grafico_hist.update_layout(title_x=0.1)
            st.plotly_chart(grafico_hist, use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico de distribuição.")

    col_graf3, col_graf4 = st.columns(2)

    with col_graf3:
        if not df_filtrado.empty:
            remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
            remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
            grafico_remoto = px.pie(
                remoto_contagem,
                names='tipo_trabalho',
                values='quantidade',
                title='Proporção dos tipos de trabalho',
                hole=0.5  
            )
            grafico_remoto.update_traces(textinfo='percent+label')
            grafico_remoto.update_layout(title_x=0.1)
            st.plotly_chart(grafico_remoto, use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")
