# Module 09 — Project: Train a CNN, See Inside It, Then Fool It

**Goal:** Train a convolutional network, visualize what it learned, and — the part
that matters for your research — craft an adversarial example that fools it.

**Time:** ~2 hrs. **Deliverable:** `my_cnn.py` + `filters.png` + `adversarial.md`.

**Setup:** `pip install torch` (see Module 07 if you haven't).

---

## Part A — Train a CNN

Adapt `cnn_classifier.py` into `my_cnn.py`. Use Fashion-MNIST-style difficulty by
staying on sklearn digits first (fast), then optionally scale up:

1. Get it training and report test accuracy (aim ≥ 97% on digits).
2. Add one change and measure its effect: e.g., a third conv layer, or dropout
   (`nn.Dropout(0.25)`), or a different learning rate. Report before/after.
3. Print a confusion matrix (reuse Module 06's tool). Which digits confuse it?

---

## Part B — See what it learned

After training, visualize the first conv layer's kernels:

```python
w = model.conv1.weight.detach().numpy()   # shape (out_channels, 1, 3, 3)
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, w.shape[0], figsize=(2*w.shape[0], 2))
for i, ax in enumerate(axes):
    ax.imshow(w[i, 0], cmap="RdBu"); ax.axis("off")
plt.savefig("module_09_vision/filters.png")
```

Do any learned kernels resemble the edge/blob detectors from `see_the_filters.ipynb`?
Note which in a sentence. (They often do — the network rediscovers edge detection.)

---

## Part C — Craft an adversarial example (the research payoff)

Implement the **Fast Gradient Sign Method (FGSM)**: nudge a correctly-classified
image in the direction that increases the loss.

```python
import torch
x = X_te[0:1].clone().requires_grad_(True)   # one correctly-classified image
true = y_te[0:1]
loss = loss_fn(model(x), true)
loss.backward()
epsilon = 0.15
x_adv = (x + epsilon * x.grad.sign()).clamp(0, 1)   # the adversarial image

orig = model(x).argmax(1).item()
adv  = model(x_adv).argmax(1).item()
print(f"original prediction: {orig}, true: {true.item()}")
print(f"adversarial prediction: {adv}  (image barely changed!)")
```

In `adversarial.md`: report whether the prediction flipped, how large `epsilon` had
to be, and **two paragraphs** on the security implications — why does a barely-changed
image fool the model, and what does that mean for deploying vision AI in
security-critical settings (surveillance, malware-image classifiers, biometrics)?

---

## Mastery checklist
- [ ] CNN trains to ≥97% on digits; you reported one architecture change's effect.
- [ ] You visualized learned filters and compared them to hand-designed edge detectors.
- [ ] You produced a working FGSM adversarial example that flips a prediction.
- [ ] `adversarial.md` explains *why* adversarial examples exist (differentiability +
      high dimensions), connecting it to the gradient mechanism from Module 07.

## Stretch (dissertation-adjacent)
Implement a simple defense and measure it: (a) adversarial training (add FGSM examples
to the training set and retrain), or (b) input preprocessing (blur/quantize the image
before classifying). Report how much your defense reduces the attack success rate, and
what it costs in clean accuracy. This attack-then-defend-then-measure loop is the
literal structure of an adversarial-ML research contribution.

**Next module:** `../module_10_genai/headfirst.md` — build real things with LLMs.
