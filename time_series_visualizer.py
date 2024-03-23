import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)


# Clean data: Set the index to the date column. Clean the data by filtering out days when the page views 
#were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
per_inf = df["value"].quantile(0.025)
per_sup = df["value"].quantile(0.975)

df_filtered_up = df[df["value"]>=per_inf]
df_filtered = df_filtered_up[df_filtered_up["value"]<=per_sup]

df_line = df_filtered
df_bar = df_filtered
df_box = df_filtered


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 7), dpi=100)
    
    x = df_line.index.values
    y = df_line["value"]

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.plot(x, y, linewidth=0.5, color="red")
    plt.xticks(x[[27, 235, 410, 600, 755, 939, 1135]])

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
    plt.close(fig)

draw_line_plot()


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar.loc[:, "Years"] = df_bar.index.year
    df_bar.loc[:, "Months"] = df_bar.index.month_name()
    df_bar_grouped = df_bar.groupby(["Years", "Months"], sort=False)["value"].mean().round().astype(int)
    
    fig, ax = plt.subplots(figsize=(15, 7), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")

    chart = sns.barplot(data=df_bar, x="Years", y="value", hue="Months", palette="tab10", errorbar=None)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='center')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
    plt.close(fig)
draw_bar_plot()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df_bar.copy()
    df_box['Years'] = [d.year for d in df_box.index]
    df_box['Months'] = [d.strftime('%b') for d in df_box.index]


    fig, ax = plt.subplots(1, 2, figsize=(15, 6), dpi=100)
    sns.boxplot(df_box, x="Years", y="value", hue="Years", palette="Set1", ax=ax[0], legend=False)
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")

    # gráfico por mes
    sns.boxplot(data=df_box, x="Months", y="value", hue="Months", palette="Set2")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")  

    # Draw box plots (using Seaborn)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
    plt.close(fig)
draw_box_plot()