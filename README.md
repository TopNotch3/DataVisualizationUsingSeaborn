# DataVisualizationUsingSeaborn
Using Seaborn library to efficiently draw out important insights by plotting different types of graphs and charts.

Project: CO₂ Emissions Visualizations (wide-format dataset)

1. Put your original file as `Data.csv` in project root.
2. Install requirements: `pip install -r requirements.txt`.
3. Run `python run_all.py` to generate cleaned data and all visualizations.
4. Outputs:
   - Cleaned long-format CSV: `data/clean_co2_emissions.csv`
   - Figures: `outputs/figures/*.png`
   - Country features with cluster labels: `outputs/country_features_with_clusters.csv`

Notes:
- Sector-level analysis was removed because the uploaded dataset doesn’t include sector columns.
- Many plots automatically pick the latest year found in the data; change parameters inside scripts if you want other years.
