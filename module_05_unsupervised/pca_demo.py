"""
pca_demo.py  —  Module 05

DIMENSIONALITY REDUCTION: squash many features down to a few, keeping as much
information as possible. PCA (Principal Component Analysis) finds the directions
along which the data varies most, and projects onto them.

Why you care:
  - You can't eyeball 30-dimensional data; PCA lets you plot it in 2D.
  - Fewer features = faster models, less overfitting, less noise.
  - The "explained variance" tells you how much you kept.

We reduce the 30-feature breast-cancer dataset to 2D and show the classes still
separate — proving PCA kept the signal while throwing away 28 dimensions.

Run:  python module_05_unsupervised/pca_demo.py
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

OUTDIR = "module_05_unsupervised/plots"
line = lambda: print("-" * 60)

# 1. LOAD — 30 features per tumor. Far too many to visualize directly.
data = load_breast_cancer()
X, y = data.data, data.target
print(f"Data: {X.shape[0]} samples, {X.shape[1]} features. Can't plot 30-D by eye.")

# 2. SCALE — PCA is sensitive to feature scale; standardize first (Module 02/03).
Xs = StandardScaler().fit_transform(X)

# 3. PCA to 2 components.
pca = PCA(n_components=2).fit(Xs)
X2 = pca.transform(Xs)
line()
print("Reduced 30 features -> 2 principal components.")
ev = pca.explained_variance_ratio_
print(f"   PC1 explains {ev[0]:.1%} of variance")
print(f"   PC2 explains {ev[1]:.1%} of variance")
print(f"   Together: {ev.sum():.1%} of ALL information kept in just 2 numbers.")
print("   >> We threw away 28 dimensions and kept most of the signal.")

# 4. HOW MANY COMPONENTS FOR 95%? (a common real decision)
line()
full = PCA().fit(Xs)
cum = np.cumsum(full.explained_variance_ratio_)
k95 = int(np.argmax(cum >= 0.95)) + 1
print(f"To retain 95% of the variance you need {k95} of 30 components.")
print("   That's the compression PCA buys you — often 3-10x fewer features.")

# 5. PLOT the 2D projection, colored by true diagnosis.
os.makedirs(OUTDIR, exist_ok=True)
plt.figure(figsize=(6, 5))
for cls, name, color in [(0, "malignant", "#ff6b6b"), (1, "benign", "#3ddc84")]:
    m = y == cls
    plt.scatter(X2[m, 0], X2[m, 1], s=18, c=color, label=name, alpha=0.7)
plt.xlabel("PC1"); plt.ylabel("PC2"); plt.legend()
plt.title("30-D tumor data projected to 2-D by PCA")
plt.tight_layout(); plt.savefig(f"{OUTDIR}/pca_2d.png", dpi=110); plt.close()
print(f"\nWrote {OUTDIR}/pca_2d.png — open it: the two classes separate clearly")
print("in 2-D, confirming PCA preserved the structure that matters.")
