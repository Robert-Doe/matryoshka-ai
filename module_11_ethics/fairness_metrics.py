"""
fairness_metrics.py  —  Module 11

"Fair" is not one thing — it's several DIFFERENT, often mutually incompatible,
mathematical definitions. This script computes the three most common fairness
metrics on the same predictions so you see how a model can satisfy one and fail
another. Knowing which definition you mean is half of any responsible-AI argument.

The three:
  1. Demographic parity  — each group approved at the same RATE.
  2. Equal opportunity   — each group's QUALIFIED members approved at the same rate
                           (equal true-positive rate).
  3. Predictive parity   — a "yes" means the same thing for each group
                           (equal precision).

Run:  python module_11_ethics/fairness_metrics.py
"""

import numpy as np

line = lambda: print("-" * 62)

# We use fixed illustrative numbers so the definitions are crystal clear.
# Two groups, each with (y_true, y_pred) for several individuals.
# Group A: mostly qualified, mostly approved.  Group B: approved less.
data = {
    "A": {"y_true": np.array([1,1,1,1,0,0,1,1,0,1]),
          "y_pred": np.array([1,1,1,0,0,1,1,1,0,1])},
    "B": {"y_true": np.array([1,1,0,1,0,0,1,0,1,1]),
          "y_pred": np.array([1,0,0,0,0,0,1,0,0,1])},
}

def rates(y_true, y_pred):
    tp = int(((y_pred == 1) & (y_true == 1)).sum())
    fp = int(((y_pred == 1) & (y_true == 0)).sum())
    fn = int(((y_pred == 0) & (y_true == 1)).sum())
    tn = int(((y_pred == 0) & (y_true == 0)).sum())
    approval = (tp + fp) / len(y_true)                       # for demographic parity
    tpr = tp / (tp + fn) if (tp + fn) else 0                 # for equal opportunity
    precision = tp / (tp + fp) if (tp + fp) else 0           # for predictive parity
    return approval, tpr, precision

print("Three fairness definitions, same predictions, two groups:\n")
print(f"   {'group':>6} {'approval rate':>14} {'true-pos rate':>14} {'precision':>11}")
stats = {}
for g in ("A", "B"):
    ap, tpr, prec = rates(**data[g])
    stats[g] = (ap, tpr, prec)
    print(f"   {g:>6} {ap:>14.2f} {tpr:>14.2f} {prec:>11.2f}")
line()

def gap(i):
    return abs(stats["A"][i] - stats["B"][i])

print("Is each fairness criterion satisfied? (gap ~ 0 means yes)")
print(f"   1. Demographic parity (equal approval rate): gap = {gap(0):.2f}  "
      f"-> {'PASS' if gap(0) < 0.1 else 'FAIL'}")
print(f"   2. Equal opportunity  (equal true-pos rate): gap = {gap(1):.2f}  "
      f"-> {'PASS' if gap(1) < 0.1 else 'FAIL'}")
print(f"   3. Predictive parity  (equal precision):     gap = {gap(2):.2f}  "
      f"-> {'PASS' if gap(2) < 0.1 else 'FAIL'}")
line()
print("""
The uncomfortable truth (an actual theorem):
  When base rates differ between groups, you generally CANNOT satisfy all three
  fairness definitions at once. Improving one can worsen another. This isn't a bug
  in your code — it's a mathematical impossibility (Kleinberg et al., Chouldechova).

So 'is the model fair?' has no purely technical answer. You must choose WHICH
definition matters for THIS decision and JUSTIFY it:
  * Equal opportunity often matters most when a false rejection is the harm
    (denying a qualified person a loan, a job, bail).
  * Predictive parity matters when a positive prediction triggers a consequence
    that must mean the same thing across groups.
Stating and defending that choice is the real deliverable of a fairness analysis —
and exactly the kind of rigor a thesis committee will probe.
""")
