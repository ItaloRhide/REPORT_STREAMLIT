import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Carregar os dados com os cabeçalhos corretos
file = 'LEVANTAMENTO - MAIO.xlsx'
df_embarque = pd.read_excel(file, sheet_name='CONSULTAS DE EMBARQUE', header=1)
df_candi = pd.read_excel(file, sheet_name='CONSULTAS E RENOVA\u00c7\u00d5ES DE CANDI', header=1)
df_ctes = pd.read_excel(file, sheet_name='EMISS\u00c3O DE CTES', header=1)

st.title('Dashboard de Levantamento - Maio')

# CONSULTAS DE EMBARQUE
st.header('Consultas de Embarque')
total_embarque = df_embarque['TOTAL CONSULTADO'].sum()
st.write(f'Total de consultas realizadas: {total_embarque}')

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

# CONSULTAS E RENOVAÇÕES DE CANDI
st.header('Consultas e Renovações de CANDI')
total_candi = df_candi['TOTAL'].sum()
st.write(f'Total de candidatos consultados/renovados: {total_candi}')

# Gráfico por Gerenciadora
fig2, ax2 = plt.subplots()
df_candi.groupby('GERENCIADORAS')['TOTAL'].sum().plot(kind='bar', ax=ax2, color='orange')
ax2.set_ylabel('Total')
ax2.set_xlabel('Gerenciadora')
ax2.set_title('Consultas/Renovações por Gerenciadora')
st.pyplot(fig2)

# Tabela quantitativa de Consultas e Renovações de CANDI por Gerenciadora
st.subheader('Tabela de Consultas e Renovações de CANDI por Gerenciadora')
candi_summary = df_candi.groupby('GERENCIADORAS')['TOTAL'].sum().reset_index()
candi_summary.columns = ['Gerenciadora', 'Quantidade de Consultas/Renovações']
st.dataframe(candi_summary)

# EMISSÃO DE CTES
st.header('Emissão de CT-es')
total_ctes = df_ctes.shape[0]
st.write(f'Total de CT-es emitidos: {total_ctes}')

# Gráfico por Indústria
st.subheader('CT-es por Indústria')
df_ctes_industrias = df_ctes['INDÚSTRIA'].value_counts().reset_index()
df_ctes_industrias.columns = ['Indústria', 'Quantidade']
fig3, ax3 = plt.subplots()
df_ctes_industrias.set_index('Indústria')['Quantidade'].plot(kind='bar', ax=ax3, color='green')
ax3.set_ylabel('Quantidade de CT-es')
ax3.set_xlabel('Indústria')
ax3.set_title('Distribuição de CT-es por Indústria')
st.pyplot(fig3)

# Tabela separando quantitativos por indústria
st.subheader('Tabela de CT-es por Indústria')
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
st.subheader('Tabela Detalhada de CT-es')
st.dataframe(df_ctes[['DATA', 'MOTORISTA', 'INDÚSTRIA', 'TIPO EMBARQUE']])
