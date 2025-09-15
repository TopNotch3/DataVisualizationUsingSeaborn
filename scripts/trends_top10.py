import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import save_fig, read_cleaned


def plot_trends_top10(latest_year=None):
    df = read_cleaned()
    if latest_year is None:
        latest_year = int(df['year'].max())
    top_emitters = (df[df['year'] == latest_year]
                    .groupby('country', as_index=False)['co2_total'].sum()
                    .sort_values('co2_total', ascending=False)
                    .head(10)['country'].tolist())

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df[df['country'].isin(top_emitters)], x='year', y='co2_total', hue='country', ax=ax)
    ax.set_title(f'CO₂ Emissions Trends of Top 10 Emitters ({latest_year})')
    ax.set_xlabel('Year')
    ax.set_ylabel('CO₂ Total')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    save_fig(fig, f'trends_top10_{latest_year}.png')


if __name__ == '__main__':
    plot_trends_top10()