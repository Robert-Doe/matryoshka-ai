"""
confusion_matrix.py  —  Module 06

The confusion matrix is the source of truth from which every classification
metric is derived. This script builds one on a real classifier and shows how
accuracy, precision, recall, and F1 all fall out of its four numbers. It also
renders a heatmap so you can SEE where a model confuses classes.

Run:  python module_06_evaluation/confusion_matrix.py
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

OUTDIR = "module_06_evaluation/plots"
line = lambda: print("-" * 62)

# ------------------------------------------------------------------ #
# PART 1 — the 2x2 confusion matrix explained (binary case)
# ------------------------------------------------------------------ #
print("PART 1 — the four numbers everything derives from (binary):")
print("""
                     PREDICTED
                  negative   positive
   ACTUAL neg  |    TN     |   FP    |   FP = false alarm
          pos  |    FN     |   TP    |   FN = missed detection

   accuracy  = (TP+TN) / everything          'how often right'
   precision =  TP / (TP+FP)                 'of alarms, % real'
   recall    =  TP / (TP+FN)                 'of positives, % caught'
   F1        = harmonic mean(precision, recall)
""")
line()

# ------------------------------------------------------------------ #
# PART 2 — a real 10-class confusion matrix (handwritten digits)
# ------------------------------------------------------------------ #
print("PART 2 — a 10-class confusion matrix on handwritten digits")
digits = load_digits()
X_tr, X_te, y_tr, y_te = train_test_split(
    digits.data, digits.target, test_size=0.3, random_state=0, stratify=digits.target)
clf = LogisticRegression(max_iter=2000).fit(X_tr, y_tr)
y_pred = clf.predict(X_te)

cm = confusion_matrix(y_te, y_pred)
print("Confusion matrix (rows=true digit, cols=predicted). Diagonal = correct:")
print(cm)

# find the most-confused off-diagonal pair
off = cm.copy()
np.fill_diagonal(off, 0)
i, j = np.unravel_index(off.argmax(), off.shape)
print(f"\nMost common mistake: true '{i}' predicted as '{j}'  ({off[i, j]} times).")
print("   >> The confusion matrix tells you WHICH classes blur, not just the total error.")
print("      That's actionable: you know exactly where to improve.")
line()

print("Per-class precision/recall/F1:")
print(classification_report(y_te, y_pred, digits=3))

# ------------------------------------------------------------------ #
# PART 3 — save a heatmap
# ------------------------------------------------------------------ #
os.makedirs(OUTDIR, exist_ok=True)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=range(10))
fig, ax = plt.subplots(figsize=(6, 5))
disp.plot(ax=ax, cmap="Blues", colorbar=False)
ax.set_title("Digit classifier — confusion matrix")
plt.tight_layout(); plt.savefig(f"{OUTDIR}/confusion_heatmap.png", dpi=110); plt.close()
print(f"Wrote {OUTDIR}/confusion_heatmap.png — bright off-diagonal cells = confusable digits.")
