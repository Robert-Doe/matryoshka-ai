"""
bias_variance.py  —  Module 06

The bias-variance trade-off is the theory behind underfitting vs overfitting
(which you saw in Module 04). This script makes it concrete by measuring, across
many random datasets, how a model's error splits into:

    BIAS^2   — error from being too SIMPLE (systematically wrong)   -> underfit
    VARIANCE — error from being too SENSITIVE to the exact data     -> overfit
    (+ irreducible noise you can never remove)

We sweep model complexity and watch bias fall while variance rises. The best
model sits at the bottom of their sum.

Run:  python module_06_evaluation/bias_variance.py
"""

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

rng = np.random.default_rng(0)
line = lambda: print("-" * 62)

def true_fn(x):
    return np.cos(1.3 * x)                  # the real pattern

def make_dataset(n=30):
    x = rng.uniform(0, 4, n)
    y = true_fn(x) + rng.normal(0, 0.3, n)  # signal + noise
    return x.reshape(-1, 1), y

# Fixed test points where we measure bias and variance.
x_test = np.linspace(0, 4, 50).reshape(-1, 1)
y_test_true = true_fn(x_test.ravel())

print("Measuring bias vs variance across 200 resampled datasets per complexity.\n")
print(f"{'degree':>6} | {'bias^2':>8} | {'variance':>9} | {'total err':>9} | regime")
print("-" * 60)

best = (None, 1e9)
for degree in [1, 2, 3, 5, 9, 14]:
    preds = []
    for _ in range(200):                     # many datasets -> see the spread
        Xtr, ytr = make_dataset()
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression()).fit(Xtr, ytr)
        preds.append(model.predict(x_test))
    preds = np.array(preds)                   # shape (200, 50)

    mean_pred = preds.mean(axis=0)
    bias2 = np.mean((mean_pred - y_test_true) ** 2)     # avg model vs truth
    variance = np.mean(preds.var(axis=0))               # wobble across datasets
    total = bias2 + variance

    if degree <= 2:
        regime = "underfit (high bias)"
    elif degree >= 9:
        regime = "overfit (high variance)"
    else:
        regime = "balanced <- sweet spot"
    if total < best[1]:
        best = (degree, total)
    print(f"{degree:>6} | {bias2:>8.3f} | {variance:>9.3f} | {total:>9.3f} | {regime}")

print("-" * 60)
print(f"""
Read the columns:
  * Simple model (low degree): HIGH bias, low variance -> underfits.
    It's confidently wrong the same way every time.
  * Complex model (high degree): low bias, HIGH variance -> overfits.
    It chases the noise, so it swings wildly between datasets.
  * The best total error is around degree {best[0]} — the balance point.

This is WHY 'just use a bigger model' isn't always right. More capacity cuts
bias but raises variance. Good ML is finding that balance — via the train/test
split and cross-validation you just learned.
""")
