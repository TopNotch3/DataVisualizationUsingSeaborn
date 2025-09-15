import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import save_fig, read_cleaned


def plot_distribution():
    df = read_cleaned()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['co2_total'], bins=60, kde=True, ax=ax)
    ax.set_title('Distribution of CO₂ Emissions (all country-years)')
    ax.set_xlabel('CO₂ Total')
    plt.tight_layout()
    save_fig(fig, 'distribution_all.png')


def plot_boxplot_by_year(remove_outliers=True):
    df = read_cleaned()
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.boxplot(x='year', y='co2_total', data=df, showfliers=not remove_outliers, ax=ax)
    ax.set_title('CO₂ by Year (boxplot)')
    ax.set_xlabel('Year')
    ax.set_ylabel('CO₂ Total')
    plt.xticks(rotation=90)
    plt.tight_layout()
    save_fig(fig, 'boxplot_by_year.png')


if __name__ == '__main__':
    plot_distribution()
    plot_boxplot_by_year()