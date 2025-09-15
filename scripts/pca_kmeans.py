import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from utils import save_fig, read_cleaned, write_csv


def build_country_features(df):
    g = df.groupby('country')
    feats = g.agg(total_co2=pd.NamedAgg(column='co2_total', aggfunc='sum'),
                  mean_co2=pd.NamedAgg(column='co2_total', aggfunc='mean'),
                  std_co2=pd.NamedAgg(column='co2_total', aggfunc='std'),
                  years_count=pd.NamedAgg(column='year', aggfunc='nunique')).reset_index()
    feats = feats.fillna(0)
    return feats


def run_pca_kmeans(n_clusters=4):
    df = read_cleaned()
    feats = build_country_features(df)
    X = feats[['total_co2', 'mean_co2', 'std_co2', 'years_count']].values
    X = (X - X.mean(axis=0)) / (X.std(axis=0) + 1e-9)
    pca = PCA(n_components=2, random_state=42)
    Z = pca.fit_transform(X)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(Z)
    feats['pc1'] = Z[:, 0]
    feats['pc2'] = Z[:, 1]
    feats['cluster'] = kmeans.labels_

    fig, ax = plt.subplots(figsize=(10, 7))
    sns.scatterplot(data=feats, x='pc1', y='pc2', hue='cluster', palette='tab10', s=80, ax=ax)
    for i, row in feats.sort_values('total_co2', ascending=False).head(10).iterrows():
        ax.text(row['pc1'] + 0.01, row['pc2'] + 0.01, row['country'], fontsize=9)
    ax.set_title('PCA + KMeans clustering of countries (based on CO₂ features)')
    plt.tight_layout()
    save_fig(fig, 'pca_kmeans_countries.png')

    write_csv(feats, 'country_features_with_clusters.csv', outdir='outputs')


if __name__ == '__main__':
    run_pca_kmeans(n_clusters=4)