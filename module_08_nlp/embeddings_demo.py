"""
embeddings_demo.py  —  Module 08

An EMBEDDING turns a word into a vector of numbers such that similar words land
near each other. This is the idea that made modern NLP work: "meaning as
geometry." We build real embeddings from scratch using the distributional
hypothesis — "you shall know a word by the company it keeps."

Method (no downloads, fully self-contained):
    1. Build a word x word CO-OCCURRENCE matrix from a corpus.
    2. Reduce it with SVD to dense vectors (this is a classic word-embedding recipe).
    3. Find nearest neighbors by cosine similarity (Module 02!).

Run:  python module_08_nlp/embeddings_demo.py
"""

import numpy as np
from collections import defaultdict

line = lambda: print("-" * 60)

# A small themed corpus so neighbors are meaningful. Two topics: security & animals.
corpus = """
the attacker exploited the server and stole the password from the database
the hacker breached the network and stole the credentials from the server
the malware infected the computer and encrypted the files on the disk
the virus infected the machine and corrupted the files on the drive
the cat chased the mouse across the floor near the door
the dog chased the cat around the yard near the fence
the kitten played with the mouse beside the warm fire
the puppy played with the ball beside the happy child
""".lower().split()

# 1. VOCAB + CO-OCCURRENCE within a small context window.
vocab = sorted(set(corpus))
idx = {w: i for i, w in enumerate(vocab)}
V = len(vocab)
window = 2
co = np.zeros((V, V))
for i, w in enumerate(corpus):
    for j in range(max(0, i - window), min(len(corpus), i + window + 1)):
        if i != j:
            co[idx[w], idx[corpus[j]]] += 1
print(f"Corpus: {len(corpus)} words, vocab {V}. Built {V}x{V} co-occurrence matrix.")

# 2. Weight (log) then SVD to dense d-dim vectors.
weighted = np.log1p(co)
U, S, Vt = np.linalg.svd(weighted)
d = 8
embeddings = U[:, :d] * S[:d]      # word vectors
line()

def neighbors(word, k=4):
    if word not in idx:
        return []
    v = embeddings[idx[word]]
    sims = embeddings @ v / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(v) + 1e-9)
    order = np.argsort(-sims)
    return [(vocab[i], sims[i]) for i in order if vocab[i] != word][:k]

# 3. Nearest neighbors — words used in similar contexts cluster together.
print("Nearest neighbors by cosine similarity (learned from context alone):")
for word in ["attacker", "malware", "cat", "stole", "infected"]:
    nbrs = ", ".join(f"{w}({s:.2f})" for w, s in neighbors(word))
    print(f"   {word:10s} -> {nbrs}")

line()
print("""
What just happened:
  * We never TOLD the model any meanings. It learned that 'attacker' and 'hacker'
    are similar PURELY because they appear in similar contexts.
  * Security words cluster together; animal words cluster together. Meaning
    emerged as GEOMETRY (nearby vectors = similar words).
  * Real embeddings (word2vec, GloVe, and the input layer of every LLM) are this
    idea trained on billions of words with neural nets instead of SVD.

Security angle: embed log lines or commands, and semantically-similar-but-novel
attacks land near known ones -> detection that generalizes beyond exact strings.
""")
