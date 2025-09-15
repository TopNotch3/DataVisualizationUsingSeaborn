import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import save_fig, read_cleaned


def plot_top_emitters(year=None, top_n=15):
    df = read_cleaned()
    if year is None:
        year = int(df['year'].max())
    sub = df[df['year'] == year]
    top = sub.groupby('country', as_index=False)['co2_total'].sum().sort_values('co2_total', ascending=False).head(top_n)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top, x='co2_total', y='country', ax=ax)
    ax.set_title(f'Top {top_n} CO₂ emitting countries in {year} (total)')
    ax.set_xlabel('CO₂ Total')
    ax.set_ylabel('Country')
    plt.tight_layout()
    save_fig(fig, f'top_emitters_{year}.png')


if __name__ == '__main__':
    plot_top_emitters()