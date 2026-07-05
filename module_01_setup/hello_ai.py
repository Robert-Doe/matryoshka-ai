"""
hello_ai.py  —  Module 01

Your first machine-learning program. NO libraries. ~40 lines of pure Python.

Goal: watch a program LEARN. We give it example pairs (x, y) where the true
rule is  y = 2 * x  (the program is NOT told this). It starts with a random
guess for the multiplier `w`, makes predictions, measures how wrong it is, and
nudges `w` in the direction that reduces the error. Repeat.

This is THE loop under all of machine learning:

        data  ->  model  ->  prediction  ->  feedback (error)
          ^                                        |
          |________________ adjust ________________|

Run:  python module_01_setup/hello_ai.py
"""

# 1. DATA — examples of the world. The true rule (y = 2x) is hidden from the model.
data = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]

# 2. MODEL — a single number `w`. Our model is: prediction = w * x.
#    Start with a deliberately-wrong guess so we can watch it improve.
w = 0.0
learning_rate = 0.01  # how big a nudge we make each step (too big = overshoot)

print("Learning the rule behind these (x, y) pairs:")
print(f"  {data}")
print(f"\nStarting guess: prediction = {w:.3f} * x   (the truth is 2 * x)\n")
print(f"{'step':>4} | {'w (our guess)':>14} | {'total error':>12}")
print("-" * 38)

# 3. LEARN — repeat the loop many times.
for step in range(1, 301):
    total_error = 0.0
    gradient = 0.0

    for x, y_true in data:
        y_pred = w * x                 # PREDICTION
        error = y_pred - y_true        # FEEDBACK: how wrong were we?
        total_error += error ** 2      # squared error (always positive)
        gradient += 2 * error * x      # which way is "downhill" for this example

    gradient /= len(data)
    w -= learning_rate * gradient      # ADJUST: nudge w to reduce error

    if step % 30 == 0 or step == 1:
        print(f"{step:>4} | {w:>14.5f} | {total_error:>12.5f}")

print("-" * 38)
print(f"\nLearned rule: prediction = {w:.4f} * x")
print(f"The program discovered the '2' on its own — nobody told it.\n")

# 4. USE IT — make a prediction on a value it never saw.
test_x = 10
print(f"Prediction for x = {test_x}:  {w * test_x:.2f}   (true answer: {2 * test_x})")
print("\nThat's machine learning. Everything else is this idea, scaled up.")
