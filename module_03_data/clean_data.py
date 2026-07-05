"""
clean_data.py  —  Module 03

Turn the messy login dataset into a clean, model-ready table. Each step fixes
ONE class of problem found in load_explore.py, and prints what it changed so
the cleaning is auditable (crucial in security research — silent data edits
destroy reproducibility).

Output: writes module_03_data/clean_data.csv

Run:  python module_03_data/clean_data.py
"""

import pandas as pd

RAW = "module_03_data/messy_data.csv"
OUT = "module_03_data/clean_data.csv"
line = lambda: print("-" * 64)


def main():
    df = pd.read_csv(RAW)
    print(f"Loaded raw: {df.shape[0]} rows")
    line()

    # 1) FIX TYPES — coerce numeric columns; bad strings ('N/A') become NaN.
    before_bad = df["bytes_sent"].apply(lambda v: not str(v).replace(".", "").isdigit()).sum()
    df["bytes_sent"] = pd.to_numeric(df["bytes_sent"], errors="coerce")
    df["duration_sec"] = pd.to_numeric(df["duration_sec"], errors="coerce")
    df["failed_attempts"] = pd.to_numeric(df["failed_attempts"], errors="coerce")
    print(f"1) TYPES: coerced bytes_sent/duration to numeric ({before_bad} bad string(s) -> NaN)")

    # 2) STANDARDIZE CATEGORIES — fix casing so 'us' == 'US', 'NORMAL' == 'normal'.
    df["country"] = df["country"].str.upper().str.strip()
    df["label"] = df["label"].str.lower().str.strip()
    print(f"2) CATEGORIES: country -> {sorted(df['country'].dropna().unique())}")
    print(f"               label   -> {sorted(df['label'].dropna().unique())}")

    # 3) DROP DUPLICATES — identical event rows are noise / leakage risk.
    before = len(df)
    df = df.drop_duplicates()
    print(f"3) DUPLICATES: removed {before - len(df)} duplicate row(s)")

    # 4) REMOVE IMPOSSIBLE VALUES — negatives that can't physically exist.
    bad_mask = (df["bytes_sent"] < 0) | (df["duration_sec"] < 0)
    print(f"4) IMPOSSIBLE: dropping {int(bad_mask.sum())} row(s) with negative bytes/duration")
    df = df[~bad_mask]

    # 5) HANDLE MISSING VALUES — impute numerics with the median (robust to
    #    outliers), drop rows missing the LABEL (can't learn without a target).
    before = len(df)
    df = df.dropna(subset=["label"])
    print(f"5a) MISSING LABEL: dropped {before - len(df)} unlabeled row(s)")
    for col in ["bytes_sent", "duration_sec", "failed_attempts"]:
        med = df[col].median()
        n_missing = int(df[col].isna().sum())
        df[col] = df[col].fillna(med)
        if n_missing:
            print(f"5b) MISSING {col}: filled {n_missing} value(s) with median={med:.0f}")

    # 6) CAP OUTLIERS — winsorize duration at the 95th percentile so a stray 999
    #    doesn't dominate. (Keep the giant bytes_sent — those are the ACTUAL
    #    suspicious events we want the model to catch. Domain knowledge decides.)
    cap = df["duration_sec"].quantile(0.95)
    n_capped = int((df["duration_sec"] > cap).sum())
    df["duration_sec"] = df["duration_sec"].clip(upper=cap)
    print(f"6) OUTLIERS: capped {n_capped} duration value(s) at 95th pctile ({cap:.0f}s)")
    print("            (kept large bytes_sent on purpose — that's the signal, not noise)")

    line()
    df.to_csv(OUT, index=False)
    print(f"CLEANED: {len(df)} rows written to {OUT}")
    print("\nClean column types:")
    print(df.dtypes.to_string())
    print("\nClass balance (label):")
    print(df["label"].value_counts().to_string())
    print("\n>> Note the imbalance: far more 'normal' than 'suspicious'. Remember this")
    print("   for Module 06 — accuracy will lie on data this lopsided.")


if __name__ == "__main__":
    main()
