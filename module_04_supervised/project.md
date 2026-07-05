# Module 04 — Project: Predict, Beat the Baseline, Then Overfit on Purpose

**Goal:** Build a real regression model end-to-end, prove it beats a baseline, then
*deliberately overfit it* and watch the test score collapse. You'll have felt both
the promise and the failure mode of supervised learning in one sitting.

**Time:** ~75 min. **Deliverable:** `house_predictor.py` + a 5-line
`findings.md` reporting your numbers.

---

## Part A — Build a working predictor

Use scikit-learn's built-in California housing data (no download needed):

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

data = fetch_california_housing()
X, y = data.data, data.target          # y = median house value ($100k units)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)
```

Your tasks:
1. **Baseline:** predict the mean of `y_tr` for every test row; report its MAE.
2. **Model:** fit `LinearRegression`; report test MAE.
3. **Prove it learned:** state how much the model beats the baseline.
4. **Interpret:** print `data.feature_names` alongside `model.coef_`. Which feature
   moves price the most? Does the sign make sense?

---

## Part B — Summon the enemy (overfit on purpose)

Now make a model that *memorizes*. Add polynomial features of rising degree and
watch train vs test error diverge:

```python
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline

for degree in [1, 2, 3, 4]:
    model = make_pipeline(StandardScaler(), PolynomialFeatures(degree), LinearRegression())
    model.fit(X_tr, y_tr)
    tr = mean_absolute_error(y_tr, model.predict(X_tr))
    te = mean_absolute_error(y_te, model.predict(X_te))
    print(f"degree {degree}: train MAE={tr:.3f}  test MAE={te:.3f}  gap={te-tr:+.3f}")
```

**Report in `findings.md`:** at which degree does the train–test *gap* start
widening? That widening gap is overfitting caught in the act.

---

## Mastery checklist
- [ ] Your model's test MAE is clearly below the mean-baseline MAE.
- [ ] You can name the most influential feature and explain its sign
      (hint: median income should push price *up*).
- [ ] You produced a table where train error keeps dropping but test error stops
      improving (or worsens) as degree rises.
- [ ] You can state the golden rule in one sentence: *judge only on unseen data.*

## Stretch (optional, and genuinely useful for your research)
Swap `LinearRegression` for `RandomForestRegressor(n_estimators=100)`. Does test MAE
improve? Then note the trade-off you just made: better accuracy, but you can no
longer read a simple weight per feature (interpretability drops). Write two sentences
on when that trade-off is acceptable in a security setting where decisions must be
explainable (e.g., blocking a user, flagging fraud).

**Next module:** `../module_05_unsupervised/headfirst.md` — finding structure with no labels.
