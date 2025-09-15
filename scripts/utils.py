import os
import pandas as pd
import matplotlib.pyplot as plt


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def save_fig(fig, fname, outdir='outputs/figures'):
    ensure_dir(outdir)
    fpath = os.path.join(outdir, fname)
    fig.savefig(fpath, bbox_inches='tight', dpi=150)
    print(f'Saved figure to {fpath}')


def write_csv(df, fname, outdir='data'):
    ensure_dir(outdir)
    path = os.path.join(outdir, fname)
    df.to_csv(path, index=False)
    print(f'Wrote CSV to {path}')


def read_cleaned(path='data/clean_co2_emissions.csv'):
    return pd.read_csv(path)