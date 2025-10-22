import streamlit as st
import pandas as pd
import plotly.express as px

def main():

    st.set_page_config(page_title="Projeto de Big Data", layout="wide")

    st.write("Bem vindo ao meu projeto de Big Data!")
    df = pd.read_csv('data/netflix_titles.csv')
    colunas = list(df.columns)
    selecionadas = st.multiselect("Selecione as colunas que deseja visualizar:", colunas, default=colunas)
    st.dataframe(df[selecionadas], height=600)

    st.divider()

    st.markdown("# Contagem de Filmes e Séries na Netflix")
    counts = df['type'].value_counts()
    st.dataframe(counts)

    st.divider()

    col1, col2 = st.columns(2, gap="large", border=True)

    with col1:
        fig = px.bar(counts.reset_index(), 
                    x='type', 
                    y='count', 
                    title='Contagem de Filmes e Séries na Netflix',
                    labels={'type': 'Tipo', 'count': 'Contagem'}
                    )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.pie(counts.reset_index(), 
                    names='type', 
                    values='count', 
                    title='Proporção de Filmes e Séries na Netflix'
                    )
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
