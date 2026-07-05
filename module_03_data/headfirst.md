# Module 03 — Head First: Data Is 80% of the Job

> The dirty secret of AI: practitioners spend most of their time not on models
> but on *data*. Get the data right and a simple model wins. Get it wrong and no
> model on earth will save you. This module makes you dangerous with data.

---

## The most important law in AI

**Garbage in, garbage out.** A model learns whatever patterns are in its data —
including the wrong ones. If your data is biased, incomplete, mislabeled, or
leaky, your model faithfully learns to be biased, incomplete, wrong, or cheating.
The model has no way to know the data was bad; it just optimizes.

This has a sharp security edge you'll care about: **data poisoning** is a real
attack. If an adversary can inject crafted rows into your training set, they can
plant a backdoor or degrade the model — no access to the model itself required.
Everything in this module (spotting anomalies, validating types, catching
outliers) is *also* your first line of defense against poisoned data.

---

## The data pipeline (memorize this shape)

```
   COLLECT  →  CLEAN  →  EXPLORE (EDA)  →  VISUALIZE  →  (feed to model)
     │           │            │               │
  get rows   fix types,   understand      see it with
   in         missing,     the shape       your eyes
              dupes,       and signal
              outliers
```

You will run this exact pipeline on a deliberately messy dataset:
`load_explore.py` (see the mess) → `clean_data.py` (fix it, auditable) →
`visualize.py` (tell the story). The dataset is login events labeled
`normal`/`suspicious` — chosen so the lessons map straight onto your world.

---

## What "messy" actually means (the five horsemen)

Real data is never clean. Here are the five problems you'll find in
`messy_data.csv`, and why each is dangerous:

**1. Wrong types.** `bytes_sent` looks numeric but one cell says `N/A`, so the
whole column loads as *text*. Every math operation on it silently breaks or
errors. **Fix:** coerce to numbers; turn un-coercible junk into "missing."

**2. Missing values.** Blank cells. You can't average around them naively.
**Fix:** either drop the row (if the *label* is missing — you can't learn from an
unlabeled example) or *impute* (fill numeric gaps with the median, which is robust
to outliers).

**3. Duplicates.** The same event row appears twice. Duplicates inflate your
counts and — worse — can leak the same example into both training and test sets,
giving you a falsely optimistic score. **Fix:** drop exact duplicates.

**4. Inconsistent categories.** `US` vs `us`, `normal` vs `NORMAL`. To a computer
these are *different* categories, so your "US" group gets split in two. **Fix:**
standardize casing/whitespace.

**5. Outliers & impossible values.** A negative `bytes_sent` (-500) is physically
impossible — it's a data error. A duration of `999` is a suspicious spike. But a
`bytes_sent` of 1,000,000 might be the *actual attack you want to detect*.
**Fix requires judgment:** delete impossible values, cap noise-outliers, but
*keep* outliers that are genuine signal. This is where domain knowledge — yours —
beats any automated rule.

---

## The subtlest, most dangerous bug: data leakage

**Leakage** is when information from the future (or from the answer) sneaks into
your training features, so the model looks brilliant in testing and then fails in
the real world. Classic examples:

- A duplicate row lands in both train and test → the model "predicts" a row it
  already memorized.
- A feature that's secretly derived from the label (e.g., "was_blocked" when
  predicting "is_malicious") → the model just reads the answer.

Leakage is the reason a model can score 99% in your notebook and 60% in
production. Cleaning carefully (dedup, sanity-check features) is your defense.
You'll meet leakage's cousin — the train/test split — head-on in Module 04.

---

## Why we visualize

A table of numbers hides structure; a plot reveals it in one glance. In
`visualize.py` you'll make three charts and each answers a question:

- **Histogram of `bytes_sent`** — *Are there distinct populations?* (Yes: a normal
  cluster and an exfil-sized tail.)
- **Bar chart of failed attempts by label** — *Is this feature useful?* (Yes:
  suspicious logins fail far more often — a strong predictor.)
- **Scatter of duration vs bytes, colored by label** — *Are the classes
  separable?* (Yes: suspicious points sit apart.) If classes separate visually, a
  model can learn the boundary. If they're hopelessly mixed, no model will.

That last plot is a *feasibility check you do before modeling* — it can save you
days of training something that was never going to work.

---

## What you'll do in this module

1. `load_explore.py` — run EDA on the raw file; let it list its own problems.
2. `clean_data.py` — fix each problem in order; every step prints what it changed
   (auditable cleaning = reproducible research).
3. `visualize.py` — generate three story-telling plots into `plots/`.
4. `project.md` — you get a *new* messy dataset and clean it yourself, then
   defend every decision.

**The mindset:** distrust your data until you've looked at it. "I plotted it and
it looked reasonable" is a sentence that prevents more disasters than any model
tweak.

**Next:** `tutorial.html` → `project.md`.
