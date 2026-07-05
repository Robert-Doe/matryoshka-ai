"""
linear_regression.py  —  Module 04

Supervised learning, the simplest useful case: REGRESSION (predict a number).
We predict house prices from features, and — crucially — we always compare a
model against a dumb BASELINE. "Better than guessing the average" is the bar
every model must clear before you trust it.

Concepts shown:
  - features (X) and target (y)
  - fitting a model = finding the line/plane of best fit (gradient descent's cousin)
  - a baseline (predict the mean) to measure real skill against
  - interpreting the learned weights (which feature matters, and how much)

Run:  python module_04_supervised/linear_regression.py
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

line = lambda: print("-" * 62)
rng = np.random.default_rng(42)

# ------------------------------------------------------------------ #
# 1. MAKE DATA — a synthetic housing market with a KNOWN true rule, so
#    we can check whether the model recovers it.
#    price = 50*size + 30*bedrooms - 20*age + noise   (in $1000s)
# ------------------------------------------------------------------ #
N = 300
size = rng.uniform(0.5, 3.5, N)         # 1000s of sq ft
bedrooms = rng.integers(1, 6, N)
age = rng.uniform(0, 40, N)
noise = rng.normal(0, 15, N)
price = 50 * size + 30 * bedrooms - 20 * age + 100 + noise

X = np.column_stack([size, bedrooms, age])   # feature matrix (N x 3)
y = price                                     # target vector

print("Predicting house price from [size, bedrooms, age]")
print(f"   {N} houses, true rule: 50*size + 30*bed - 20*age + 100 (+noise)")
line()

# ------------------------------------------------------------------ #
# 2. BASELINE — the model has to beat "just predict the average price."
# ------------------------------------------------------------------ #
baseline_pred = np.full_like(y, y.mean())
baseline_mae = mean_absolute_error(y, baseline_pred)
print(f"1) BASELINE (predict mean = ${y.mean():.0f}k):  MAE = ${baseline_mae:.1f}k")
print("   Any model worse than this has learned nothing useful.")
line()

# ------------------------------------------------------------------ #
# 3. FIT — one call. Under the hood it minimizes squared error (M02's
#    gradient descent idea, solved directly for linear models).
# ------------------------------------------------------------------ #
model = LinearRegression().fit(X, y)
pred = model.predict(X)
mae = mean_absolute_error(y, pred)
r2 = r2_score(y, pred)

print(f"2) LINEAR MODEL:  MAE = ${mae:.1f}k   (baseline was ${baseline_mae:.1f}k)")
print(f"   R^2 = {r2:.3f}  (1.0 = perfect, 0.0 = no better than the mean)")
print(f"   -> the model beats the baseline by {baseline_mae - mae:.0f}k of error. It learned.")
line()

# ------------------------------------------------------------------ #
# 4. INTERPRET — read the learned weights. Did it recover the true rule?
# ------------------------------------------------------------------ #
print("3) WHAT DID IT LEARN?  (learned weight vs the true coefficient)")
names = ["size", "bedrooms", "age"]
truth = [50, 30, -20]
for n, w, t in zip(names, model.coef_, truth):
    print(f"   {n:9s}: learned {w:+7.1f}   (true {t:+d})")
print(f"   intercept: learned {model.intercept_:+7.1f}   (true +100)")
print("   >> It recovered the hidden rule from data alone. THAT is supervised learning.")
line()

# ------------------------------------------------------------------ #
# 5. PREDICT — use it on a brand-new house it never saw.
# ------------------------------------------------------------------ #
new_house = np.array([[2.0, 3, 10]])    # 2000 sqft, 3 bed, 10 yrs old
print(f"4) PREDICT new house [size=2.0, bed=3, age=10]:  ${model.predict(new_house)[0]:.0f}k")
print("\n   Interpretability note: because weights are readable, you can EXPLAIN every")
print("   prediction. That transparency matters for audits, fairness, and trust —")
print("   a recurring theme when models make consequential decisions (Module 11).")
