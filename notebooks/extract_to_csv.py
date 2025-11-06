"""
Minimal ETL stub:
- Load raw CSV (NYC OpenData or similar)
- Clean/select columns
- Output standardized CSVs for DB load and Tableau
"""
import pandas as pd, os
RAW = "data/raw/nypd_raw.csv"
OUT = "data/processed/arrests_clean.csv"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

if not os.path.exists(RAW):
    raise SystemExit(f"Put your raw CSV at {RAW}")

use_cols = ["ARREST_KEY","ARREST_DATE","AGE_GROUP","PERP_SEX","PERP_RACE","OFNS_DESC","ARREST_PRECINCT"]
df = pd.read_csv(RAW, usecols=use_cols, low_memory=False)
df.rename(columns={
    "ARREST_KEY":"arrest_id",
    "ARREST_DATE":"arrest_date",
    "AGE_GROUP":"age_group",
    "PERP_SEX":"gender",
    "PERP_RACE":"race",
    "OFNS_DESC":"offense",
    "ARREST_PRECINCT":"precinct_id"
}, inplace=True)
df.to_csv(OUT, index=False)
print("✅ Wrote", OUT)
