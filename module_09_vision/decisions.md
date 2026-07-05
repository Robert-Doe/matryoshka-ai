# Module 09 — DECISIONS

## Decision 1 — "An image is an array" before anything else
`pixels_demo.py` draws the numbers as a picture.
- **Why:** Vision intimidates beginners precisely because they don't see the
  substrate. Making the array-picture equivalence tactile (print pixels as chars)
  removes the mystique in five minutes and connects vision to Module 02 array math.

## Decision 2 — Implement convolution by hand before using a framework
`convolution_demo.py` has an explicit sliding-window loop.
- **Why:** Same philosophy as Module 07. "Convolution" is a scary word for "slide a
  small dot-product across the image." Writing the loop makes a Conv2d layer
  obvious later. Seeing hand-set Sobel kernels fire on edges shows what a *learned*
  kernel will end up doing.
- **Trade-off:** The loop is slow; it's for understanding, not production. Real conv
  is heavily optimized (im2col, FFT, GPU).

## Decision 3 — CNN in PyTorch, guarded, on 8x8 digits
No torchvision download, no GPU, and it degrades gracefully without torch.
- **Why:** Reliability again. sklearn digits give a real conv-net problem that trains
  on a CPU in seconds. The graceful guard keeps torch-less learners oriented and
  points them to the NumPy convolution that teaches the same idea.

## Decision 4 — The filters notebook runs WITHOUT torch
`see_the_filters.ipynb` uses hand-set kernels on a real digit; torch is optional.
- **Why:** The pedagogical payoff — "watch a filter fire on the pattern it detects"
  — shouldn't be gated behind a 2GB install. Learners who did install torch get an
  optional peek at real learned weights.

## Decision 5 — Adversarial examples as the headline security topic
Emphasized in headfirst, tutorial, and the project stretch.
- **Why:** For this audience it's the single most valuable connection in the module.
  Adversarial ML is a mature research field sitting exactly at the AI/security border,
  and vision is where it's most visual and intuitive. The module deliberately builds
  the differentiability intuition that makes FGSM/PGD comprehensible.

## What we left out
- **Modern architectures (ResNet, ViT, YOLO), transfer learning, data augmentation** —
  named where relevant; they're refinements once the conv → pool → classify core is solid.
- **Object detection / segmentation** — whole subfields; classification is the right
  first rung and the concepts transfer.
- **Real image files / dataloaders** — using in-memory sklearn digits avoids I/O and
  download friction; the project points to CIFAR/Fashion-MNIST for scaling up.
