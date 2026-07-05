# Module 07 — Head First: Build a Brain From Scratch

> Deep learning powers modern AI — vision, speech, and the LLMs in Module 10. It
> has a reputation for being impenetrable magic. It is not. By the end of this
> module you will have written a neural network *and its learning algorithm* by
> hand, and no framework will ever intimidate you again.

---

## Start with one neuron

A neural network is built from one absurdly simple unit. A single neuron does
exactly two things:

```
   inputs ──▶  1) weighted sum:  z = w1·x1 + w2·x2 + ... + b   ◀── a DOT PRODUCT (M02!)
                     │
                     ▼
              2) activation:   a = squish(z)                  ◀── a nonlinearity
                     │
                     ▼
                  output a
```

Step 1 is the dot product you already know from Module 02. Step 2 runs it through
a "squishing" function (like the sigmoid, which maps anything to a value between 0
and 1). That's the *entire* neuron. `neuron.py` trains one to learn logical AND
using — you guessed it — the gradient descent from Module 02.

---

## Why one neuron isn't enough: the XOR wall

A single neuron can only separate data with a **straight line**. That's fine for
AND and OR. But **XOR** (output 1 when inputs *differ*) can't be split by any
single straight line — and one neuron fails at it, forever, no matter how long you
train.

This isn't a footnote; it's *the* historical reason neural networks stalled for
years and then exploded. The fix: stack neurons into **layers**. A "hidden" layer
lets the network bend the decision boundary into curves. `tiny_net_from_scratch.py`
solves XOR with a 2-neuron hidden layer, proving the point.

**"Deep" learning just means many layers stacked.** Each layer transforms the data
into a representation where the next layer's job is easier. Early layers in an image
network learn edges; later layers learn shapes; the last learns "cat." Depth =
composition of simple transforms into complex understanding.

---

## The heart of it all: backpropagation

Here's the question that makes learning possible in a network with millions of
weights: *when the output is wrong, how much is each individual weight to blame?*

The answer is **backpropagation** — and it's just the **chain rule** from calculus,
applied as bookkeeping. It computes, for every weight, `∂Loss/∂weight`: the gradient,
i.e. that weight's share of the blame. Then gradient descent nudges each weight
downhill by its blame. Do this thousands of times and the network learns.

The four-step training loop (you've seen its baby version since Module 01):

```
   1. FORWARD   push data through the layers → get a prediction
   2. LOSS      measure how wrong the prediction is
   3. BACKWARD  backprop the blame to every weight (chain rule)
   4. UPDATE    each weight steps downhill by its gradient
   ── repeat ──
```

`backprop_explained.ipynb` walks the chain rule through the tiniest possible
network, and *verifies* the hand-derived gradient against a numerical "wiggle it and
measure" estimate — the exact trick engineers use to debug real autograd code.
`tiny_net_from_scratch.py` then runs the full loop on XOR in ~60 lines of NumPy.

---

## Then let the framework do the boring part

Once you've written backprop by hand, `mnist_pytorch.py` shows the same network in
PyTorch — and it's dramatically shorter, because the framework does two things for
you:

- **Autograd** — `loss.backward()` computes all those gradients automatically. That
  one line *is* the entire backward pass you wrote by hand.
- **GPU speed** — the matrix multiplies run in parallel on a graphics card.

The mapping is exact and worth memorizing:

| Your by-hand code | PyTorch |
|---|---|
| `W @ x + b` | `nn.Linear` |
| your `sigmoid` / activation | `nn.ReLU`, `nn.Sigmoid`, … |
| the whole backward pass | `loss.backward()` |
| `w -= lr * grad` | `optimizer.step()` |

Frameworks aren't magic. They're a convenience layer over math you now own.

---

## Security lenses for a deep-learning researcher

Neural nets open a rich attack surface you'll care about:

- **Adversarial examples** — tiny, human-invisible input perturbations that flip a
  network's prediction. They exist *because* of how these gradients work; you can
  literally run gradient descent on the *input* to fool the model. (You'll do a
  version of this thinking in Module 09.)
- **Model/data extraction & poisoning** — big models memorize; memorization leaks
  (Module 04's theme, now at scale).
- **Opacity** — a million weights aren't human-readable, which is exactly why
  interpretability and the ethics work in Module 11 matter for high-stakes use.

Understanding the mechanism (this module) is the prerequisite for attacking or
defending it (your research).

---

## What you'll do

1. `neuron.py` — train a single neuron to learn AND; hit the XOR wall.
2. `tiny_net_from_scratch.py` — a 2-layer net with hand-written backprop solves XOR.
3. `backprop_explained.ipynb` — the chain rule, step by step, checked numerically.
4. `mnist_pytorch.py` — the framework version on real digits (`pip install torch`).
5. `project.md` — hand-code XOR yourself, then reproduce it in PyTorch and classify
   digits at 97%+.

**Next:** `tutorial.html` → `project.md`.
