# Module 04 — DECISIONS

## Decision 1 — Synthetic data with a KNOWN rule for regression
`linear_regression.py` generates prices from a rule we control
(50·size + 30·bed − 20·age).
- **Why:** When you know the ground-truth rule, you can verify the model
  *recovered* it. That "aha — it found the 50" moment is impossible with real data
  where the true rule is unknown. It proves learning is real, not luck.
- **Trade-off:** Synthetic data is cleaner than reality. The project uses a *real*
  dataset to restore that messiness.

## Decision 2 — Baseline before model, every time
Both scripts compare against a dumb baseline (predict the mean / most common class).
- **Why:** The most common beginner error is celebrating a number with no reference
  point. "MAE = $12k" is meaningless until you know the baseline was $60k. This
  habit also inoculates against the imbalanced-data trap in Module 06.

## Decision 3 — Linear/logistic regression, not a fancy model
- **Why:** Interpretability. You can read the weights and explain every prediction.
  For a first classifier that matters more than squeezing out 2% accuracy. Powerful
  black boxes come in Module 07, once you can articulate what you gave up for them.

## Decision 4 — Overfitting taught by CAUSING it
`train_test_split_demo.py` deliberately overfits high-degree polynomials.
- **Why:** You understand a failure mode far better after producing it on purpose.
  Seeing test error explode while train error hits zero is more convincing than any
  definition, and it makes the train/test split feel necessary rather than ritual.

## Decision 5 — Introduce the confusion matrix here, metrics later
We show the confusion matrix but defer precision/recall/F1 depth to Module 06.
- **Why:** One new idea at a time. Here the point is the *workflow*; Module 06 is
  entirely about *how to measure* correctly, so metrics get their own stage.

## Decision 6 — Frame overfitting as a security issue, not just accuracy
- **Why:** For this audience, "memorization enables membership inference / data
  extraction" reframes generalization as a privacy control — directly useful for a
  security dissertation, and a hook back into Modules 10–11.

## What we left out
- **Regularization (L1/L2), feature scaling for models, hyperparameter search** —
  named but not drilled; they belong with evaluation (Module 06) and neural nets
  (Module 07) where they're immediately actionable.
- **Tree-based models (random forests, gradient boosting)** — hugely useful in
  practice; introduced conceptually in the project's stretch so the module stays
  focused on the core workflow rather than a zoo of algorithms.
