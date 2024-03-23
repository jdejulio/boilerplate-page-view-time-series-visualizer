import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv("fcc-forum-pageviews.csv")
df = df.set_index("date")

lower_limit = df['value'].quantile(0.025)
upper_limit = df['value'].quantile(0.975)

filtered_df = df[(df['value'] > lower_limit) & (df['value'] < upper_limit)]

filtered_df['date'] = pd.to_datetime(filtered_df['date'])

df_bar = None
 # Save image and return fig (don't change this part)

fig.savefig('bar_plot.png')
   