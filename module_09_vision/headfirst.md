# Module 09 — Head First: Teaching Machines to See

> Computer vision feels like the most "magical" AI — how does a machine know that's
> a cat? The answer is surprisingly concrete, and you already have every piece:
> images are arrays (Module 02), convolution is a dot product (Module 02), and CNNs
> learn their filters by backprop (Module 07). This module assembles them.

---

## The one idea: an image is a grid of numbers

A grayscale image is a 2-D array of brightness values, 0 (black) to 255 (white). A
color image is **three** such grids stacked — Red, Green, Blue. That's the whole
foundation. `pixels_demo.py` builds a tiny image by hand, draws the numbers as
characters so you can literally see the picture *in* the array, and shows that
editing an image (brighten, invert, threshold) is just array arithmetic —
broadcasting, straight from Module 02.

Once you accept "image = numbers," vision stops being mystical. A 1000×1000 color
photo is just 3,000,000 numbers. The only question is: how do we find *patterns*
(edges, shapes, objects) inside all those numbers? Answer: convolution.

---

## Convolution: sliding a pattern detector

**Convolution** slides a small grid of weights — a **kernel** (or filter) — across
the image. At every position it multiplies the kernel by the pixels underneath and
sums them up. That sum is a **dot product** (Module 02, yet again), and it measures
"how much does this spot look like the kernel's pattern?"

Different kernels detect different things:

```
   edge detector (Sobel-x):     blur (average):       sharpen:
     -1  0  1                     1/9 everywhere        0 -1  0
     -2  0  2                                          -1  5 -1
     -1  0  1                                           0 -1  0
```

`convolution_demo.py` applies these by hand to a handwritten digit and saves a
before/after image. You'll *see* the edge kernels light up wherever brightness
changes, the blur smooth things out, the sharpen crisp them up. Each kernel is a
**feature detector**.

---

## The CNN leap: learn the kernels instead of designing them

For decades, people hand-designed kernels (Sobel, Gabor, …). The breakthrough of
**Convolutional Neural Networks (CNNs)** was this: *don't design the kernels — let
the network learn them from data* via backpropagation (Module 07). Feed a CNN
enough labeled images and it discovers, on its own, that edge detectors are useful
in layer 1, curve detectors in layer 2, and so on.

The structure that makes a CNN work:

```
   image ─▶ CONV (learned kernels) ─▶ ReLU ─▶ POOL (shrink) ─▶ CONV ─▶ ... ─▶ classify
              detect edges                     downsample     combine into shapes
```

Two ideas make CNNs efficient and powerful:

- **Weight sharing** — the *same* small kernel slides over the whole image, so a
  CNN has far fewer parameters than a fully-connected net. An edge is an edge
  wherever it appears; why relearn it per location?
- **Hierarchy** — early layers detect simple patterns (edges), later layers combine
  them into complex ones (shapes → objects). Meaning is built up in stages, just
  like the "deep = composition" idea from Module 07.

`cnn_classifier.py` trains a small CNN on handwritten digits (needs
`pip install torch`), and `see_the_filters.ipynb` *visualizes* what the filters
detect — activation maps glowing exactly where their pattern appears.

---

## The most important security topic in vision: adversarial examples

This is where your research instincts should light up. Because a CNN's output is a
smooth, differentiable function of the pixel values, you can do something unsettling:
run gradient descent **on the input image** to find a tiny perturbation — often
invisible to a human — that flips the model's prediction. A stop sign becomes a
speed-limit sign to a self-driving car; a malware image-classifier is bypassed.

These **adversarial examples** aren't a bug in one model; they're a general
consequence of how high-dimensional differentiable classifiers work. The whole
subfield of *adversarial machine learning* — attacks (FGSM, PGD) and defenses
(adversarial training, certified robustness, detection) — grows from this. For a
cybersecurity PhD, this is one of the most natural bridges between AI and your
field, and this module gives you the mechanistic grounding to enter it.

---

## What you'll do

1. `pixels_demo.py` — see that an image is literally an array; edit it with math.
2. `convolution_demo.py` — apply edge/blur/sharpen kernels by hand; save the results.
3. `cnn_classifier.py` — train a CNN that learns its own kernels (`pip install torch`).
4. `see_the_filters.ipynb` — visualize what filters detect (runs without torch).
5. `project.md` — train a CNN on an image dataset, visualize a learned filter, and
   (stretch) craft an adversarial example that fools it.

**Next:** `tutorial.html` → `project.md`.
