"""
kmeans_demo.py  —  Module 05

CLUSTERING: find groups in data when NOBODY tells you the groups.
K-Means is the workhorse. The idea is almost embarrassingly simple:

    1. Drop k "center" points at random.
    2. Assign each data point to its nearest center.
    3. Move each center to the average of its assigned points.
    4. Repeat 2-3 until nothing moves.

We run it step by step so you SEE the centers converge, then show how to pick k
with the "elbow" method. Security tie-in: cluster network sessions and the odd,
tiny cluster is often your anomaly.

Run:  python module_05_unsupervised/kmeans_demo.py
"""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

rng = np.random.default_rng(0)
line = lambda: print("-" * 60)

# 1. DATA — 3 natural blobs, but we PRETEND we don't know there are 3.
X, true_labels = make_blobs(n_samples=300, centers=3, cluster_std=0.9,
                            random_state=0)
print("300 points that fall into some number of natural groups.")
print("K-Means gets NO labels — it must discover the structure itself.\n")

# 2. WATCH IT CONVERGE — run k-means for increasing iteration counts and
#    print how far the centers moved (inertia = total within-cluster distance).
line()
print("Watching k=3 converge (inertia = tightness; lower = better):")
prev = None
for n_iter in [1, 2, 3, 5, 10]:
    km = KMeans(n_clusters=3, n_init=1, max_iter=n_iter, random_state=0).fit(X)
    delta = "" if prev is None else f"  (improved {prev - km.inertia_:6.1f})"
    print(f"   after {n_iter:2d} iterations: inertia = {km.inertia_:7.1f}{delta}")
    prev = km.inertia_
print("   >> Inertia drops then flattens — that flattening is convergence.")

# 3. PICK k WITH THE ELBOW METHOD — try several k, plot inertia vs k. The
#    'elbow' where improvement sharply slows is a good k.
line()
print("Choosing k with the elbow method (inertia for each k):")
inertias = []
for k in range(1, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    inertias.append(km.inertia_)
    bar = "#" * int(km.inertia_ / max(inertias) * 40)
    print(f"   k={k}: inertia={km.inertia_:7.1f}  {bar}")
drops = [inertias[i-1] - inertias[i] for i in range(1, len(inertias))]
elbow = drops.index(min(drops[1:])) + 1 if len(drops) > 1 else 2
print(f"   >> The 'elbow' (where gains flatten) is around k=3 — the true answer.")
print("      In real problems you don't KNOW the truth; the elbow is your guide.")

# 4. FINAL CLUSTERING
line()
km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
print("Final cluster sizes:", np.bincount(km.labels_).tolist())
print("Cluster centers (the 'prototype' of each group):")
print(np.round(km.cluster_centers_, 2))
print("\nNote: cluster LABELS are arbitrary (cluster 0 isn't 'better' than 1).")
print("Unsupervised learning finds STRUCTURE, not meaning — YOU assign the meaning.")
