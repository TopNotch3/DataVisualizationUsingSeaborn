import pandas as pd
import os

def load_and_clean(path):
    print(f"Loading {path}")
    df = pd.read_csv(path)

    # Standardize column names
    df = df.rename(columns={
        "Name": "country",
        "year": "year",
        "co2": "co2_total",
        "co2_per_capita": "co2_per_capita",
        "gdp": "gdp",
        "population": "population"
    })

    # Keep only useful columns for now (extend if needed)
    keep_cols = ["country", "iso_code", "year", "population", "gdp",
                 "co2_total", "co2_per_capita"]
    df = df[keep_cols]

    # Ensure numeric types
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["population"] = pd.to_numeric(df["population"], errors="coerce")
    df["gdp"] = pd.to_numeric(df["gdp"], errors="coerce")
    df["co2_total"] = pd.to_numeric(df["co2_total"], errors="coerce")
    df["co2_per_capita"] = pd.to_numeric(df["co2_per_capita"], errors="coerce")

    # Drop rows with missing critical values
    df.dropna(subset=["year", "co2_total"], inplace=True)

    return df


if __name__ == "__main__":
    df_clean = load_and_clean("data/Data.csv")

    # Save cleaned data
    os.makedirs("data", exist_ok=True)
    output_path = "data/clean_co2_emissions.csv"
    df_clean.to_csv(output_path, index=False)
    print(f" Cleaned data saved to {output_path}")
