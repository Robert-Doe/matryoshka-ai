"""
tiny_net_from_scratch.py  —  Module 07

A 2-layer neural network with BACKPROPAGATION written by hand in NumPy — no
PyTorch, no TensorFlow. It learns XOR, the problem a single neuron CANNOT solve.

This ~60-line file contains the entire secret of deep learning:
    forward pass  -> compute prediction
    loss          -> measure wrongness
    backward pass -> use the chain rule to find each weight's blame (gradient)
    update        -> nudge every weight downhill

Once you've written backprop once, no framework is ever magic again.

Run:  python module_07_neural_nets/tiny_net_from_scratch.py
"""

import numpy as np

rng = np.random.default_rng(1)
line = lambda: print("-" * 56)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_deriv(a):
    """Derivative expressed via the output a = sigmoid(z)."""
    return a * (1 - a)

# XOR: output 1 when inputs DIFFER. Not linearly separable -> needs a hidden layer.
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

print("Learning XOR (output=1 when inputs differ) with a 2-2-1 network.")
print("A single neuron CANNOT do this. A hidden layer can.\n")

# --- Parameters: input(2) -> hidden(2) -> output(1) ---
W1 = rng.normal(0, 1, (2, 2)); b1 = np.zeros((1, 2))   # layer 1
W2 = rng.normal(0, 1, (2, 1)); b2 = np.zeros((1, 1))   # layer 2
lr = 0.5

for epoch in range(20000):
    # ---------- FORWARD PASS ----------
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)          # hidden-layer activations
    z2 = a1 @ W2 + b2
    a2 = sigmoid(z2)          # final prediction

    # ---------- LOSS ----------
    loss = np.mean((a2 - y) ** 2)

    # ---------- BACKWARD PASS (chain rule = 'blame assignment') ----------
    d2 = (a2 - y) * sigmoid_deriv(a2)       # blame at output
    dW2 = a1.T @ d2
    db2 = d2.sum(axis=0, keepdims=True)

    d1 = (d2 @ W2.T) * sigmoid_deriv(a1)    # propagate blame back to hidden layer
    dW1 = X.T @ d1
    db1 = d1.sum(axis=0, keepdims=True)

    # ---------- UPDATE (gradient descent) ----------
    W2 -= lr * dW2; b2 -= lr * db2
    W1 -= lr * dW1; b1 -= lr * db1

    if epoch % 4000 == 0:
        print(f"   epoch {epoch:5d}: loss = {loss:.4f}")

line()
print("Final predictions (target: 0,1,1,0):")
for xi, p in zip(X, a2):
    print(f"   {xi.astype(int)} -> {p[0]:.3f}  => {int(round(p[0]))}")

line()
print("""
What just happened is ALL of deep learning, in miniature:
  1. FORWARD  : data flows through layers of (matrix multiply + activation).
  2. LOSS     : we measure how wrong the output is.
  3. BACKWARD : backprop uses the chain rule to compute how much EACH weight
                contributed to the error (its gradient).
  4. UPDATE   : every weight steps downhill. Repeat thousands of times.

PyTorch/TensorFlow just do the BACKWARD step automatically (autograd) and run it
fast on a GPU. You now know what they're doing. See mnist_pytorch.py to meet the
framework version -- same idea, real images, far less code.
""")
