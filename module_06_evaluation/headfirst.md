# Module 06 — Head First: How to Not Fool Yourself

> Richard Feynman: *"The first principle is that you must not fool yourself — and
> you are the easiest person to fool."* This module is that principle applied to
> models. For a researcher, evaluation IS the science; everything else is plumbing.

---

## The one sentence that matters most in this module

**Accuracy lies on imbalanced data — and security data is always imbalanced.**

Attacks are rare. Fraud is rare. Malware is rare. So a model that does nothing —
"always predict benign" — is *automatically* 98–99.9% accurate. It has learned
nothing, catches zero threats, and yet posts a beautiful accuracy number. If you
report accuracy on rare-event data, you are fooling yourself, and possibly your
reviewers.

`metrics_demo.py` shows this brutally: a lazy "always benign" model scores 98%
accuracy while catching **0%** of attacks, and a *real* detector scores *lower*
accuracy while catching 80% of them. Accuracy ranks the useless model above the
useful one. That's why we need better metrics.

---

## The four numbers everything comes from (the confusion matrix)

Every classification metric is derived from four counts:

```
                     PREDICTED
                  negative   positive
   ACTUAL neg  |    TN     |   FP    |   FP = false alarm (cried wolf)
          pos  |    FN     |   TP    |   FN = missed detection (wolf ate sheep)
```

- **TP** — attack, and we caught it. 
- **TN** — benign, and we let it through. 
- **FP** — benign, but we alarmed. (False alarm → alert fatigue.)
- **FN** — attack, but we missed it. (Missed detection → breach.)

From these:

```
accuracy  = (TP + TN) / everything     "how often correct"     (lies when imbalanced)
precision =  TP / (TP + FP)            "of our alarms, % real"  (high = few false alarms)
recall    =  TP / (TP + FN)            "of real attacks, % caught" (high = few misses)
F1        = harmonic mean(precision, recall)  "single balanced score"
```

---

## Precision vs. recall: a trade-off you must CHOOSE

You cannot usually max both. Turn up sensitivity and you catch more attacks
(recall ↑) but also raise more false alarms (precision ↓). The right balance
depends on **the cost of a miss vs. the cost of a false alarm**:

- **Airport threat screening / malware quarantine:** a miss is catastrophic →
  favor **recall** (catch everything, tolerate false alarms).
- **Auto-blocking user accounts / spam deletion:** a false positive angers real
  users or deletes real mail → favor **precision** (only act when confident).

This is a *product/policy decision*, not a math fact. Stating which you optimized —
and why — is a hallmark of a rigorous evaluation section in a paper.

> The base-rate fallacy from Module 02 lives here: even a 99%-accurate scanner
> produces mostly false alarms when the true positive rate in the population is
> tiny. Precision is the metric that exposes that pain.

---

## Don't trust one split: cross-validation

A single train/test split can be lucky or unlucky depending on *which* rows landed
in the test set. `cross_validation.py` shows the same model swinging 2–3% across
five different random splits. Reporting the best one would be cherry-picking.

**k-fold cross-validation** fixes this: chop the data into k folds; each fold is
the test set exactly once while the rest train. You get k scores → report their
**mean ± standard deviation**. The mean estimates performance; the **std tells you
how much to trust it**. A small std = stable result; a large std = fragile.

Two correctness traps the script hammers (both are real ways papers get retracted):
- **Stratify** the folds so each keeps the class balance — otherwise a fold might
  contain *zero* attacks and the metric is meaningless.
- **Keep preprocessing inside the CV loop.** If you scale/normalize using the whole
  dataset before splitting, test information leaks into training and your scores
  come out falsely high. Put the scaler in a pipeline so each fold only sees its
  own training data.

---

## The theory tying it together: bias vs. variance

Underfitting and overfitting (Module 04) are two ends of one trade-off:

- **Bias** = error from being too **simple**. The model is systematically wrong the
  same way every time. (Underfit.)
- **Variance** = error from being too **sensitive** to the exact training data. The
  model swings wildly if you resample. (Overfit.)

`bias_variance.py` *measures* both across 200 resampled datasets and shows bias
falling while variance rises as complexity grows. Total error is their sum, and the
best model sits at the bottom of that U-shaped curve. This is the precise reason
"just use a bigger model" is not always the answer: more capacity trades bias for
variance.

---

## What you'll do

1. `metrics_demo.py` — watch accuracy crown a useless model on imbalanced data,
   then rescue the evaluation with precision/recall/F1.
2. `confusion_matrix.py` — see all metrics derive from four numbers; find *which*
   classes a real model confuses.
3. `cross_validation.py` — replace one shaky split with a mean ± std, and avoid the
   scaling-leak bug.
4. `bias_variance.py` — measure the trade-off behind under/overfitting.
5. `project.md` — evaluate a model on imbalanced data the *right* way and write the
   honest evaluation paragraph you'd defend to a committee.

**The mindset:** a number without a baseline, a spread, and the right metric is a
rumor, not a result.

**Next:** `tutorial.html` → `project.md`.
