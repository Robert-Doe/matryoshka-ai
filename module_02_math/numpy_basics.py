"""
numpy_basics.py  —  Module 02

The math ideas that ALL of machine learning is built from, shown in code:
  1. Vectors            — a list of numbers = a point / a direction
  2. The dot product    — the single most important operation in ML (= similarity)
  3. Matrices           — a stack of vectors; how models transform data in bulk
  4. Broadcasting       — apply one operation to millions of numbers at once
  5. Why NumPy is fast  — vectorization vs a Python loop (measured)

Run:  python module_02_math/numpy_basics.py
"""

import time
import numpy as np

line = lambda: print("-" * 60)


# ------------------------------------------------------------------ #
# 1. A VECTOR is just a list of numbers. It can mean a point in space,
#    a direction, or a "feature vector" describing one example.
# ------------------------------------------------------------------ #
print("1) VECTORS")
user_a = np.array([5, 1, 0, 3])   # e.g. [logins, downloads, alerts, hours_active]
user_b = np.array([4, 2, 0, 3])
print(f"   user_a = {user_a}")
print(f"   user_b = {user_b}")
print(f"   element-wise sum   = {user_a + user_b}")
print(f"   scaled (x2)        = {user_a * 2}")
line()


# ------------------------------------------------------------------ #
# 2. THE DOT PRODUCT — multiply matching elements, add them up.
#    This one number measures how ALIGNED two vectors are.
#    Big dot product = pointing the same way = "similar".
#    This is literally how search, recommendations, and attention work.
# ------------------------------------------------------------------ #
print("2) DOT PRODUCT = similarity")
dot = np.dot(user_a, user_b)
print(f"   user_a . user_b = {dot}")

def cosine_similarity(x, y):
    """Angle-based similarity: 1.0 = identical direction, 0 = unrelated."""
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

print(f"   cosine(a, b)      = {cosine_similarity(user_a, user_b):.4f}  (near 1 = very similar)")
attacker = np.array([50, 0, 40, 1])   # very different behavior profile
print(f"   cosine(a, atkr)   = {cosine_similarity(user_a, attacker):.4f}  (lower = anomalous)")
print("   >> Anomaly detection, in one line. This is the seed of a lot of security ML.")
line()


# ------------------------------------------------------------------ #
# 3. A MATRIX is a grid of numbers = many vectors stacked.
#    Multiplying a matrix by a vector transforms it. Neural network
#    layers are matrix multiplies. That's the whole trick.
# ------------------------------------------------------------------ #
print("3) MATRICES transform data")
M = np.array([[1, 0],
              [0, -1]])            # a transform that flips the y-axis
point = np.array([3, 4])
print(f"   matrix M =\n{M}")
print(f"   point {point}  --M-->  {M @ point}   (@ is matrix multiply)")
print(f"   shapes: M{M.shape} @ v{point.shape} -> {(M @ point).shape}")
line()


# ------------------------------------------------------------------ #
# 4. BROADCASTING — apply one op across a whole array without loops.
#    'Normalize every column' is one line, not a nested for-loop.
# ------------------------------------------------------------------ #
print("4) BROADCASTING")
data = np.array([[10.0, 200.0],
                 [20.0, 400.0],
                 [30.0, 600.0]])
col_mean = data.mean(axis=0)       # mean of each column
col_std = data.std(axis=0)
normalized = (data - col_mean) / col_std   # broadcast subtract + divide
print(f"   column means = {col_mean}")
print(f"   normalized (mean 0, std 1):\n{np.round(normalized, 3)}")
print("   >> Feature scaling. Models learn far better on normalized data (Module 03/04).")
line()


# ------------------------------------------------------------------ #
# 5. WHY NUMPY — the same computation, loop vs vectorized. Measured.
# ------------------------------------------------------------------ #
print("5) SPEED: python loop vs numpy")
N = 2_000_000
xs = np.random.rand(N)

t0 = time.perf_counter()
s = 0.0
for v in xs:            # the slow, "obvious" way
    s += v * v
t_loop = time.perf_counter() - t0

t0 = time.perf_counter()
s2 = np.dot(xs, xs)     # the vectorized way (C under the hood)
t_vec = time.perf_counter() - t0

print(f"   python loop : {t_loop*1000:8.1f} ms")
print(f"   numpy dot   : {t_vec*1000:8.1f} ms")
print(f"   speedup     : {t_loop / max(t_vec, 1e-9):8.0f}x   (same answer: {abs(s-s2) < 1e-3})")
print("\n   Lesson: in ML you NEVER loop over data by hand. You express math on")
print("   whole arrays and let optimized code run it. This is 'vectorization'.")
