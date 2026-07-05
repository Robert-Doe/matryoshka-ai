# Module 07 — Project: Engine, Then Car

**Goal:** Prove you understand neural nets at both levels — write one by hand, then
wield the framework. Two parts, each with a concrete success bar.

**Time:** ~2 hrs. **Deliverable:** `xor_by_hand.py` + `digits_pytorch.py` + a short
`notes.md`.

---

## Part A — XOR by hand (the engine)

Starting from `tiny_net_from_scratch.py`, write your OWN `xor_by_hand.py`. Don't
copy — retype it and make these changes so you truly own it:

1. Change the hidden layer from 2 neurons to **4**. Does it still learn XOR? Faster
   or slower?
2. Add a `predict(x)` function that takes a single `[a, b]` and returns 0 or 1.
3. Print the loss every 2000 epochs and confirm it approaches 0.

**Success bar:** your network outputs the correct XOR truth table (0,1,1,0), and you
can explain in `notes.md` what the hidden layer's neurons are each "detecting."

---

## Part B — Digits in PyTorch (the car)

Install torch (`pip install torch`), then adapt `mnist_pytorch.py` into
`digits_pytorch.py`:

1. Add a **second hidden layer**. Report whether test accuracy improves.
2. Try two learning rates (e.g. 0.01 and 0.1) and report which trains better.
3. Print a confusion matrix (reuse the tool from Module 06) to see which digits the
   network confuses.

**Success bar:** ≥ **97%** test accuracy on the digits, plus a confusion matrix
showing where the remaining errors are.

---

## Mastery checklist
- [ ] Your hand-written XOR net produces (0,1,1,0) and you can point at where backprop
      happens in the code.
- [ ] You can map each PyTorch line (`nn.Linear`, `loss.backward()`, `optimizer.step()`)
      to its by-hand equivalent.
- [ ] Your PyTorch digit classifier reaches ≥97% test accuracy.
- [ ] `notes.md` explains, in your words, what "deep" buys you over one neuron.

## Stretch (security research-grade)
Implement a one-step **adversarial example** on your digit model: take a correctly
classified test image, compute the gradient of the loss *with respect to the input
pixels* (`image.requires_grad_(True)`, then `loss.backward()`), and nudge the image
a tiny step in the direction that *increases* loss (the Fast Gradient Sign Method).
Does the model now misclassify a barely-changed image? Write two sentences connecting
this to why deploying neural nets in security-critical settings is risky — a genuine
research observation you could build on.

**Next module:** `../module_08_nlp/headfirst.md` — how machines read, and how LLMs work.
