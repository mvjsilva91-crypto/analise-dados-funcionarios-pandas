import pandas as pd
import numpy as np

print("="*50)
print("📊 CRIAÇÃO DO DATAFRAME")
print("="*50)

dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Carla'],
    'Idade': [25, 30, 35, 28, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Porto Alegre'],
    'Salário': [5000, 7000, 6000, 5500, 6500],
    'Departamento': ['Vendas', 'TI', 'RH', 'Vendas', 'TI']
}

df = pd.DataFrame(dados)
print(df)

print("\n📌 Manipulação de Dados")

# Novas colunas
df['Desconto'] = df['Salário'] * 0.06
df['Salário Anual'] = df['Salário'] * 13
df['Faixa Etária'] = np.where(df['Idade'] < 30, 'Jovem', 'Adulto')

# Ajuste específico
df.loc[df['Nome'] == 'Ana', 'Salário'] = 5500

print("\n📊 DataFrame atualizado:")
print(df)

print("\n📊 Ordenações")
print(df.sort_values('Idade', ascending=False))
print(df.sort_values(['Departamento', 'Salário']))

print("\n📊 AGRUPAMENTOS (GROUPBY)")
agrupamento = df.groupby('Departamento')

print("\nEstatísticas por Departamento:")
print(agrupamento['Salário'].agg(['mean', 'sum', 'count', 'min', 'max']))

print("\nMédia de Idade e Salário:")
print(agrupamento[['Idade', 'Salário']].mean())

print("\n📊 VALORES AUSENTES")

dados_nulos = {
    'Nome': ['Ana', 'João', 'Maria', None, 'Carla'],
    'Idade': [25, 30, 35, 28, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Porto Alegre'],
    'Salário': [5000, 7000, 6000, 5500, None],
    'Departamento': ['Vendas', 'TI', 'RH', 'Vendas', None]
}

df_nulos = pd.DataFrame(dados_nulos)

print("\nValores ausentes por coluna:")
print(df_nulos.isnull().sum())

print("\nSem valores nulos:")
print(df_nulos.dropna())

print("\nPreenchendo valores nulos:")
df_preenchido = df_nulos.fillna({
    'Nome': 'Desconhecido',
    'Salário': df_nulos['Salário'].mean(),
    'Departamento': 'Geral'
})

print(df_preenchido)

print("\n📅 TRABALHANDO COM DATAS")

dados_vendas = {
    'Data': pd.date_range('2024-01-01', periods=10, freq='D'),
    'Vendedor': ['Ana', 'João', 'Maria', 'Pedro'] * 2 + ['Ana', 'João'],
    'Vendas': [1000, 1500, 800, 1200, 900, 1600, 1100, 1300, 1400, 1700],
    'Produto': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
}

df_vendas = pd.DataFrame(dados_vendas)

df_vendas['Dia'] = df_vendas['Data'].dt.day
df_vendas['Mês'] = df_vendas['Data'].dt.month
df_vendas['Dia da Semana'] = df_vendas['Data'].dt.day_name()

print(df_vendas[['Data', 'Dia', 'Mês', 'Dia da Semana', 'Vendas']])

print("\n📂 LEITURA DE ARQUIVO EXCEL")

try:
    df_excel = pd.read_excel("dados/BaseFuncionarios.xlsx")

    print("\nColunas:")
    print(df_excel.columns.tolist())

    print("\nInformações:")
    print(df_excel.info())

    print("\nEstatísticas:")
    print(df_excel.describe())

except:
    print("⚠️ Arquivo Excel não encontrado na pasta /dados")