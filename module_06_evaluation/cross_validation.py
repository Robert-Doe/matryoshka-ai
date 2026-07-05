"""
cross_validation.py  —  Module 06

A single train/test split can LIE — you might get lucky (or unlucky) with which
rows landed in the test set. Cross-validation tests the model on EVERY part of
the data by rotating the test fold, giving you a mean score AND a spread
(how much the score wobbles). The spread is as important as the mean.

Run:  python module_06_evaluation/cross_validation.py
"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, StratifiedKFold, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

line = lambda: print("-" * 62)
data = load_breast_cancer()
X, y = data.data, data.target

# 1. THE PROBLEM — different single splits give different scores.
print("1) One split can be lucky or unlucky. Five different random splits:")
for seed in range(5):
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=seed)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
    print(f"   random_state={seed}: test accuracy = {model.score(Xte, yte):.3f}")
print("   >> Same model, same data, ~2-3% swing just from WHICH rows were held out.")
print("      Reporting one number would be cherry-picking (accidental or not).")
line()

# 2. THE FIX — k-fold cross-validation. Split into k folds; each fold is the
#    test set once while the others train. Average the k scores.
print("2) 5-fold cross-validation: every row is tested exactly once.")
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)   # keep class balance per fold
scores = cross_val_score(pipe, X, y, cv=cv, scoring="accuracy")
for i, s in enumerate(scores):
    print(f"   fold {i+1}: {s:.3f}")
print(f"\n   MEAN accuracy = {scores.mean():.3f}   STD = {scores.std():.3f}")
print(f"   Report it as: {scores.mean():.1%} +/- {scores.std():.1%}")
print("   >> The +/- (spread) tells you how MUCH to trust the mean. A tiny std means")
print("      the result is stable; a big std means your model is sensitive to the split.")
line()

# 3. WHY 'STRATIFIED' AND 'PIPELINE' MATTER — two classic evaluation bugs.
print("3) Two subtle correctness points:")
print("   * STRATIFIED folds keep each class's proportion in every fold — essential")
print("     for imbalanced data, or a fold might contain zero attacks.")
print("   * Putting the SCALER INSIDE the pipeline means each fold is scaled using")
print("     only its own training data. Scaling before CV leaks test info into")
print("     training -> optimistic, WRONG scores. This is a real, common leak.")
print("\nRule: cross-validate, report mean +/- std, and keep all preprocessing")
print("inside the CV loop so no test information leaks in.")
