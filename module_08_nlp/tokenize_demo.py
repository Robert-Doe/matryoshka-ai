"""
tokenize_demo.py  —  Module 08

Before a model can read text, the text must become NUMBERS. That conversion is
tokenization, and it's the first thing that happens to every prompt you send an
LLM. We show three levels:

    1. word tokenization      — split on spaces (simple, but huge vocab)
    2. character tokenization  — every char is a token (tiny vocab, long sequences)
    3. subword (BPE-style)     — merge frequent pairs; what real LLMs use

Then we map tokens -> integer IDs, exactly like a model's tokenizer.

Run:  python module_08_nlp/tokenize_demo.py
"""

from collections import Counter

line = lambda: print("-" * 60)
text = "the attacker sent a phishing email to the unsuspecting user"

# 1. WORD TOKENS
words = text.split()
print("1) WORD tokens:", words)
print(f"   {len(words)} tokens, vocab size grows with every new word you ever see.")
print("   Problem: 'phish', 'phishing', 'phished' become 3 unrelated tokens,")
print("   and rare/unseen words become 'unknown'. That's lossy.")
line()

# 2. CHARACTER TOKENS
chars = list(text)
print("2) CHARACTER tokens (first 20):", chars[:20])
print(f"   Only {len(set(chars))} unique symbols -> tiny vocab, but sequences get LONG")
print("   and the model must relearn spelling. Rarely used alone.")
line()

# 3. SUBWORD via a tiny Byte-Pair-Encoding (BPE) — the real-world approach.
#    Repeatedly merge the most frequent adjacent pair of symbols into one token.
print("3) SUBWORD tokens (BPE): merge frequent character pairs into subwords")
corpus = "phishing phisher phished phishes fishing".split()
# represent each word as a list of chars ending with '_' (word boundary)
tokens = [list(w) + ["_"] for w in corpus]

def most_frequent_pair(seqs):
    pairs = Counter()
    for seq in seqs:
        for i in range(len(seq) - 1):
            pairs[(seq[i], seq[i + 1])] += 1
    return pairs.most_common(1)[0] if pairs else (None, 0)

for step in range(6):
    (pair, count) = most_frequent_pair(tokens)
    if pair is None or count < 2:
        break
    merged = "".join(pair)
    # merge that pair everywhere
    new_tokens = []
    for seq in tokens:
        out, i = [], 0
        while i < len(seq):
            if i < len(seq) - 1 and (seq[i], seq[i + 1]) == pair:
                out.append(merged); i += 2
            else:
                out.append(seq[i]); i += 1
        new_tokens.append(out)
    tokens = new_tokens
    print(f"   merge #{step+1}: joined {pair} (seen {count}x) -> '{merged}'")

print("   result for 'phishing':", tokens[0])
print("   >> BPE discovered 'phish' as a reusable subword! Now 'phishing',")
print("      'phisher', 'phished' SHARE the 'phish' token -> the model generalizes.")
print("      This is why GPT/Claude tokenizers use subwords: balance vocab vs. meaning.")
line()

# 4. TOKENS -> IDS. Models don't see strings; they see integer indices.
vocab = {tok: i for i, tok in enumerate(sorted(set(words)))}
ids = [vocab[w] for w in words]
print("4) TOKEN -> ID mapping (what the model actually receives):")
print("   vocab:", vocab)
print("   encoded sentence:", ids)
print("\nEvery prompt you send an LLM becomes a list of integers like this first.")
print("Fun fact: token count = what you're billed for, and what context limits count.")
