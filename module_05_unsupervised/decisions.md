# Module 05 — DECISIONS

## Decision 1 — K-Means as the one clustering algorithm to teach first
There are many (DBSCAN, hierarchical, GMM). We teach K-Means.
- **Why:** Its loop (assign → move centers → repeat) is the most transparent
  intuition for "what clustering even is." Once you own that mental model, the
  others are variations. We name DBSCAN in the project stretch for density/anomaly cases.
- **Trade-off:** K-Means assumes roughly round, similar-size clusters and needs you
  to pick k. We state these limitations explicitly rather than hide them.

## Decision 2 — Teach the elbow method, admit it's a heuristic
- **Why:** "How do I pick k?" is the first real question. The elbow gives a
  principled starting point. But we're honest that it's a guide, not an oracle —
  in real data the elbow is often ambiguous, and domain knowledge breaks ties.

## Decision 3 — PCA on a REAL 30-feature dataset, not a toy
`pca_demo.py` uses the breast-cancer dataset.
- **Why:** The payoff — "we kept the signal after dropping 28 dimensions" — only
  lands when the reduction is dramatic and the classes visibly survive it. A 2→2
  toy would prove nothing.
- **Trade-off:** A medical dataset instead of a security one; the *technique* is
  domain-agnostic and the project brings it back toward your world.

## Decision 4 — Scale features before PCA and K-Means, and say why
Both scripts standardize first.
- **Why:** Both methods are distance/variance based, so an unscaled large-range
  feature (e.g., bytes in the thousands) would dominate a small-range one (a ratio
  in [0,1]). Forgetting to scale is the #1 silent bug in unsupervised pipelines.

## Decision 5 — Frame the small cluster as an anomaly (UEBA)
`customer_segments.py` plants a tiny weird cluster and calls it out.
- **Why:** It connects unsupervised learning to a defensive technique you'll
  actually use/cite, and demonstrates the "structure vs meaning" hand-off: the
  model isolates the group, you decide it's worth investigating.

## Decision 6 — Repeatedly stress "structure, not meaning"
- **Why:** The most common misuse of clustering is treating cluster IDs as ground
  truth. Hammering that labels are arbitrary and interpretation is human prevents a
  whole category of bad conclusions (and bad papers).

## What we left out
- **DBSCAN / hierarchical / GMM** — named, not drilled; introduced when a task
  needs density-based clustering or soft assignments.
- **t-SNE / UMAP** — powerful nonlinear visualizers, but easy to misread; PCA first
  because it's linear, fast, and interpretable via explained variance.
- **Autoencoders** (neural dimensionality reduction) — deferred to after Module 07,
  since they need neural-network foundations.
