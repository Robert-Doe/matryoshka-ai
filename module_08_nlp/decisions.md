# Module 08 — DECISIONS

## Decision 1 — Build tokens → embeddings → next-token, in that order
The module mirrors the actual LLM pipeline stage by stage.
- **Why:** LLMs feel like magic because people never see the stages. Walking the
  real pipeline (and running each stage) replaces mystique with mechanism. The order
  is the data-flow order, so each script's output is the next script's input conceptually.

## Decision 2 — Everything self-contained, no model downloads
Embeddings are built from a local corpus via SVD; the LM is a hand-counted bigram.
- **Why:** Downloading GloVe vectors or a HuggingFace model would work but hide the
  idea behind an API call. Building embeddings from co-occurrence makes "meaning as
  geometry" something you *derived*, not imported. Also: it runs offline, instantly.
- **Trade-off:** Toy-scale results. We explicitly connect each toy to its real
  counterpart (word2vec, transformers) so the scale gap is understood, not hidden.

## Decision 3 — Show BPE actually merging, not just described
`tokenize_demo.py` runs the merge loop and prints each discovered subword.
- **Why:** "Subword tokenization" is abstract; watching the algorithm *find* `phish`
  makes it click, and explains why related words share structure (generalization).

## Decision 4 — A bigram LM to make "next-token prediction" literal
- **Why:** The most important sentence about LLMs — "they predict the next token" —
  is just words until you build one and watch it generate. The bigram's obvious
  limitation (sees only the last word) then MOTIVATES attention, so the next piece
  feels necessary rather than arbitrary.

## Decision 5 — Attention computed by hand with Q/K/V
The notebook does scaled dot-product attention on 4 words with printed weights.
- **Why:** Attention is the concept people most want and least understand. Seeing the
  actual weight each word assigns to each other word ("cat attends 0.4 to sat")
  turns a famous diagram into arithmetic you followed.

## Decision 6 — Thread security through: detection embeddings + prompt injection
- **Why:** Two high-value hooks for this researcher: (a) semantic embeddings of logs/
  commands generalize detection beyond string matching; (b) attention over untrusted
  context is the root cause of prompt injection. Both are real research directions and
  both fall naturally out of the mechanisms taught here.

## What we left out
- **Positional encodings, multi-head attention, layer norm, residual connections** —
  the full transformer's plumbing. Named where relevant; drilling them needs the
  single-head intuition first, which is what we build.
- **Fine-tuning / RLHF** — how raw next-token models become helpful assistants;
  touched conceptually in Module 10 where the API makes it concrete.
- **Modern tokenizer libraries (tiktoken, SentencePiece)** — the production tools;
  the hand-rolled BPE teaches what they do.
