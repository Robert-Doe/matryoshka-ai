"""
customer_segments.py  —  Module 05

A realistic end-to-end unsupervised task: SEGMENTATION. We have behavior data
for many "users" and no labels. Clustering groups them; then WE interpret and
name each group. This is exactly how marketing segments customers — and how
security teams profile user/entity behavior (UEBA) to spot the odd one out.

Run:  python module_05_unsupervised/customer_segments.py
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

rng = np.random.default_rng(7)
line = lambda: print("-" * 64)

# 1. SYNTHESIZE users with three hidden behavior types + a few weird ones.
#    Features: [sessions_per_week, avg_session_min, downloads, off_hours_ratio]
def make(n, s, a, d, oh, spread):
    return np.column_stack([
        rng.normal(s, spread, n), rng.normal(a, spread * 3, n),
        rng.normal(d, spread, n), np.clip(rng.normal(oh, 0.08, n), 0, 1)])

casual   = make(120, 3, 12, 2, 0.05, 1.0)     # light, daytime users
power    = make(90, 20, 45, 15, 0.10, 2.0)    # heavy, engaged users
nightowl = make(60, 8, 25, 6, 0.55, 1.5)      # off-hours users
weird    = make(8, 40, 3, 80, 0.85, 1.0)      # tiny group: huge downloads, off-hours
X = np.vstack([casual, power, nightowl, weird])
names = ["sessions/wk", "avg_min", "downloads", "off_hours"]

print(f"{X.shape[0]} users, {X.shape[1]} behavior features, NO labels.")
print("Goal: discover the behavior segments and interpret them.\n")

# 2. SCALE + CLUSTER. We try k=4 (in practice, use the elbow from kmeans_demo).
Xs = StandardScaler().fit_transform(X)
km = KMeans(n_clusters=4, n_init=10, random_state=0).fit(Xs)

# 3. PROFILE each cluster by its AVERAGE (unscaled) feature values.
line()
print("Segment profiles (mean of each feature per cluster):")
print(f"   {'cluster':>8} {'size':>5} | " + " ".join(f"{n:>11}" for n in names))
for c in range(4):
    m = km.labels_ == c
    prof = X[m].mean(axis=0)
    print(f"   {c:>8} {m.sum():>5} | " + " ".join(f"{v:>11.1f}" for v in prof))

# 4. INTERPRET — turn numbers into human labels (this is YOUR job, not the model's).
line()
print("Naming the segments (interpretation is the human's job):")
print("   * Big, high-engagement group   -> 'Power users'")
print("   * Large light-usage group      -> 'Casual users'")
print("   * Off-hours moderate group     -> 'Night owls'")
print("   * TINY group, huge downloads,  -> 'ANOMALIES' — investigate!")
print("     off-hours, few sessions")
line()

# 5. SECURITY PAYOFF — the smallest, most distinctive cluster is often the alert.
sizes = np.bincount(km.labels_)
smallest = int(np.argmin(sizes))
print(f"Smallest cluster is #{smallest} with {sizes[smallest]} users.")
print("In User/Entity Behavior Analytics (UEBA), a tiny cluster far from the others")
print("is a classic unsupervised anomaly signal — no labeled attacks required.")
print("That's why clustering matters for defenders: it finds the unknown-unknowns.")
