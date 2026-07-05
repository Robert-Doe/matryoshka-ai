"""
train_test_split_demo.py  —  Module 04

OVERFITTING — the #1 enemy in machine learning — made visible.

An overfit model MEMORIZES the training data (including its noise) instead of
LEARNING the underlying pattern. It scores great on data it has seen and fails
on data it hasn't. We demonstrate this by fitting polynomials of increasing
complexity to noisy data and watching train error fall while TEST error rises.

This is also a security intuition: a model that memorizes can leak its training
data (membership-inference / memorization attacks). Generalization is safety.

Run:  python module_04_supervised/train_test_split_demo.py
"""

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

rng = np.random.default_rng(1)

# True pattern: a gentle curve. Plus noise. The model should learn the CURVE,
# not the noise.
def true_fn(x):
    return np.sin(1.5 * x)

x = np.sort(rng.uniform(0, 4, 40))
y = true_fn(x) + rng.normal(0, 0.25, len(x))

# Split: first 70% train, rest test (data is sorted, but random noise differs).
idx = rng.permutation(len(x))
tr, te = idx[:28], idx[28:]
x_tr, y_tr, x_te, y_te = x[tr], y[tr], x[te], y[te]

print("Fitting polynomials of increasing degree to noisy data.")
print("Watch TRAIN error fall while TEST error eventually EXPLODES.\n")
print(f"{'degree':>6} | {'train RMSE':>11} | {'test RMSE':>10} | verdict")
print("-" * 58)

best_degree, best_test = None, float("inf")
for degree in [1, 2, 3, 5, 9, 15]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(x_tr.reshape(-1, 1), y_tr)
    tr_rmse = mean_squared_error(y_tr, model.predict(x_tr.reshape(-1, 1))) ** 0.5
    te_rmse = mean_squared_error(y_te, model.predict(x_te.reshape(-1, 1))) ** 0.5

    if degree <= 2:
        verdict = "underfit (too simple)"
    elif te_rmse <= best_test * 1.05 and degree <= 5:
        verdict = "good fit"
    else:
        verdict = "OVERFIT (memorizing noise)"
    if te_rmse < best_test:
        best_test, best_degree = te_rmse, degree

    print(f"{degree:>6} | {tr_rmse:>11.3f} | {te_rmse:>10.3f} | {verdict}")

print("-" * 58)
print(f"""
Read the table:
  * Low degree  -> both errors high         = UNDERFIT (model too simple).
  * Mid degree  -> both errors low           = GOOD (learned the real pattern).
  * High degree -> train ~0, test blows up   = OVERFIT (memorized the noise).

Best generalization here was around degree {best_degree}.

The golden rule: JUDGE A MODEL ONLY ON DATA IT HAS NOT SEEN. Train accuracy
is vanity; test accuracy is truth. Everything from here on obeys this.
""")
