import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Análise de Veículos",
    page_icon="🚗",
    layout="wide"
)

# Título
st.header("🚗 Dashboard de Análise de Veículos")

st.write("""
Este aplicativo permite realizar uma análise exploratória de um conjunto de dados
de anúncios de venda de veículos.
""")

# Ler os dados
car_data = pd.read_csv("vehicles.csv")

# Mostrar tabela
if st.checkbox("Mostrar conjunto de dados"):
    st.dataframe(car_data)

# Histograma
if st.checkbox("Construir histograma"):

    st.write("Distribuição da quilometragem dos veículos.")

    fig = px.histogram(
        car_data,
        x="odometer",
        title="Histograma da Quilometragem"
    )

    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersão
if st.checkbox("Construir gráfico de dispersão"):

    st.write("Relação entre preço e quilometragem.")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Preço x Quilometragem"
    )

    st.plotly_chart(fig, use_container_width=True)