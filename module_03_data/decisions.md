# Module 03 — DECISIONS

## Decision 1 — A messy dataset on purpose
`messy_data.csv` was hand-crafted to contain all five common data problems (type
errors, missing values, duplicates, inconsistent categories, outliers).
- **Why:** Clean tutorial datasets teach nothing about the actual job, which is
  90% cleaning. You can't learn to spot dirt you've never seen.
- **Trade-off:** It's small (36 rows) so you can eyeball every fix. Real datasets
  are millions of rows, but the *categories* of problem are identical.

## Decision 2 — Login events, not iris flowers
The dataset is `normal`/`suspicious` login records.
- **Why:** You're a security researcher. A dataset from your domain makes the
  cleaning judgments (which outliers are noise vs. signal) real, and the leakage /
  poisoning discussions land as things you'll actually face.

## Decision 3 — Cleaning is auditable (every step prints what it changed)
- **Why:** Reproducibility. In research, a silent `df.fillna(0)` buried in a
  notebook is how results become impossible to trust or replicate. Printing "filled
  3 values with median=9600" makes the pipeline a documented transformation.
- **Trade-off:** More verbose code. Correct trade for a teaching tool and for science.

## Decision 4 — Median imputation, not mean
Missing numerics are filled with the column median.
- **Why:** The median is robust to outliers; the mean is dragged around by that
  1,000,000-byte event. Filling with a corrupted mean would inject the very noise
  we're trying to control.

## Decision 5 — Keep the big outliers, cap the noisy ones
We delete impossible negatives, cap a stray 999s duration, but *keep* the huge
`bytes_sent` values.
- **Why:** This is the module's most important lesson: outlier handling requires
  DOMAIN KNOWLEDGE. The giant transfers aren't errors — they're the suspicious
  behavior the whole task exists to catch. A naive "remove all outliers" rule would
  delete the signal. No automated tool can make this call for you.

## Decision 6 — Save plots to files, use the 'Agg' backend
`visualize.py` renders PNGs instead of popping GUI windows.
- **Why:** Works headless, over SSH, in CI, and on any OS without a display server.
  Reliability beats interactivity for a course that must "just run."

## What we left out
- **Feature engineering depth** (creating new features, encoding categoricals for a
  model) — introduced in Module 04 where it's immediately used.
- **Databases / SQL / big-data tools** (Spark, warehouses) — out of scope; the
  concepts transfer, the tooling is a separate skill.
- **Automated data-validation frameworks** (Great Expectations, pandera) — worth
  knowing later; here you build the checks by hand so you understand what they do.
