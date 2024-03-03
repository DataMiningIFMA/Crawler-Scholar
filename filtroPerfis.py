import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('perfs_csv.csv')

# Excluindo linhas que contêm a string 'view_op=search_authors&mauthors'
mask = ~df['perfs'].str.contains('view_op=search_authors&mauthors', case=False)
df = df.loc[mask]

# Salvando o DataFrame resultante em formato CSV
df.to_csv('tabela_filtrada.csv', index=False)