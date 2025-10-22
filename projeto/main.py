import streamlit as st
import pandas as pd

def main():
    st.write("Bem vindo ao meu projeto de Big Data!")
    df = pd.read_csv('data/netflix_titles.csv')
    colunas = list(df.columns)
    selecionadas = st.multiselect("Selecione as colunas que deseja visualizar:", colunas, default=colunas)
    st.dataframe(df[selecionadas], height=600)


if __name__ == "__main__":
    main()
