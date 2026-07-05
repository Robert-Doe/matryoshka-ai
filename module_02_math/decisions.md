# Module 02 — DECISIONS

Why the math module looks the way it does.

## Decision 1 — Four primitives, not a textbook
We teach exactly four things: vectors, dot products, matrices, gradients (plus a
probability aside). We deliberately skip eigenvalues, matrix inverses, formal proofs,
and multivariable calculus notation.
- **Why:** 95% of practical ML intuition comes from these four. The rest can be
  learned on demand when a specific method needs it. Front-loading a math course is
  the #1 reason people quit AI before doing anything.
- **Trade-off:** You won't be able to derive backprop from first principles yet.
  You will be able to *use and reason about* every model in this course. We derive
  backprop concretely in Module 07 when you have a network in front of you.

## Decision 2 — Every concept has a security example
Cosine similarity → anomaly detection. Bayes' rule → malware-scanner base rate.
Naive Bayes → spam filter.
- **Why:** You're a cybersecurity PhD student. Anchoring each abstraction to a
  threat-model you already understand makes it stick and makes it *usable in your
  research*, not just recognizable.
- **Trade-off:** Slightly narrows the examples. Worth it for your audience of one.

## Decision 3 — Measure the speedup, don't assert it
`numpy_basics.py` times a Python loop against a vectorized op and prints the ratio.
- **Why:** "NumPy is fast" is a claim; a measured 500× is a lesson. It also teaches
  the single most important performance habit in ML: never loop over data by hand.

## Decision 4 — Gradient descent is shown FAILING, not just working
We run it with a good, a too-big, and a too-small learning rate.
- **Why:** You learn a knob by breaking it. Seeing error *explode* with a large
  learning rate builds an instinct that a textbook definition never will — and
  you'll recognize that exact failure when training real models later.

## Decision 5 — Build Naive Bayes by hand before ever importing scikit-learn
- **Why:** The same "no magic" principle as Module 01. When you call
  `sklearn.naive_bayes` in Module 04, you'll know precisely what it's computing,
  including the Laplace smoothing that stops unseen words from zeroing a probability.

## What we left out (on purpose)
- **Formal linear algebra** (rank, determinants, eigen-decomposition) — deferred;
  introduced only if/when PCA in Module 05 needs the intuition.
- **Calculus notation** — we use "slope / downhill," not ∂L/∂w, until Module 07.
- **Statistics depth** (hypothesis testing, confidence intervals) — not needed to
  build models; revisited lightly in Module 06 evaluation.
