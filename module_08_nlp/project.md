# Module 08 — Project: Build a Next-Word Model, Then Diagnose Its Limits

**Goal:** Train a language model on a text *you* choose, generate from it, and then
write a precise diagnosis of where it falls short of a real LLM. Understanding the
gap is the deliverable — it's what turns "I used an LLM" into "I understand LLMs."

**Time:** ~75 min. **Deliverable:** `my_lm.py` + `limits.md`.

---

## Part A — Train and generate

1. Pick a text with a distinct style: song lyrics, a research abstract, log files,
   your own writing — anything a few hundred+ words long. Save it as `corpus.txt`.

2. Adapt `tiny_bigram_lm.py` to read `corpus.txt` and generate. Then **upgrade it to
   a trigram model** (condition on the previous *two* words instead of one):

```python
from collections import defaultdict, Counter
counts = defaultdict(Counter)
for a, b, c in zip(words, words[1:], words[2:]):
    counts[(a, b)][c] += 1        # P(next | previous TWO words)
```

3. Generate from both the bigram and trigram versions. Which reads better? Why?

---

## Part B — Diagnose the gap (`limits.md`)

Write a short analysis. For each real-LLM capability below, state whether your model
has it, and connect the answer to a concept from this module:

| Capability | Does your model have it? | Which module concept explains why/why not? |
|---|---|---|
| Handles words it never saw in training | | tokenization (word vs subword) |
| Understands that "hacker" ≈ "attacker" | | embeddings |
| Uses context from many sentences ago | | attention vs. n-gram window |
| Produces globally coherent paragraphs | | context length + scale |

The trigram sees 2 words of context; an LLM sees thousands via attention. Your
`limits.md` should make that contrast concrete with an example from your own
generated text where the model "forgot" what it was talking about.

---

## Mastery checklist
- [ ] Your trigram model generates more coherent text than the bigram, and you can
      explain why (more context).
- [ ] You can state the three-stage LLM pipeline (tokenize → embed → predict) from memory.
- [ ] Your `limits.md` ties each shortcoming to a specific concept (tokenization,
      embeddings, or attention).
- [ ] You can explain "autoregressive generation" in one sentence.

## Stretch (research-flavored)
Add subword handling: run your BPE from `tokenize_demo.py` over `corpus.txt` first,
then build the n-gram model over *subword* tokens instead of words. Does it now
handle rare/unseen words more gracefully? Write two sentences on the trade-off
between vocabulary size and sequence length — a real design axis in LLM engineering,
and one with security implications (e.g., token-smuggling attacks that hide payloads
across token boundaries).

**Next module:** `../module_09_vision/headfirst.md` — teaching machines to see.
