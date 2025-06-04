import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Custom CSS para background estático (gradiente)
page_bg_css = """
<style>
    .stApp {
        background: linear-gradient(180deg, #161616, #0a0042);
    }
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Carregar os dados com os cabeçalhos corretos
file = 'LEVANTAMENTO - MAIO.xlsx'
df_embarque = pd.read_excel(file, sheet_name='CONSULTAS DE EMBARQUE', header=1)
df_candi = pd.read_excel(file, sheet_name='CONSULTAS E RENOVA\u00c7\u00d5ES DE CANDI', header=1)
df_ctes = pd.read_excel(file, sheet_name='EMISS\u00c3O DE CTES', header=1)

st.title('Dashboard de Levantamento - Maio')

# CONSULTAS DE EMBARQUE
st.header('Consultas de Embarque')
total_embarque = df_embarque['TOTAL CONSULTADO'].sum()

# Gráfico por Gerenciadora
fig1, ax1 = plt.subplots()
df_embarque.groupby('GERENCIADORAS')['TOTAL CONSULTADO'].sum().plot(kind='bar', ax=ax1)
ax1.set_ylabel('Total Consultado')
ax1.set_xlabel('Gerenciadora')
ax1.set_title('Consultas por Gerenciadora')
st.pyplot(fig1)

# Tabela quantitativa de Consultas de Embarque por Gerenciadora
st.subheader('Tabela de Consultas de Embarque por Gerenciadora')
embarque_summary = df_embarque.groupby('GERENCIADORAS')['TOTAL CONSULTADO'].sum().reset_index()
embarque_summary.columns = ['Gerenciadora', 'Quantidade de Consultas']
st.dataframe(embarque_summary)
st.subheader(f'Total de consultas realizadas: {total_embarque}')

# CONSULTAS E RENOVAÇÕES DE CANDI
st.header('Consultas e Renovações de CANDI')
total_candi = df_candi['TOTAL'].sum()

# Gráfico por Gerenciadora
fig2, ax2 = plt.subplots()
df_candi.groupby('GERENCIADORAS')['TOTAL'].sum().plot(kind='bar', ax=ax2, color='#001e63')
ax2.set_ylabel('Total')
ax2.set_xlabel('Gerenciadora')
ax2.set_title('Consultas/Renovações por Gerenciadora')
st.pyplot(fig2)

# Tabela quantitativa de Consultas e Renovações de CANDI por Gerenciadora
st.subheader('Tabela de Consultas e Renovações de CANDI por Gerenciadora')
candi_summary = df_candi.groupby('GERENCIADORAS')['TOTAL'].sum().reset_index()
candi_summary.columns = ['Gerenciadora', 'Quantidade de Consultas/Renovações']
st.dataframe(candi_summary)
st.subheader(f'Total de candidatos consultados/renovados: {total_candi}')

# EMISSÃO DE CTES
st.header('Emissão de Documentação')
total_ctes = df_ctes.shape[0]

# Gráfico por Indústria
st.subheader('Documentações por Indústria')
df_ctes_industrias = df_ctes['INDÚSTRIA'].value_counts().reset_index()
df_ctes_industrias.columns = ['Indústria', 'Quantidade']
fig3, ax3 = plt.subplots()
df_ctes_industrias.set_index('Indústria')['Quantidade'].plot(kind='bar', ax=ax3, color='#008f96')
ax3.set_ylabel('Quantidade de Documentações')
ax3.set_xlabel('Indústria')
ax3.set_title('Distribuição de Documentações por Indústria')
st.pyplot(fig3)
st.subheader(f'Total de documentos emitidos: {total_ctes}')

# Tabela separando quantitativos por indústria
st.subheader('Tabela de Documentações por Indústria')
st.dataframe(df_ctes_industrias)

# Montante por Tipo de Embarque
st.subheader('Distribuição por Tipo de Embarque')
df_ctes_tipo = df_ctes['TIPO EMBARQUE'].value_counts().reset_index()
df_ctes_tipo.columns = ['Tipo de Embarque', 'Quantidade']
fig4, ax4 = plt.subplots()
df_ctes_tipo.set_index('Tipo de Embarque')['Quantidade'].plot(kind='pie', autopct='%1.1f%%', ax=ax4)
ax4.set_ylabel('')
st.pyplot(fig4)

# Tabela detalhada de CT-es
st.subheader('Tabela Detalhada de Documentações')
st.dataframe(df_ctes[['DATA', 'MOTORISTA', 'INDÚSTRIA', 'TIPO EMBARQUE']])