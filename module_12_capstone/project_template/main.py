"""
main.py  —  Capstone pipeline skeleton

This is the SHAPE of an end-to-end AI project, with the six stages from the course
as clearly-marked TODOs. Fill each stage in for your chosen track. It runs as-is
(on a tiny built-in demo) so you always have a working starting point; replace the
demo pieces with your real project.

Run:  python main.py
"""

import os
import numpy as np

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)
SEED = 0                      # fix seeds everywhere for reproducibility
rng = np.random.default_rng(SEED)
line = lambda: print("-" * 60)


# ================================================================== #
# STAGE 1 — FRAME (Module 01)
# State the problem and what success means BEFORE you model.
# ================================================================== #
PROBLEM = "TODO: what are you predicting/building, and why?"
SUCCESS_CRITERION = "TODO: which metric, and what bar beats the baseline?"
print("STAGE 1 — FRAME")
print(f"  Problem: {PROBLEM}")
print(f"  Success: {SUCCESS_CRITERION}")
line()


# ================================================================== #
# STAGE 2 — DATA (Modules 03-04)
# Load, clean, explore, split. Guard against leakage.
# ================================================================== #
def load_data():
    """TODO: replace this demo with your real dataset (clean it, check leakage)."""
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    d = load_breast_cancer()
    X_tr, X_te, y_tr, y_te = train_test_split(
        d.data, d.target, test_size=0.3, random_state=SEED, stratify=d.target)
    return X_tr, X_te, y_tr, y_te

print("STAGE 2 — DATA")
X_tr, X_te, y_tr, y_te = load_data()
print(f"  train={len(X_tr)}  test={len(X_te)}  positive rate={y_tr.mean():.1%}")
line()


# ================================================================== #
# STAGE 3 — MODEL (Modules 04-07)
# Simplest thing that could work, then iterate.
# ================================================================== #
print("STAGE 3 — MODEL")
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
model.fit(X_tr, y_tr)          # TODO: your model + one measured improvement
print("  trained a baseline-beating model (replace with yours)")
line()


# ================================================================== #
# STAGE 4 — EVALUATE (Module 06)
# Right metric + baseline + honest failure analysis. NEVER train accuracy.
# ================================================================== #
print("STAGE 4 — EVALUATE")
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
# Baseline: predict the majority class.
majority = int(round(y_tr.mean()))
baseline_acc = accuracy_score(y_te, np.full_like(y_te, majority))
pred = model.predict(X_te)
print(f"  baseline (majority) accuracy: {baseline_acc:.3f}")
print(f"  model accuracy: {accuracy_score(y_te, pred):.3f}   F1: {f1_score(y_te, pred):.3f}")
print(f"  confusion matrix:\n{confusion_matrix(y_te, pred)}")
print("  TODO: use the RIGHT metric for your class balance; add cross-validation.")
line()


# ================================================================== #
# STAGE 5 — ETHICS (Module 11)
# Audit for bias / adversarial robustness / prompt injection.
# ================================================================== #
print("STAGE 5 — ETHICS")
print("  TODO: run your responsible-AI check here (see ../evaluation_rubric.md).")
print("  Then run ../../module_11_ethics/red_team_checklist.md on this model.")
line()


# ================================================================== #
# STAGE 6 — WRITE UP (all modules)
# Explain it so someone else believes it. Fill in ../writeup_template.md.
# ================================================================== #
print("STAGE 6 — WRITE UP")
print(f"  Save plots/metrics into {RESULTS_DIR}/ and complete writeup.md.")
print("\nSkeleton complete. Now replace each TODO with your real project.")
