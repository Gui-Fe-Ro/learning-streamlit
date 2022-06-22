#Fazendo os imports
import pandas as pd
import plotly.express as px
import streamlit as st

#Criando a página
st.set_page_config(
    page_title="Pagina gov",
    page_icon=":bar_chart:",
    layout="wide"
)

df = pd.read_excel(
    io='planilha_gov.xlsx',
    engine='openpyxl',
    #sheet_name='unidades-academicas-06-2022',
    skiprows=0,
    usecols='A:L',
    nrows=100
)

#st.dataframe(df)

#----- Side bar -----

#Adicionando um header
st.sidebar.header("Filtros:")

#Adicionando as caixas de seleções
sigla_academica = st.sidebar.multiselect(
    "Selecione a sigla acadêmica",
    options=df["sigla_academica"].unique(),
    default=df["sigla_academica"].unique()
)

UNIDADE_GESTORA_ACADEMICA = st.sidebar.multiselect(
    "Selecione a unidade gestora",
    options=df["UNIDADE_GESTORA_ACADEMICA"].unique(),
    default=df["UNIDADE_GESTORA_ACADEMICA"].unique()
)

TIPO_ACADEMICA = st.sidebar.multiselect(
    "Selecione o tipo",
    options=df["TIPO_ACADEMICA"].unique(),
    default=df["TIPO_ACADEMICA"].unique()
)

#Filtrando os dados
df_selection = df.query(
    "sigla_academica == @sigla_academica & UNIDADE_GESTORA_ACADEMICA == @UNIDADE_GESTORA_ACADEMICA & TIPO_ACADEMICA == @TIPO_ACADEMICA"
)

st.dataframe(df_selection)

#---- Mainpage -----
st.title(":bar_chart: Gov Dashboard")
st.markdown("##")

#Top KPIs
