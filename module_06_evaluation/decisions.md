# Module 06 — DECISIONS

## Decision 1 — Lead with the imbalanced-data trap
The very first script proves accuracy crowns a useless model.
- **Why:** For a security audience this is THE lesson. Attacks are rare, so accuracy
  is actively misleading on exactly the data you care about. Front-loading it means
  every later metric is motivated by a failure you've already felt.

## Decision 2 — Derive all metrics from the confusion matrix
Rather than present precision/recall/F1 as formulas to memorize, we show them
falling out of TP/TN/FP/FN.
- **Why:** Four counts + division is memorable; four disconnected formulas are not.
  Understanding the source means you can reconstruct any metric and reason about
  new ones (e.g., specificity, FPR) without lookup.

## Decision 3 — Frame precision/recall as a policy choice, not a math fact
- **Why:** The single most valuable evaluation skill is knowing *which* metric to
  optimize for a given cost structure. A dissertation that says "we optimized recall
  because a missed intrusion costs far more than a false alarm" reads as rigorous;
  one that reports F1 with no justification reads as rote.

## Decision 4 — Teach the two CV leakage bugs explicitly
Stratification and in-pipeline scaling.
- **Why:** These are the two most common ways real evaluations get silently
  inflated — including in published work. Showing the correct pattern (pipeline
  inside `cross_val_score`) once builds a habit that prevents embarrassing retractions.

## Decision 5 — MEASURE bias and variance, don't just define them
`bias_variance.py` resamples 200 datasets to estimate both empirically.
- **Why:** The trade-off is abstract until you watch variance climb as a number.
  Measuring it also demonstrates a real research technique (Monte-Carlo estimation
  of estimator properties) you can reuse.

## Decision 6 — Reuse datasets students have seen
Breast-cancer, digits — already met in earlier modules.
- **Why:** Removing dataset novelty keeps attention on the *evaluation* concepts,
  which are the point here. Cognitive load spent on new data is load not spent on metrics.

## What we left out
- **ROC/PR curves in depth** — we compute AUC and name PR curves, but full
  threshold-sweep analysis is a natural extension in the project.
- **Calibration** (do predicted probabilities mean what they say?) — important and
  named, but a topic of its own; flagged for later self-study.
- **Statistical significance testing between models** — mentioned via mean±std;
  formal tests (e.g., paired t-test over folds) left as a stretch for the researcher.
