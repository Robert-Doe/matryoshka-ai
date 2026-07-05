"""
metrics_demo.py  —  Module 06

ACCURACY LIES on imbalanced data. This is the single most important evaluation
lesson, and it hits security hardest (attacks are rare, so "always predict
benign" scores ~99%). We build an intrusion-detection scenario where 2% of
traffic is malicious and show why you must look at precision, recall, and F1.

Run:  python module_06_evaluation/metrics_demo.py
"""

import numpy as np
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, roc_auc_score)

rng = np.random.default_rng(0)
line = lambda: print("-" * 62)

# 1. A realistic IMBALANCED problem: 1000 events, 2% are attacks (label 1).
N = 1000
y_true = np.zeros(N, dtype=int)
attack_idx = rng.choice(N, size=20, replace=False)   # only 20 attacks
y_true[attack_idx] = 1
print(f"Intrusion detection: {N} events, {y_true.sum()} attacks ({y_true.mean():.1%}).")
line()

# 2. THE LAZY MODEL — always predicts "benign" (0). Never catches an attack.
lazy = np.zeros(N, dtype=int)
print("MODEL A — 'always predict benign' (catches ZERO attacks):")
print(f"   accuracy  = {accuracy_score(y_true, lazy):.1%}   <-- looks amazing!")
print(f"   recall    = {recall_score(y_true, lazy, zero_division=0):.1%}   <-- catches 0% of attacks")
print(f"   precision = {precision_score(y_true, lazy, zero_division=0):.1%}")
print(f"   F1        = {f1_score(y_true, lazy, zero_division=0):.1%}")
print("   >> 98% accurate and COMPLETELY USELESS. This is the trap.")
line()

# 3. A REAL detector — catches most attacks but with some false alarms.
y_pred = y_true.copy()
# miss 4 real attacks (false negatives)
y_pred[attack_idx[:4]] = 0
# raise 30 false alarms on benign traffic (false positives)
benign = np.where(y_true == 0)[0]
y_pred[rng.choice(benign, size=30, replace=False)] = 1

print("MODEL B — an actual detector (catches 16/20 attacks, 30 false alarms):")
print(f"   accuracy  = {accuracy_score(y_true, y_pred):.1%}   <-- LOWER than the lazy model!")
print(f"   recall    = {recall_score(y_true, y_pred):.1%}   <-- catches 80% of attacks (what we want)")
print(f"   precision = {precision_score(y_true, y_pred):.1%}   <-- of its alarms, this % are real")
print(f"   F1        = {f1_score(y_true, y_pred):.1%}   <-- balances the two")
line()

# 4. THE VOCABULARY — precision vs recall, and why the trade-off is a CHOICE.
print("PRECISION vs RECALL (memorize this):")
print("   Recall    = of all real attacks, what fraction did we CATCH?")
print("               (miss attacks -> low recall -> breach)")
print("   Precision = of all our alarms, what fraction were REAL?")
print("               (too many false alarms -> low precision -> alert fatigue)")
print("   You TRADE them: a paranoid model has high recall, low precision.")
print("   The right balance depends on the cost of a miss vs a false alarm.")
line()

# 5. CONFUSION MATRIX + AUC (a threshold-independent quality score)
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
print("Model B confusion matrix:")
print(f"   true negatives  = {tn:4d}   false positives = {fp:4d} (false alarms)")
print(f"   false negatives = {fn:4d} (missed attacks)   true positives  = {tp:4d}")
# AUC needs scores; simulate a decent scorer correlated with truth
scores = y_true + rng.normal(0, 0.4, N)
print(f"\n   ROC-AUC (ranking quality, 0.5=random, 1.0=perfect) = {roc_auc_score(y_true, scores):.3f}")
print("\nTakeaway: on imbalanced/security data, NEVER report accuracy alone.")
print("Lead with recall (did we catch attacks?) and precision (were alarms real?).")
