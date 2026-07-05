# Module 04 — Head First: Teaching a Machine to Predict

> This is the heart of machine learning. Supervised learning is 90% of the ML you
> will read about in security papers. Master this module and the whole field opens.

---

## What "supervised" means

You give the model **examples with answers** — inputs paired with the correct
output — and it learns the mapping from input to output. "Supervised" = there's an
answer key during training.

```
   INPUT (features, X)                 OUTPUT (label/target, y)
   ─────────────────────              ───────────────────────
   [size, bedrooms, age]      ─────▶   price          (a number  → REGRESSION)
   [4 flower measurements]    ─────▶   species         (a category → CLASSIFICATION)
   [links, urgency, domain]   ─────▶   phish / legit   (a category → CLASSIFICATION)
```

Two flavors, one idea:
- **Regression** predicts a *number* (price, temperature, bytes transferred).
- **Classification** predicts a *category* (spam/ham, malware family, benign/malicious).

That's it. Everything else — which algorithm, how big the model — is detail.

---

## The universal workflow (burn this in)

Every supervised project, from a 15-line iris demo to a fraud detector at a bank,
follows the same five steps:

```
   1. SPLIT     hold out a TEST set the model never sees
   2. TRAIN     fit the model on the training set
   3. PREDICT   run it on the held-out test set
   4. EVALUATE  measure error/accuracy on that test set
   5. INTERPRET understand WHAT it learned and WHERE it fails
```

Skip step 1 and everything downstream is a lie. Which brings us to the two ideas
that matter most in this entire module.

---

## Big idea #1: Always beat a baseline

Before celebrating a model, ask: *is it better than the dumbest possible guess?*

- Regression baseline: always predict the **average**.
- Classification baseline: always predict the **most common class**.

In `linear_regression.py`, the model must beat "just guess the mean price." A model
that can't beat the baseline has learned *nothing*, no matter how fancy it is. This
single habit will save you from a career of self-deception. (It's also how you'll
catch that a 99%-accurate model on imbalanced data is worthless — the baseline of
"always predict normal" already gets 99%. More in Module 06.)

---

## Big idea #2: Overfitting, the #1 enemy

A model can learn in two very different ways:

- **Generalize** — learn the *underlying pattern*. Works on new data. This is the goal.
- **Memorize** — learn the *training examples themselves*, including their random
  noise. Looks perfect on training data, fails on anything new. This is **overfitting**.

The tell: **train accuracy high, test accuracy low.** The gap between them is your
overfitting alarm.

`train_test_split_demo.py` makes this visible: it fits polynomials of rising
complexity to noisy data. Watch train error march to zero while test error, after
a sweet spot, *explodes*. The wiggly high-degree curve threads every training point
perfectly and predicts garbage between them. That's memorization pretending to be
learning.

**The cure is the train/test split.** By judging the model only on data it never
saw, you catch memorization red-handed. This is why step 1 is sacred.

> **Security connection:** memorization isn't just inaccurate — it's a *leak*. A
> model that memorizes training rows can be probed to reveal them (membership
> inference, training-data extraction). In privacy-sensitive ML, *generalization is
> a security property*, not just a performance one. You'll see this theme again in
> Modules 10 and 11.

---

## Why we start with simple, interpretable models

We use **linear** and **logistic regression** — deliberately simple. Their killer
feature isn't accuracy; it's that you can **read the weights** and know exactly why
the model predicted what it did (`size` matters +50, `age` matters −20). That
transparency is gold for:

- **Debugging** — a nonsense weight reveals a data bug.
- **Trust & audits** — you can explain every decision to a regulator or a review board.
- **Security** — an interpretable model has fewer places for a hidden backdoor to lurk.

Complex models (neural nets, Module 07) trade this transparency for power. Knowing
the trade-off is the mark of an engineer, not a library-caller.

---

## What you'll do

1. `linear_regression.py` — predict house prices, beat the mean baseline, and watch
   the model *recover the hidden rule* (50·size + 30·bed − 20·age).
2. `classify_iris.py` — the full split→train→predict→evaluate workflow on a classifier;
   read the confusion matrix to see *where* it errs.
3. `train_test_split_demo.py` — watch overfitting happen as model complexity rises.
4. `project.md` — build a house-price predictor on real data, beat the baseline,
   then *deliberately overfit it* and watch test accuracy collapse. Breaking it is
   how you truly understand it.

**Next:** `tutorial.html` → `project.md`.
