# Module 08 — Head First: How Machines Read (and How LLMs Work)

> This is the module that demystifies ChatGPT and Claude. By the end you'll have
> built the three ideas an LLM is made of — tokens, embeddings, and next-token
> prediction — and understood attention, the mechanism that ties them together.
> No hand-waving: you'll run each piece.

---

## The problem: computers do math, not words

A model can't "read" the word *phishing*. So NLP is fundamentally a translation
pipeline: **text → numbers → model → numbers → text.** Three stages turn language
into something a neural net can chew on:

```
   TEXT ──tokenize──▶ token IDs ──embed──▶ vectors ──▶ [ neural net ] ──▶ next token
```

Master these three and LLMs stop being magic.

---

## Stage 1: Tokenization — chop text into pieces

A model needs a fixed vocabulary of "tokens." Three strategies:

- **Words** — split on spaces. Simple, but the vocabulary is enormous and
  *phishing / phished / phisher* become three unrelated tokens. Unseen words break it.
- **Characters** — tiny vocabulary, but sequences get very long and the model must
  relearn spelling.
- **Subwords (BPE)** — the winner, used by GPT and Claude. It repeatedly merges the
  most frequent character pairs into subword units. `tokenize_demo.py` runs BPE live
  and watches it *discover* `phish` as a reusable chunk, so all the phish-words share
  it and the model generalizes.

Every prompt you send an LLM first becomes a list of integer token IDs. Two
practical consequences you'll care about: **token count is what you're billed for**,
and **context limits are measured in tokens**, not words.

---

## Stage 2: Embeddings — meaning as geometry

A token ID (say, 4173) carries no meaning. An **embedding** maps each token to a
vector of numbers, learned so that **words used in similar ways land near each
other in space.** This is the breakthrough idea of modern NLP:

> "You shall know a word by the company it keeps." — J.R. Firth

`embeddings_demo.py` builds real embeddings from scratch: it counts which words
co-occur, factorizes that matrix, and — without being told any meanings — discovers
that *attacker* sits near *hacker* and *cat* sits near *dog*. Meaning emerged as
**distance**. Then cosine similarity (straight from Module 02!) finds a word's
neighbors.

The famous party trick — `king − man + woman ≈ queen` — works because these
relationships become consistent *directions* in the vector space. Real embeddings
(word2vec, GloVe, and the input layer of every LLM) are this idea trained at scale.

> **Security angle:** embed log lines, commands, or URLs, and a novel attack that's
> *semantically* similar to a known one lands nearby — detection that generalizes
> past exact-string matching. This is a live area you could push on.

---

## Stage 3: Language modeling — predict the next token

Here's the whole job of an LLM, stated plainly: **given the tokens so far, predict
the next one.** That's it. Everything else is scale.

`tiny_bigram_lm.py` builds the smallest real language model: it counts
`P(next word | current word)` and then **generates** text by sampling — pick a
word, sample the next from its distribution, append, repeat. This
"predict-then-append" loop is called **autoregressive generation**, and it is
*exactly* how Claude writes this sentence: one token at a time, feeding its own
output back as input.

Your bigram model has one crippling limitation: it only sees the **last** word. Ask
it about anything earlier and it's blind. Fixing that limitation is the entire
reason transformers exist.

---

## The missing piece: attention

Real LLMs consider **all** previous tokens and *decide which ones matter* for the
current prediction. That mechanism is **attention**, the core of the Transformer
architecture.

The intuition: to understand a word, each word asks a **Query** ("what am I looking
for?"), every word offers a **Key** ("what do I have?"), and attention weight = how
well a Query matches a Key (a dot product — Module 02, again). Softmax turns those
scores into weights that sum to 1, and the word's new representation is a weighted
blend of every word's **Value**.

`attention_intuition.ipynb` computes this by hand on a 4-word sentence so you see
the weights: each word literally deciding how much to "look at" every other word.
Stack many attention layers + billions of parameters + trillions of training
tokens, and you have an LLM.

> **Security angle — prompt injection:** attention operates over the *entire*
> context, including text a user or a document injects. The model attends to
> malicious hidden instructions the same way it attends to trusted ones — that's the
> mechanistic root of prompt injection, which you'll defend against in Module 10.

---

## Putting it together: what an LLM actually is

```
   your prompt
       │ tokenize        (Stage 1)
       ▼
   token IDs
       │ embed           (Stage 2)
       ▼
   vectors ──▶ many Transformer layers (attention + feed-forward)
       │ predict a probability over the whole vocabulary
       ▼
   sample the next token ──▶ append ──▶ repeat   (Stage 3, autoregressive)
```

You have now built or hand-computed every box in that diagram. That's the demystification.

---

## What you'll do

1. `tokenize_demo.py` — word/char/subword tokenization; watch BPE find `phish`.
2. `embeddings_demo.py` — build embeddings from scratch; see meaning become geometry.
3. `tiny_bigram_lm.py` — a real next-token model that generates text.
4. `attention_intuition.ipynb` — compute attention by hand; understand transformers.
5. `project.md` — train a next-word model on a text you choose, then articulate
   exactly where it falls short of a real LLM (tokenization? context? attention?).

**Next:** `tutorial.html` → `project.md`.
