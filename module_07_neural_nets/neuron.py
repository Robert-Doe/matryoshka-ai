"""
neuron.py  —  Module 07

A single artificial neuron, from scratch. This is the LEGO brick of all deep
learning. A neuron does exactly two things:

    1. weighted sum:   z = w1*x1 + w2*x2 + ... + bias      (a dot product!)
    2. activation:     a = squish(z)                       (a nonlinearity)

That's it. Stack millions of these and you get GPT. Here we train ONE neuron to
learn the logical AND function, so you can see it work end to end.

Run:  python module_07_neural_nets/neuron.py
"""

import numpy as np

line = lambda: print("-" * 56)

def sigmoid(z):
    """Squish any number into (0, 1). The classic activation."""
    return 1 / (1 + np.exp(-z))

# ------------------------------------------------------------------ #
# Training data for logical AND: output is 1 only when both inputs are 1.
# ------------------------------------------------------------------ #
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 0, 0, 1], dtype=float)     # AND truth table

print("Training ONE neuron to learn logical AND:")
print("   inputs -> target")
for xi, yi in zip(X, y):
    print(f"   {xi.astype(int)} -> {int(yi)}")
line()

# ------------------------------------------------------------------ #
# The neuron's parameters: two weights + one bias. Start random.
# ------------------------------------------------------------------ #
rng = np.random.default_rng(0)
w = rng.normal(0, 1, 2)
b = 0.0
lr = 0.5

# ------------------------------------------------------------------ #
# TRAIN with gradient descent (the Module 02 idea, now on a neuron).
# ------------------------------------------------------------------ #
for epoch in range(5000):
    z = X @ w + b            # 1) weighted sum for all 4 examples at once
    a = sigmoid(z)           # 2) activation -> prediction in (0,1)
    error = a - y            # how wrong

    # gradients (chain rule through the sigmoid + linear step)
    grad_z = error * a * (1 - a)
    grad_w = X.T @ grad_z / len(X)
    grad_b = grad_z.mean()

    w -= lr * grad_w         # 3) step downhill
    b -= lr * grad_b

    if epoch % 1000 == 0:
        loss = np.mean(error ** 2)
        print(f"   epoch {epoch:4d}: loss={loss:.4f}  w={np.round(w,2)}  b={b:.2f}")

line()
print("Trained neuron predictions (should be ~0,0,0,1):")
final = sigmoid(X @ w + b)
for xi, p in zip(X, final):
    print(f"   {xi.astype(int)} -> {p:.3f}  => {int(round(p))}")

line()
print("""
Key ideas you just saw:
  * A neuron = dot product (Module 02!) + a squishing activation.
  * 'Learning' = the same gradient descent from Module 02, adjusting w and b.
  * The activation's NONLINEARITY is what lets networks model curves, not lines.

BUT: a single neuron can only learn patterns separable by a straight line. AND
works; XOR does NOT. To learn XOR you need a LAYER of neurons -> next file,
tiny_net_from_scratch.py. That limitation is literally why we need 'deep' nets.
""")
