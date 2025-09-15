import seaborn as sns
import matplotlib.pyplot as plt
from utils import save_fig, read_cleaned


def plot_missing():
    df = read_cleaned()
    wide = df.pivot(index='year', columns='country', values='co2_total')
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.heatmap(wide.isnull(), cbar=False, ax=ax)
    ax.set_title('Missing data heatmap (rows=years, cols=countries)')
    plt.tight_layout()
    save_fig(fig, 'missing_heatmap.png')


if __name__ == '__main__':
    plot_missing()