import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import save_fig, read_cleaned


def rolling_avg_country(country='United States', window=5):
    df = read_cleaned()
    sel = df[df['country'] == country].dropna(subset=['co2_total'])
    if sel.empty:
        print('No data for', country)
        return
    ts = sel.sort_values('year').groupby('year', as_index=False)['co2_total'].sum()
    ts['rolling'] = ts['co2_total'].rolling(window, min_periods=1).mean()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=ts, x='year', y='co2_total', marker='o', label='annual', ax=ax)
    sns.lineplot(data=ts, x='year', y='rolling', marker='o', label=f'{window}-yr rolling', ax=ax)
    ax.set_title(f'CO₂ emissions trend for {country} (with {window}-yr rolling avg)')
    plt.tight_layout()
    save_fig(fig, f'rolling_{country.replace(" ","_")}.png')


def percent_change_between(year_start=1990, year_end=None, top_n=12):
    df = read_cleaned()
    if year_end is None:
        year_end = int(df['year'].max())
    s = df[df['year'] == year_start].groupby('country', as_index=False)['co2_total'].sum()
    e = df[df['year'] == year_end].groupby('country', as_index=False)['co2_total'].sum()
    merged = pd.merge(s, e, on='country', how='inner', suffixes=('_start', '_end'))
    merged = merged[merged['co2_total_start'] > 0]
    merged['pct_change'] = (merged['co2_total_end'] - merged['co2_total_start']) / merged['co2_total_start'] * 100
    merged = merged.replace([pd.NA, float('inf'), -float('inf')], pd.NA).dropna(subset=['pct_change'])
    top = merged.sort_values('pct_change', ascending=False).head(top_n)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top, x='pct_change', y='country', ax=ax)
    ax.set_title(f'Top {top_n} countries by % change in CO₂ from {year_start} to {year_end}')
    plt.tight_layout()
    save_fig(fig, f'pct_change_{year_start}_{year_end}.png')


if __name__ == '__main__':
    rolling_avg_country(country='China', window=5)
    percent_change_between(year_start=1990, year_end=None, top_n=12)