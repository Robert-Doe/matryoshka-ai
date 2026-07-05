"""
tiny_bigram_lm.py  —  Module 08

A LANGUAGE MODEL predicts the next token given previous ones. That's the ENTIRE
job of an LLM, just at colossal scale. Here we build the smallest real language
model — a bigram model — that learns P(next word | current word) by counting,
then GENERATES text by sampling from those probabilities.

This demystifies "the model predicts the next token": you'll watch it happen with
numbers you can inspect.

Run:  python module_08_nlp/tiny_bigram_lm.py
"""

import numpy as np
from collections import defaultdict, Counter

rng = np.random.default_rng(3)
line = lambda: print("-" * 60)

# Training text. Swap this for anything — the model learns ITS style.
text = """
the system logs the event and the system alerts the admin
the admin reviews the event and the admin blocks the attacker
the attacker probes the system and the system logs the probe
the system blocks the attacker and the admin reviews the logs
""".lower().split()

# 1. LEARN P(next | current) by counting adjacent word pairs (bigrams).
counts = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    counts[a][b] += 1

print("Learned next-word distributions (a tiny sample):")
for word in ["the", "system", "admin", "attacker"]:
    dist = counts[word]
    total = sum(dist.values())
    probs = {w: c / total for w, c in dist.most_common(3)}
    pretty = ", ".join(f"{w}={p:.2f}" for w, p in probs.items())
    print(f"   P(next | '{word}') = {{ {pretty} }}")
print("   >> After 'the', the model expects 'system'/'admin'/'attacker'. It LEARNED")
print("      the structure of this text purely by counting — no rules written.")
line()

# 2. GENERATE by sampling: pick a start word, sample the next from its
#    distribution, move to it, repeat. This is 'autoregressive' generation —
#    exactly how an LLM writes, one token at a time, feeding output back as input.
def generate(start, n=14):
    out = [start]
    cur = start
    for _ in range(n):
        dist = counts[cur]
        if not dist:
            break
        words = list(dist.keys())
        probs = np.array(list(dist.values()), dtype=float)
        probs /= probs.sum()
        cur = rng.choice(words, p=probs)     # sample the next token
        out.append(cur)
    return " ".join(out)

print("Generated text (sampling next word each step):")
for _ in range(3):
    print("   -", generate("the"))
line()

print("""
This IS how an LLM works, minus the scale and sophistication:
  * PREDICT the next token from context, as a probability distribution.
  * SAMPLE one, append it, and predict again (autoregressive generation).

The differences that make a real LLM:
  * Context: a bigram sees only the LAST word. GPT/Claude see thousands of prior
    tokens via ATTENTION (see attention_intuition.ipynb).
  * Representation: LLMs use learned embeddings + deep transformers, not raw counts.
  * Scale: billions of parameters trained on trillions of tokens.
But the core loop — 'predict the next token' — is exactly what you just built.
""")
