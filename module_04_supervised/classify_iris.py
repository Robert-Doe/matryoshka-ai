"""
classify_iris.py  —  Module 04

The other kind of supervised learning: CLASSIFICATION (predict a category).
We use the classic Iris dataset (3 flower species from 4 measurements) because
it's small, clean, and lets us focus on the WORKFLOW every classifier follows:

    split -> train -> predict -> evaluate

The exact same workflow classifies malware families, phishing emails, or
network intrusions. Flowers today; threats in your research tomorrow.

Run:  python module_04_supervised/classify_iris.py
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

line = lambda: print("-" * 62)

# 1. LOAD — X = measurements, y = species (0,1,2)
iris = load_iris()
X, y = iris.data, iris.target
print("Iris classification: 3 species from 4 measurements")
print(f"   samples: {X.shape[0]}, features: {list(iris.feature_names)}")
print(f"   classes: {list(iris.target_names)}")
line()

# 2. SPLIT — the single most important habit in ML. Train on one part,
#    TEST on data the model has never seen. 'stratify' keeps class balance.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0, stratify=y)
print(f"1) SPLIT: {len(X_train)} train / {len(X_test)} test (never seen during training)")
line()

# 3. TRAIN — fit a logistic regression classifier.
clf = LogisticRegression(max_iter=500).fit(X_train, y_train)
print("2) TRAINED a LogisticRegression classifier")
line()

# 4. EVALUATE — accuracy on TRAIN vs TEST. The gap is the honesty check.
train_acc = accuracy_score(y_train, clf.predict(X_train))
test_acc = accuracy_score(y_test, clf.predict(X_test))
print(f"3) ACCURACY:  train = {train_acc:.1%}   test = {test_acc:.1%}")
print("   Report TEST accuracy — it estimates real-world performance.")
print("   A big train>>test gap signals OVERFITTING (see train_test_split_demo.py).")
line()

# 5. LOOK CLOSER — per-class report + confusion matrix (WHERE it errs).
print("4) PER-CLASS REPORT (precision/recall per species):")
print(classification_report(y_test, clf.predict(X_test),
                            target_names=iris.target_names))
print("   Confusion matrix (rows=true, cols=predicted):")
print("   ", iris.target_names.tolist())
print(confusion_matrix(y_test, clf.predict(X_test)))
print("   >> Off-diagonal = mistakes. Iris is easy; versicolor/virginica overlap a bit.")
print("      In Module 06 you'll learn why accuracy ALONE is a dangerous single number.")
