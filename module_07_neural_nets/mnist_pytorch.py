"""
mnist_pytorch.py  —  Module 07

The SAME neural network as tiny_net_from_scratch.py, but written in PyTorch and
applied to real handwritten digits. Notice how much SHORTER it is: PyTorch does
the backward pass (autograd) and the optimizer step for you. You already know
what it's doing under the hood — that's the whole point of building it by hand first.

We use scikit-learn's 8x8 digits (no download needed) so this runs anywhere.

REQUIRES:  pip install torch      (torch is large; install when you reach M07)
Run:       python module_07_neural_nets/mnist_pytorch.py
"""

import sys

try:
    import torch
    import torch.nn as nn
except ImportError:
    print("PyTorch is not installed yet.")
    print("Install it with:  pip install torch")
    print("(It's large ~2GB; that's why it's optional until Module 07.)")
    print("\nWhile you wait, re-read tiny_net_from_scratch.py — this file is the")
    print("same network, just letting the framework handle backprop for you.")
    sys.exit(0)

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

line = lambda: print("-" * 56)

# 1. DATA — 8x8 grayscale digits, 10 classes.
digits = load_digits()
X = StandardScaler().fit_transform(digits.data).astype("float32")
y = digits.target.astype("int64")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)

X_tr = torch.tensor(X_tr); y_tr = torch.tensor(y_tr)
X_te = torch.tensor(X_te); y_te = torch.tensor(y_te)
print(f"Digits: {X.shape[0]} images of 64 pixels each, 10 classes.")
line()

# 2. MODEL — input(64) -> hidden(32) -> output(10). Compare to the by-hand net:
#    nn.Linear IS 'W @ x + b'. nn.ReLU IS the activation. That's the whole map.
model = nn.Sequential(
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 10),
)
loss_fn = nn.CrossEntropyLoss()             # classification loss
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 3. TRAIN — the four steps you now know by heart, one line each.
print("Training (watch the loss fall):")
for epoch in range(200):
    optimizer.zero_grad()
    logits = model(X_tr)                     # FORWARD
    loss = loss_fn(logits, y_tr)            # LOSS
    loss.backward()                          # BACKWARD (autograd does the chain rule)
    optimizer.step()                         # UPDATE
    if epoch % 40 == 0:
        print(f"   epoch {epoch:3d}: loss = {loss.item():.4f}")

# 4. EVALUATE on the held-out test set.
line()
with torch.no_grad():
    pred = model(X_te).argmax(dim=1)
    acc = (pred == y_te).float().mean().item()
print(f"Test accuracy: {acc:.1%}")
print("""
Compare this file to tiny_net_from_scratch.py:
  * nn.Linear      == your 'W @ x + b'
  * nn.ReLU        == your activation function
  * loss.backward()== the entire backward pass you wrote by hand
  * optimizer.step == your 'w -= lr * grad' update
The framework is a convenience layer over the exact math you already implemented.
""")
