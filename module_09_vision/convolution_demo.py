"""
convolution_demo.py  —  Module 09

CONVOLUTION is the core operation of computer vision. It slides a small grid of
numbers (a 'kernel' or 'filter') across an image, and at each spot computes a
weighted sum (a dot product — Module 02 again). Different kernels detect
different patterns: edges, blurs, sharpening.

The magic of CNNs: instead of hand-designing kernels, the network LEARNS the
best kernels from data via backprop (Module 07). Here we apply them by hand so
you see exactly what a convolutional layer computes.

Run:  python module_09_vision/convolution_demo.py
Then open the PNGs in module_09_vision/plots/.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

OUTDIR = "module_09_vision/plots"
line = lambda: print("-" * 56)

def convolve2d(image, kernel):
    """Slide `kernel` over `image`, computing a weighted sum at each position."""
    kh, kw = kernel.shape
    ph, pw = kh // 2, kw // 2
    padded = np.pad(image, ((ph, ph), (pw, pw)), mode="edge")
    out = np.zeros_like(image, dtype=float)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            patch = padded[i:i + kh, j:j + kw]
            out[i, j] = np.sum(patch * kernel)     # dot product of patch & kernel
    return out

# Kernels: each is a small pattern detector.
kernels = {
    "identity":       np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    "edge (Sobel-x)": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),   # vertical edges
    "edge (Sobel-y)": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),   # horizontal edges
    "blur (3x3 avg)": np.ones((3, 3)) / 9.0,
    "sharpen":        np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
}

# 1. Show a kernel numerically on a tiny image.
print("A kernel is just a small grid of weights. The Sobel-x edge detector:")
print(kernels["edge (Sobel-x)"])
print("At each pixel it computes: sum(3x3 neighborhood * these weights).")
print("Big response where brightness changes left-to-right = a vertical EDGE.")
line()

# 2. Apply every kernel to a real handwritten digit and save a comparison figure.
digits = load_digits()
image = digits.images[0]          # an 8x8 handwritten '0'
os.makedirs(OUTDIR, exist_ok=True)

fig, axes = plt.subplots(1, len(kernels) + 1, figsize=(3 * (len(kernels) + 1), 3))
axes[0].imshow(image, cmap="gray"); axes[0].set_title("original"); axes[0].axis("off")
for ax, (name, k) in zip(axes[1:], kernels.items()):
    result = convolve2d(image, k)
    ax.imshow(result, cmap="gray"); ax.set_title(name, fontsize=9); ax.axis("off")
plt.tight_layout(); plt.savefig(f"{OUTDIR}/convolutions.png", dpi=110); plt.close()

print(f"Applied {len(kernels)} kernels to a handwritten digit.")
print(f"Wrote {OUTDIR}/convolutions.png  — open it and observe:")
print("   * Sobel kernels light up EDGES (where brightness changes).")
print("   * blur smooths; sharpen enhances edges.")
print("   * Each kernel is a different 'feature detector'.")
line()
print("""
The leap to CNNs (next: cnn_classifier.py):
  * A convolutional layer is a STACK of these kernels applied across the image.
  * Crucially, the network LEARNS the kernel weights via backprop instead of us
    hand-picking Sobel etc. Early layers learn edge detectors; deeper layers
    combine edges into shapes, then shapes into objects.
  * Weight sharing (the same small kernel everywhere) is why CNNs need far fewer
    parameters than a plain net — the key efficiency that made vision practical.
""")
