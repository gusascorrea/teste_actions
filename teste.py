import os
import pandas as pd

# Criar diretório 'csv' se não existir
os.makedirs('csv', exist_ok=True)

# Criar data frame aleatório
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
# Salvar data frame em arquivo CSV
df.to_csv('csv/dataframe.csv', index=False)
print('Data frame salvo em csv')