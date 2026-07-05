# Module 06 — Project: The Honest Evaluation

**Goal:** Take an imbalanced dataset, train a classifier, and evaluate it the way a
dissertation committee would demand — right metrics, cross-validated, with a stated
precision/recall policy. Output the evaluation *paragraph* you could paste into a paper.

**Time:** ~75 min. **Deliverable:** `evaluate.py` + `evaluation.md` (the paragraph).

---

## Build an imbalanced problem

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# 3% positives = a realistic rare-event (intrusion/fraud) setting
X, y = make_classification(n_samples=3000, weights=[0.97, 0.03],
                           n_informative=6, random_state=0)
```

---

## Your tasks

**1. Baseline first.** Report the accuracy of "always predict the majority class."
Note how high it is despite catching zero positives.

**2. Cross-validate with MULTIPLE metrics.** Use `cross_validate` with a stratified
5-fold and score accuracy, precision, recall, and F1 at once:

```python
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000, class_weight=None))
cv = StratifiedKFold(5, shuffle=True, random_state=0)
res = cross_validate(pipe, X, y, cv=cv,
                     scoring=["accuracy", "precision", "recall", "f1"])
for m in ["accuracy", "precision", "recall", "f1"]:
    s = res[f"test_{m}"]
    print(f"{m:9s}: {s.mean():.3f} +/- {s.std():.3f}")
```

**3. Improve recall on purpose.** Re-run with `class_weight="balanced"` in the
LogisticRegression. What happens to recall? To precision? Explain the trade-off you
just made in one sentence.

**4. Write the paragraph (`evaluation.md`).** In 4–6 sentences: state the class
imbalance, the baseline, your cross-validated precision/recall/F1 with spreads,
which metric you optimized and *why* (cost of a miss vs. a false alarm), and the
effect of `class_weight="balanced"`.

---

## Mastery checklist
- [ ] You reported the majority-class baseline and explained why its accuracy is misleading.
- [ ] You cross-validated (mean ± std), not a single split.
- [ ] You kept the scaler inside the pipeline (no leakage) and stratified the folds.
- [ ] You stated which metric you optimized and justified it with a cost argument.
- [ ] Your `evaluation.md` paragraph would survive a committee's "why should I believe this?"

## Stretch (research-grade)
Sweep the decision threshold from 0.1 to 0.9 and plot precision and recall vs.
threshold. Identify the threshold that gives you ≥90% recall, and report the
precision you pay for it. This precision–recall-vs-threshold analysis is exactly how
real detection systems are tuned, and it's a defensible figure for a security paper.

**Next module:** `../module_07_neural_nets/headfirst.md` — build a brain from scratch.
