# Module 02 — Project: Statistics From Scratch

**Goal:** Implement `mean`, `variance`, `standard deviation`, and `normalization`
using only pure Python (no NumPy), then prove your answers match NumPy to 6 decimal
places. Doing the math by hand *once* means you'll trust and debug the library forever.

**Time:** ~45 min. **Deliverable:** a file `my_stats.py` that passes the checks below.

---

## Why this project

Normalization (rescaling features to mean 0, std 1) is something you'll do in almost
every ML pipeline from Module 03 onward — models learn far better on normalized data.
If you've *built* it, you'll know when it's silently going wrong (e.g. a zero-variance
feature causing a divide-by-zero, which is also a subtle data-quality bug worth
catching in your research pipelines).

---

## Your task

Create `module_02_math/my_stats.py` implementing these **without** importing numpy
for the computation:

```python
def mean(xs):
    """Average of a list of numbers."""
    # your code

def variance(xs):
    """Average squared distance from the mean (population variance)."""
    # your code  -- hint: mean of (x - mean)^2

def stddev(xs):
    """Square root of the variance."""
    # your code

def normalize(xs):
    """Return a new list rescaled to mean 0, std 1: (x - mean) / stddev.
    Guard against zero standard deviation (return zeros in that case)."""
    # your code
```

---

## Self-check (paste at the bottom of `my_stats.py`)

```python
if __name__ == "__main__":
    import numpy as np   # ONLY used to grade yourself, not to compute
    data = [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]

    checks = {
        "mean":     (mean(data),     float(np.mean(data))),
        "variance": (variance(data), float(np.var(data))),      # np.var is population var
        "stddev":   (stddev(data),   float(np.std(data))),
    }
    for name, (mine, theirs) in checks.items():
        ok = abs(mine - theirs) < 1e-6
        print(f"{name:9s} mine={mine:.6f}  numpy={theirs:.6f}  {'OK' if ok else 'MISMATCH'}")

    mine_norm = normalize(data)
    np_norm = ((np.array(data) - np.mean(data)) / np.std(data)).tolist()
    max_diff = max(abs(a - b) for a, b in zip(mine_norm, np_norm))
    print(f"normalize max element diff = {max_diff:.2e}  {'OK' if max_diff < 1e-6 else 'MISMATCH'}")
    print(f"normalized mean ~ {mean(mine_norm):.6f} (should be ~0), std ~ {stddev(mine_norm):.6f} (should be ~1)")
```

Success looks like every line printing **OK**, a normalized mean of ~0.000000, and a
normalized std of ~1.000000.

---

## Mastery checklist

- [ ] All four functions match NumPy to 6 decimals.
- [ ] Your `normalize` doesn't crash on a constant list like `[5, 5, 5]` (zero variance).
- [ ] You can explain, in one sentence, why normalization helps a model learn.
- [ ] You can state which primitive from `headfirst.md` normalization relies on (broadcasting).

## Stretch (optional, security-flavored)
Extend `normalize` into a `zscore_anomalies(xs, threshold=3)` that returns the indices
of values more than `threshold` standard deviations from the mean — a one-function
outlier detector. Test it on `[10, 11, 9, 10, 250, 12]`. This is a legitimate,
if simple, anomaly-detection primitive you could cite in a pipeline.

**Next module:** `../module_03_data/headfirst.md` — data is 80% of the job.
