# Module 05 — Project: Segment and Interpret (No Labels Allowed)

**Goal:** Cluster a real dataset with no labels, justify your choice of k, and —
the hard part — assign defensible human meaning to each machine-found cluster.

**Time:** ~60 min. **Deliverable:** `my_segments.py` + `segments.md` naming and
justifying each cluster.

---

## The data

Use the built-in wine dataset (13 chemical features, no labels needed for clustering):

```python
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

wine = load_wine()
X = StandardScaler().fit_transform(wine.data)   # ALWAYS scale before K-Means
```

*(Ignore `wine.target` while clustering — only peek at it at the very end to check
how well your unsupervised grouping matched the real 3 cultivars.)*

---

## Your tasks

**1. Choose k with the elbow method.** Loop k = 1..8, record `KMeans(k).inertia_`,
print or plot it, and pick the elbow. Justify your choice in one sentence.

**2. Cluster and profile.** Fit K-Means at your chosen k. For each cluster, print
the mean of each ORIGINAL (unscaled) feature. These profiles are how you interpret.

**3. Name each cluster.** In `segments.md`, give each cluster a human label based on
its profile (e.g., "high-alcohol, high-color-intensity group"). The name must follow
from the numbers.

**4. Reality check.** NOW compare your clusters to `wine.target` using a crosstab:

```python
import pandas as pd
print(pd.crosstab(km.labels_, wine.target))
```

How cleanly did your unsupervised clusters recover the real classes? Discuss where
they blurred and why (overlapping chemistry).

---

## Reduce to see it (recommended)

Project to 2-D with PCA and scatter-plot your clusters. Do they look like separate
blobs, or do some overlap? A picture will explain your crosstab.

```python
from sklearn.decomposition import PCA
X2 = PCA(n_components=2).fit_transform(X)
```

---

## Mastery checklist
- [ ] You scaled the features before clustering (and can say why it matters).
- [ ] Your k is justified by the elbow, not picked arbitrarily.
- [ ] Every cluster has a human name that follows from its feature profile.
- [ ] You compared to the true labels and honestly discussed where clusters blurred.
- [ ] You can articulate the "structure vs meaning" division of labor.

## Stretch (security-flavored)
Swap in `DBSCAN` (a density-based clusterer that labels sparse points as noise = -1).
Run it and note which points it flags as noise. Explain in two sentences why a
noise-labeling clusterer like DBSCAN is often better suited to *anomaly detection*
than K-Means (which forces every point into some cluster). This is a real design
choice in behavior-based intrusion detection.

**Next module:** `../module_06_evaluation/headfirst.md` — how to not fool yourself
about how good your model is.
