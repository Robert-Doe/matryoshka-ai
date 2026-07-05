"""
gradient_intuition.py  —  Module 02

A gradient answers ONE question: "which way is downhill, and how steep?"
Every model that learns is doing the same thing — rolling downhill on an
'error surface' toward the point of least error. This is gradient descent,
the engine inside linear regression, neural nets, and LLM training alike.

We visualize it in the terminal on a simple bowl-shaped function so you SEE
the ball roll to the bottom.

Run:  python module_02_math/gradient_intuition.py
"""

import numpy as np

line = lambda: print("-" * 60)


# ------------------------------------------------------------------ #
# The "loss" (error) we want to minimize. A simple parabola (a bowl):
#     f(x) = (x - 3)^2 + 2      minimum is at x = 3
# Its gradient (slope) is the derivative:  f'(x) = 2 * (x - 3)
# ------------------------------------------------------------------ #
def f(x):
    return (x - 3) ** 2 + 2

def grad(x):
    return 2 * (x - 3)


def descend(start, lr, steps=25):
    """Roll downhill from `start` with learning rate `lr`."""
    x = start
    history = [x]
    for _ in range(steps):
        x = x - lr * grad(x)     # THE update rule: step opposite the slope
        history.append(x)
    return history


def draw(x, width=50, lo=-2, hi=8):
    """Crude ASCII number line showing where x sits; '|' marks the true minimum."""
    pos = int((x - lo) / (hi - lo) * width)
    minpos = int((3 - lo) / (hi - lo) * width)
    cells = [" "] * (width + 1)
    cells[minpos] = "|"
    cells[max(0, min(width, pos))] = "O"
    return "".join(cells)


print("Minimizing f(x) = (x-3)^2 + 2   (true minimum at x = 3, marked '|')")
print("The ball 'O' should roll toward the mark.\n")

line()
print("A) A good learning rate (0.1) — smooth convergence")
for i, x in enumerate(descend(start=-1.0, lr=0.1)):
    if i % 3 == 0:
        print(f"  step {i:2d}  x={x:6.3f}  f(x)={f(x):6.3f}  [{draw(x)}]")

line()
print("B) Learning rate TOO BIG (1.01) — it overshoots and diverges")
for i, x in enumerate(descend(start=-1.0, lr=1.01, steps=8)):
    print(f"  step {i:2d}  x={x:10.3f}  f(x)={f(x):12.3f}")
print("  >> Too large a step and the ball flies out of the bowl. Errors EXPLODE.")

line()
print("C) Learning rate TOO SMALL (0.001) — barely moves, wastes time")
hist = descend(start=-1.0, lr=0.001, steps=25)
print(f"  after 25 steps x={hist[-1]:.3f} (still far from 3). Would need thousands of steps.")

line()
print("""
The takeaway (you will meet this in EVERY later module):
  * Learning happens by stepping downhill on an error surface.
  * The learning rate is the step size — the most important knob you tune.
  * Too big -> diverge/explode.  Too small -> crawl.  Just right -> learn.
Real models have millions of dimensions instead of one x, but the idea is
identical: compute the gradient, take a step, repeat.
""")
