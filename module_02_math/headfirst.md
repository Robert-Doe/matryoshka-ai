# Module 02 — Head First: The Math That Makes Learning Possible

> You do **not** need a math degree. You need intuition for four ideas. This
> whole module exists to give you those four, and nothing more. As a security
> researcher you'll recognize several of these as tools you already half-use.

---

## Why a security PhD should care about this math

Every ML-based defense you'll read about in your research — anomaly detection,
malware classification, intrusion detection, phishing filters — is built from
exactly four mathematical primitives. If a paper says "we embed each flow as a
feature vector and compute similarity," this module is the reason that sentence
will feel obvious instead of intimidating. And when you later want to *attack* a
model (adversarial ML, evasion, poisoning), you attack these same primitives.

The four ideas:

1. **Vectors** — turning a thing (an email, a network flow, a user) into a list of numbers.
2. **The dot product** — measuring how *similar* two of those things are.
3. **Matrices** — transforming lots of vectors at once (this IS a neural network layer).
4. **Gradients** — figuring out which way to nudge a model to make it *less wrong*.

---

## Idea 1: A vector is a thing turned into numbers

Machines can't reason about "an email" or "a login session." They reason about
**numbers**. So step one of all ML is: describe your thing as a list of numbers —
a *feature vector*.

```
A login session  ->  [ num_logins, downloads, alerts, hours_active ]
                      [     5,          1,        0,        3        ]
```

That's it. A vector. Once your data is vectors, the whole toolbox opens up. Half
of applied ML is the art of choosing *good* numbers to describe your thing —
"feature engineering." A great feature vector makes an easy problem; a bad one
makes an impossible one.

---

## Idea 2: The dot product measures similarity (the MVP operation)

Take two vectors, multiply matching slots, add it all up. One number out.

```
a = [5, 1, 0, 3]
b = [4, 2, 0, 3]
a · b = 5·4 + 1·2 + 0·0 + 3·3 = 20 + 2 + 0 + 9 = 31
```

Big result = the two vectors "point the same way" = **similar**. Small or negative
= different. Normalize it (divide by the lengths) and you get **cosine
similarity**, a number from -1 to 1 that ignores magnitude and measures pure
direction.

Why this matters: **almost everything is similarity in disguise.**
- Search: which documents are most similar to your query?
- Recommendations: which items are similar to what you liked?
- Anomaly detection: which session is *least* similar to normal behavior?
- The "attention" inside every LLM: which earlier words are most relevant (similar) to this one?

Run `numpy_basics.py` and you'll see cosine similarity flag an attacker's weird
behavior profile in a single line. That line is the seed of a real intrusion
detector.

---

## Idea 3: A matrix transforms a whole batch at once

Stack vectors into a grid and you have a **matrix**. Multiply a matrix by your
data and you *transform* it — rotate, stretch, flip, or project it into a new
space where patterns are easier to see.

The punchline you'll use forever:

```
A neural-network layer is just:   output = W · input + b
                                          (a matrix multiply + a shift)
```

That's the whole mechanical secret of deep learning. A "deep" network is many of
these transforms stacked. GPUs exist to do these matrix multiplies fast — that's
literally why they power AI.

Open `linear_algebra.ipynb` to *watch* a matrix rotate a square, and to see one
`@` push a whole batch of examples through a layer.

---

## Idea 4: Gradients tell a model which way is "downhill"

Here's how a model actually learns. Picture its error as a landscape — a bowl.
High ground = very wrong. The bottom = least wrong. The model is a ball that wants
to roll to the bottom.

A **gradient** is just the slope under the ball: *which way is downhill, and how
steep.* The learning rule is comically simple:

```
new_position = old_position − (step_size × slope)
```

Take a step downhill. Measure again. Step again. Thousands of times. That's
**gradient descent**, and it is the engine inside linear regression (M04), neural
nets (M07), and even LLM training. The `step_size` is the **learning rate** — the
single most important knob in ML:

- Too big → you overshoot the bottom and bounce out of the bowl (error explodes).
- Too small → you crawl and never arrive.
- Just right → smooth descent to the minimum.

Run `gradient_intuition.py` and you'll literally watch a ball `O` roll toward the
minimum `|`, then watch it fly out of the bowl when the learning rate is too big.

---

## Bonus: probability = how models say "I'm not sure"

A good classifier never says "spam." It says "0.97 probability spam." Probability
is the language of uncertainty, and **Bayes' rule** is how you update a belief
when evidence arrives.

`probability_demo.py` builds a real spam filter from Bayes' rule by hand — and
shows you the **base-rate fallacy**: a 99%-accurate malware scanner is only ~17%
right when it alerts, because malware is rare. That single insight explains alert
fatigue in a SOC *and* why "accuracy" is a treacherous metric (you'll hammer this
in Module 06).

---

## What you'll do in this module

1. Run `numpy_basics.py` — vectors, dot products, matrices, and a 500× speedup
   that shows why we never loop over data by hand.
2. Work through `linear_algebra.ipynb` — see vectors and matrix transforms *drawn*.
3. Run `probability_demo.py` — Bayes' rule + a hand-built spam classifier.
4. Run `gradient_intuition.py` — watch gradient descent succeed and fail.
5. Do `project.md` — reimplement mean/variance/normalization from scratch and
   match NumPy to 6 decimals. Feeling the math by hand is the point.

**Next:** `tutorial.html` for the guided walkthrough → then `project.md`.
