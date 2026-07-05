"""
bias_audit.py  —  Module 11

A model can be highly accurate OVERALL and still be systematically unfair to a
subgroup. This script builds a synthetic loan-approval dataset with a sensitive
attribute (group A vs group B), trains a normal classifier, and AUDITS it: it
measures accuracy AND error rates SEPARATELY per group. The overall number looks
fine; the per-group breakdown reveals the harm.

This is the core move of an algorithmic-fairness audit — and a skill that shows up
in security/compliance review, model risk management, and responsible-AI work.

Run:  python module_11_ethics/bias_audit.py
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

rng = np.random.default_rng(0)
line = lambda: print("-" * 62)

# ------------------------------------------------------------------ #
# 1. SYNTHESIZE data with BAKED-IN historical bias.
#    Two groups. The TRUE creditworthiness is the same distribution for both,
#    but the historical LABELS (past human decisions) approved group B less
#    often for the same signal — a classic "biased labels" scenario. The model
#    will faithfully learn that bias, because that's what "garbage in" means.
# ------------------------------------------------------------------ #
N = 4000
group = rng.integers(0, 2, N)                      # 0 = group A, 1 = group B
income = rng.normal(50, 15, N)                     # genuine signal
history = rng.normal(0, 1, N)                      # genuine signal
true_score = 0.05 * income + 0.8 * history         # real creditworthiness

# Historical approval label: same signal, but group B needed a HIGHER bar.
bias_penalty = 0.6 * group                         # group B penalized in past decisions
approved = (true_score - bias_penalty + rng.normal(0, 0.3, N)) > 2.5
approved = approved.astype(int)

X = np.column_stack([income, history, group])      # note: group is a feature here
Xtr, Xte, ytr, yte, gtr, gte = train_test_split(
    X, approved, group, test_size=0.3, random_state=0)

print("Loan-approval model. Historical labels approved Group B less for the SAME signal.")
print(f"Approval rate in data:  Group A = {approved[group==0].mean():.1%}, "
      f"Group B = {approved[group==1].mean():.1%}")
line()

# 2. TRAIN a perfectly ordinary classifier.
clf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
pred = clf.predict(Xte)

# 3. THE TEMPTING (AND MISLEADING) HEADLINE NUMBER.
print(f"Overall accuracy: {accuracy_score(yte, pred):.1%}   <-- looks fine, ship it?")
line()

# 4. AUDIT: break every metric down BY GROUP.
print("Per-group audit (this is where the harm hides):")
print(f"   {'group':>7} {'accuracy':>9} {'approval rate':>14} {'false-reject rate':>18}")
for g, name in [(0, "A"), (1, "B")]:
    m = gte == g
    acc = accuracy_score(yte[m], pred[m])
    approval = pred[m].mean()                      # how often THIS group gets approved
    # false rejection = truly creditworthy (y=1) but predicted 0
    tn, fp, fn, tp = confusion_matrix(yte[m], pred[m], labels=[0, 1]).ravel()
    false_reject = fn / (fn + tp) if (fn + tp) else 0
    print(f"   {name:>7} {acc:>9.1%} {approval:>14.1%} {false_reject:>18.1%}")

line()
print("""
What the audit reveals:
  * Overall accuracy hid the problem entirely.
  * Group B is APPROVED far less often and FALSELY REJECTED more often, even for
    equal true creditworthiness — the model learned the historical bias in the labels.
  * The model isn't 'broken'; it faithfully reproduced biased training data.
    (Garbage in, garbage out — Module 03, now with human stakes.)

Fixes are NOT purely technical: better labels, reweighting, fairness constraints,
or deciding the model shouldn't be deployed at all. See fairness_metrics.py for the
formal definitions, and note: even DROPPING the 'group' feature doesn't fix it,
because income/history can act as PROXIES for group ('fairness through unawareness'
fails). Try it — remove the group column and re-audit; the gap often persists.
""")
