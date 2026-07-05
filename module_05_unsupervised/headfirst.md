# Module 05 — Head First: Learning Without an Answer Key

> Supervised learning needed labeled examples. But most of the world's data has no
> labels — nobody tagged your network logs as "attack" vs "normal." Unsupervised
> learning finds structure anyway. For a defender, this is how you catch the
> attacks nobody has labeled yet: the *unknown unknowns*.

---

## The core distinction

| | Supervised (Module 04) | Unsupervised (this module) |
|--|--|--|
| Data | inputs **+ correct answers** | inputs **only** |
| Learns | a mapping input → output | the **structure** inside the data |
| Example | "is this email phish?" | "what natural groups of emails exist?" |
| Security use | classify known threats | discover *new* behavior patterns / anomalies |

The catch: with no answer key, the model finds *structure*, not *meaning*. It can
tell you "these 8 users behave differently from the rest" — but **you** decide
whether that's a night-shift team or an intruder. Unsupervised learning proposes;
the human disposes.

---

## Tool 1: Clustering — "group similar things"

**K-Means** is the workhorse, and its loop is almost silly it's so simple:

```
   1. Sprinkle k center points at random.
   2. Assign each data point to its NEAREST center.
   3. Move each center to the AVERAGE of its points.
   4. Repeat 2–3 until the centers stop moving.
```

That's the whole algorithm. Run `kmeans_demo.py` and watch "inertia" (total
tightness of the clusters) drop and then flatten — that flattening is convergence.

**The hard part isn't the algorithm — it's choosing k** (how many clusters). You
usually don't know. The **elbow method** helps: plot inertia for k = 1, 2, 3, …
and look for the "elbow" where adding more clusters stops helping much. The demo
finds the elbow at k=3, which happens to be the truth.

> **Security payoff:** cluster your sessions/flows/users, and the tiny cluster that
> sits far from everything else is a classic anomaly signal (this is the backbone
> of UEBA — User & Entity Behavior Analytics). No labeled attack data required.
> `customer_segments.py` plants exactly such a cluster and lets you find it.

---

## Tool 2: Dimensionality reduction — "squash without losing the point"

Real data often has *dozens* of features. You can't plot 30 dimensions, models
choke on them, and many are redundant or noisy. **PCA (Principal Component
Analysis)** finds the few directions along which the data varies most and projects
onto them.

The key readout is **explained variance**: "these 2 components keep 63% of all the
information." In `pca_demo.py` you'll squash a 30-feature medical dataset down to
**2 numbers** and see the two classes *still separate* when plotted — proof PCA
kept the signal and threw away the noise.

Why a defender cares:
- **Visualization** — see 30-D log data in a 2-D plot to eyeball clusters/outliers.
- **Speed & robustness** — fewer features means faster models and less overfitting.
- **Noise reduction** — low-variance directions are often just noise; dropping them
  can *improve* downstream detection.

---

## The mental model: structure vs. meaning

```
   RAW DATA (no labels)
        │
        ├── clustering ──────▶ "here are the natural groups"
        │                          │
        └── dim. reduction ──▶ "here are the 2–3 axes that matter"
                                   │
                                   ▼
                          YOU interpret & name them
                        (this step is irreducibly human)
```

Unsupervised learning is a *hypothesis generator*. It surfaces patterns; your
domain expertise turns them into decisions. That division of labor is the whole
skill — and it's why unsupervised results always need a human in the loop.

---

## What you'll do

1. `kmeans_demo.py` — watch k-means converge; pick k with the elbow method.
2. `pca_demo.py` — compress 30 features to 2 and see the classes still separate;
   learn how many components you need to keep 95% of the information.
3. `customer_segments.py` — segment users with no labels, name the segments, and
   catch the planted anomaly cluster (the UEBA move).
4. `project.md` — segment a dataset yourself, defend your choice of k, and justify
   the human meaning you assign to each machine-found cluster.

**Next:** `tutorial.html` → `project.md`.
