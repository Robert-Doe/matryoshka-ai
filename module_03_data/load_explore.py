"""
load_explore.py  —  Module 03

Step 1 of every ML project: LOOK at your data before you model it. This is
Exploratory Data Analysis (EDA). We load the raw, messy login dataset and let
it show us its own problems: wrong types, missing values, duplicates, outliers,
and inconsistent categories.

The dataset is deliberately dirty. Finding the dirt is the whole exercise.

Run:  python module_03_data/load_explore.py
"""

import pandas as pd

CSV = "module_03_data/messy_data.csv"
line = lambda: print("-" * 64)


def main():
    # Load raw. Note: we do NOT clean anything yet — we want to SEE the mess.
    df = pd.read_csv(CSV)

    print("1) SHAPE & FIRST LOOK")
    print(f"   rows x cols: {df.shape}")
    print(df.head(4).to_string(index=False))
    line()

    print("2) COLUMN TYPES  (red flags hide here)")
    print(df.dtypes.to_string())
    print("   >> 'bytes_sent' should be a number, but pandas read it as 'object'")
    print("      (text). Something non-numeric is in that column. Suspicious.")
    line()

    print("3) MISSING VALUES per column")
    print(df.isna().sum().to_string())
    print("   >> Empty cells in duration_sec, bytes_sent, label. Decide: drop or fill?")
    line()

    print("4) DUPLICATE ROWS")
    dupes = df.duplicated().sum()
    print(f"   fully-duplicated rows: {dupes}")
    print("   >> Duplicates inflate counts and can leak between train/test. Must go.")
    line()

    print("5) CATEGORY CONSISTENCY  (the 'country' and 'label' columns)")
    print("   country values seen:", sorted(df["country"].dropna().unique().tolist()))
    print("   label   values seen:", sorted(df["label"].dropna().unique().tolist()))
    print("   >> 'US' vs 'us', 'GB' vs 'gb', 'normal' vs 'NORMAL' — same thing,")
    print("      different spelling. A model would treat them as different categories.")
    line()

    print("6) NUMERIC SANITY  (coerce bytes_sent to numbers first)")
    bytes_num = pd.to_numeric(df["bytes_sent"], errors="coerce")
    dur_num = pd.to_numeric(df["duration_sec"], errors="coerce")
    print(f"   bytes_sent : min={bytes_num.min():.0f}  max={bytes_num.max():.0f}")
    print(f"   duration   : min={dur_num.min():.0f}  max={dur_num.max():.0f}")
    print("   >> Negative bytes_sent (-500) and negative duration (-12) are impossible.")
    print("      A max duration of 999 and bytes over 1,000,000 look like outliers.")
    line()

    print("SUMMARY OF PROBLEMS FOUND")
    print("   [type]      bytes_sent stored as text (contains 'N/A')")
    print("   [missing]   blanks in bytes_sent, duration_sec, label")
    print("   [dupes]     duplicated event rows")
    print("   [category]  inconsistent casing in country and label")
    print("   [outliers]  negative values; giant exfil-like bytes_sent; 999s duration")
    print("\n   -> Next: clean_data.py fixes each of these, in order.")


if __name__ == "__main__":
    main()
