"""
cnn_classifier.py  —  Module 09

A Convolutional Neural Network (CNN) that classifies handwritten digits. It uses
the convolution from convolution_demo.py as a LEARNED layer: the network figures
out its own kernels via backprop (Module 07) instead of us hand-designing them.

Architecture:  conv -> relu -> pool -> conv -> relu -> pool -> flatten -> linear
Each conv layer learns pattern detectors; pooling shrinks the image; the final
linear layer maps learned features to the 10 digit classes.

REQUIRES:  pip install torch
Run:       python module_09_vision/cnn_classifier.py
"""

import sys

try:
    import torch
    import torch.nn as nn
except ImportError:
    print("PyTorch is not installed yet.  Install with:  pip install torch")
    print("\nWhile you wait, run convolution_demo.py (pure NumPy) — a CNN is just")
    print("those convolutions with LEARNED kernels stacked into a network.")
    sys.exit(0)

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

line = lambda: print("-" * 56)

# 1. DATA — 8x8 digit images, shaped (N, 1, 8, 8) for a conv net (1 channel).
digits = load_digits()
X = (digits.images / 16.0).astype("float32")[:, None, :, :]    # add channel dim
y = digits.target.astype("int64")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)
X_tr, y_tr = torch.tensor(X_tr), torch.tensor(y_tr)
X_te, y_te = torch.tensor(X_te), torch.tensor(y_te)
print(f"Digits as images: {tuple(X_tr.shape)}  (N, channels, H, W)")
line()

# 2. THE CNN.
class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3, padding=1)   # learns 8 kernels
        self.conv2 = nn.Conv2d(8, 16, kernel_size=3, padding=1)  # learns 16 kernels
        self.pool = nn.MaxPool2d(2)                              # shrink by 2x
        self.fc = nn.Linear(16 * 2 * 2, 10)                     # 8x8 ->4x4 ->2x2
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))    # 8x8 -> 4x4
        x = self.pool(self.relu(self.conv2(x)))    # 4x4 -> 2x2
        x = x.flatten(1)
        return self.fc(x)

model = SmallCNN()
loss_fn = nn.CrossEntropyLoss()
opt = torch.optim.Adam(model.parameters(), lr=0.01)

# 3. TRAIN (the four-step loop from Module 07).
print("Training the CNN:")
for epoch in range(150):
    opt.zero_grad()
    loss = loss_fn(model(X_tr), y_tr)
    loss.backward()
    opt.step()
    if epoch % 30 == 0:
        print(f"   epoch {epoch:3d}: loss = {loss.item():.4f}")

# 4. EVALUATE.
line()
with torch.no_grad():
    acc = (model(X_te).argmax(1) == y_te).float().mean().item()
print(f"Test accuracy: {acc:.1%}")
print(f"\nThe conv layers learned {8}+{16} kernels from scratch — edge and shape")
print("detectors it discovered itself. See see_the_filters.ipynb to visualize them.")
