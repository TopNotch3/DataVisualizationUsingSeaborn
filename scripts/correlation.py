import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import save_fig, read_cleaned


def plot_country_correlation(sample_countries=None, max_countries=80):
    df = read_cleaned()
    wide = df.pivot(index='year', columns='country', values='co2_total')

    # limit number of countries to make heatmap legible
    if sample_countries is not None:
        wide = wide[sample_countries]
    else:
        # choose top max_countries by average emissions
        mean_vals = wide.mean().sort_values(ascending=False).head(max_countries).index.tolist()
        wide = wide[mean_vals]

    corr = wide.corr()
    fig, ax = plt.subplots(figsize=(14, 12))
    sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation of CO₂ Emissions Between Countries')
    plt.tight_layout()
    save_fig(fig, 'country_correlation.png')


if __name__ == '__main__':
    plot_country_correlation()