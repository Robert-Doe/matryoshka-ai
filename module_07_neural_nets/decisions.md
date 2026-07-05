# Module 07 — DECISIONS

## Decision 1 — Build the neuron and backprop BY HAND before any framework
The from-scratch NumPy net comes before PyTorch.
- **Why:** This is the philosophical core of the whole course. People who start
  with PyTorch treat neural nets as magic incantations and can't debug them. People
  who write backprop once understand every framework forever. The ~60 lines are the
  single highest-leverage code in the course.
- **Trade-off:** Slower to a "real" result. Completely worth it.

## Decision 2 — Use XOR as the hero problem
- **Why:** XOR is the smallest problem that a single neuron *cannot* solve but a
  hidden layer can. It makes the entire case for depth in four data points, and it's
  historically the exact problem that stalled and then revived neural networks. No
  toy is more pedagogically loaded.

## Decision 3 — Verify backprop against a numerical gradient
The notebook checks the analytic gradient with a finite-difference estimate.
- **Why:** It proves the math is right (not just plausible) and teaches gradient
  checking — a genuine professional debugging technique for autograd code. Trust,
  but verify.

## Decision 4 — Keep the PyTorch model tiny and use 8x8 digits
No torchvision, no MNIST download, no GPU required.
- **Why:** Reliability. A course that needs a 2GB download and a working CUDA setup
  to reach lesson 7 loses people. sklearn's digits give a real 10-class image
  problem that trains in seconds on a CPU.

## Decision 5 — Guard the torch import gracefully
`mnist_pytorch.py` prints install instructions instead of crashing if torch is absent.
- **Why:** torch is the one heavy dependency. A hard ImportError traceback reads as
  "the course is broken." A friendly message keeps the learner oriented and points
  back to the from-scratch file they can run right now.

## Decision 6 — Introduce adversarial examples as a security hook
- **Why:** For this researcher, the most compelling reason to understand the
  gradient mechanism is that adversarial attacks *are* that mechanism turned on the
  input. It reframes "how nets learn" as "how nets can be fooled" — directly
  relevant to a security dissertation, and a bridge to Module 09.

## What we left out
- **CNNs / RNNs / transformers architecture detail** — CNNs get their own treatment
  in Module 09; transformers/attention in Module 08. Here we keep to the fully-
  connected fundamentals so backprop is the star.
- **Regularization, dropout, batch norm, optimizers beyond Adam** — named but not
  drilled; they're refinements on the core loop, best learned once the loop is solid.
- **GPU/CUDA setup** — deliberately avoided so everything runs on a laptop CPU.
