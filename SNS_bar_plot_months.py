import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv("fcc-forum-pageviews.csv")


# Supongamos que ya tienes df con el índice configurado como "date" y la columna "value"

lower_limit = df['value'].quantile(0.025)
upper_limit = df['value'].quantile(0.975)

filtered_df = df[(df['value'] > lower_limit) & (df['value'] < upper_limit)]
# Convertir la columna "date" a formato de fecha
filtered_df['date'] = pd.to_datetime(filtered_df['date'])

# Crear una nueva columna "year_month" que contiene la combinación de año y mes
filtered_df['year_month'] = filtered_df['date'].dt.to_period('M')

# Trazar un gráfico de barras con seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x=filtered_df['year_month'].dt.year, y=filtered_df['value'], hue=filtered_df['year_month'].dt.month, ci=None)

# Agregar etiquetas y título
plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.show()
# Guarda el gráfico

plt.savefig('bar_plot.png')
