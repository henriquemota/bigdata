import streamlit as st
import pandas as pd

def main():
    st.write("Bem vindo ao meu projeto de Big Data!")
    df = pd.read_excel('etl/rotas.xls')
    st.write(df)


if __name__ == "__main__":
    main()
