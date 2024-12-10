import pandas as pd

# criar data frame aleatório
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
# salvar data frame em arquivo CSV
df.to_csv('csv/dataframe.csv', index=False)
print('Data frame salvo em csv')