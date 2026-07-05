# Module 01 — Head First: Thinking Like an AI Engineer

> Read this in one sitting. No code yet. Just ideas that will make everything
> later feel obvious instead of scary.

---

## The one picture that explains all of AI

Imagine you're teaching a kid to recognize a dog. You don't hand them a rulebook
("four legs, fur, tail, barks"). You point at dogs. "Dog." "Dog." "That's a dog
too." After enough examples, something clicks — they can spot a dog they've never
seen before, even a weird-looking one.

**That's it. That's machine learning.** Show a system enough examples, and it
figures out the pattern *by itself*. It doesn't memorize the examples — it learns
the *idea* behind them.

Now hold that thought, because there's a hierarchy you need to burn into memory.

---

## The Russian dolls of AI

People throw around "AI," "machine learning," "deep learning," and "ChatGPT" as if
they're the same thing. They're not — they nest inside each other:

```
┌─────────────────────────────────────────────────────────┐
│ ARTIFICIAL INTELLIGENCE                                   │
│  "Any trick that makes a machine seem smart."             │
│  (Even a chess program with hand-written rules counts.)   │
│                                                           │
│   ┌─────────────────────────────────────────────────┐    │
│   │ MACHINE LEARNING                                  │    │
│   │  "Learn the rules from DATA instead of being      │    │
│   │   told them." (The dog example above.)            │    │
│   │                                                   │    │
│   │   ┌───────────────────────────────────────┐       │    │
│   │   │ DEEP LEARNING                          │       │    │
│   │   │  "Machine learning using brain-ish     │       │    │
│   │   │   networks with many layers."          │       │    │
│   │   │                                        │       │    │
│   │   │   ┌───────────────────────────┐         │       │    │
│   │   │   │ GENERATIVE AI / LLMs       │         │       │    │
│   │   │   │  "Deep learning that       │         │       │    │
│   │   │   │   CREATES — text, images,  │         │       │    │
│   │   │   │   code. Claude lives here."│         │       │    │
│   │   │   └───────────────────────────┘         │       │    │
│   │   └───────────────────────────────────────┘       │    │
│   └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

Say it out loud once: **"AI contains ML, ML contains deep learning, deep learning
contains the generative stuff."** If you remember only one thing this week, this
is it. Half of the confusion in the field vanishes when you know which doll
someone is talking about.

---

## The loop that never changes

Here's the secret that makes the rest of the course easy. Every learning system —
from the 40-line toy you're about to run, to the model that wrote this sentence —
does the **same four-step loop**:

```
   ┌──────────────────────────────────────────────────┐
   │                                                  │
   │   1. DATA         "Here are examples."           │
   │        │                                         │
   │        ▼                                         │
   │   2. MODEL        "Here's my current guess       │
   │        │           at the pattern."              │
   │        ▼                                         │
   │   3. PREDICTION   "Given this input, I say..."   │
   │        │                                         │
   │        ▼                                         │
   │   4. FEEDBACK     "How wrong was I? Adjust."     │
   │        │                                         │
   └────────┘  ← go back to 2 with a slightly         │
                 better guess, thousands of times
```

A spam filter does this. A self-driving car does this. An LLM does this. The only
differences are **how big the model is** and **what the data looks like**. Scale,
not concept.

In a few minutes you'll run `hello_ai.py`, which does exactly this loop in plain
Python to learn that `y = 2 * x` — *without being told the "2."* Watch its guess
crawl from `0.44` toward `2.0`. That crawl is learning. You are watching a machine
learn. It genuinely doesn't get more mystical than that.

---

## "So where does the intelligence come from?"

Not from clever rules a human wrote. It comes from **the data + a way to measure
being wrong + the freedom to adjust.** Give a system those three things and a lot
of repetitions, and useful behavior *emerges*. Nobody hand-codes "what a dog looks
like" anymore. We hand it a million dog photos and a scorecard.

This is why the whole industry is obsessed with data. A mediocre model on great
data beats a great model on garbage data, almost every time. You'll feel this
personally in Module 03.

---

## What you'll actually do in this module

1. **Get your environment working** — run `setup_check.py`. It tells you exactly
   what's missing and how to fix it. Green means go.
2. **Watch a machine learn** — run `hello_ai.py`. Read the numbers as they change.
   Then open the file and read the comments; it's only ~40 lines.
3. **Do the project** — `project.md` ("Is it AI?"). You'll sort 12 real-world
   systems into the right Russian doll and *defend* each choice. This is how the
   taxonomy stops being words and becomes instinct.

---

## The mindset shift (the real point of this module)

Beginners ask: *"What rules should I write to solve this?"*

AI engineers ask: *"What examples could a system learn this from, and how would I
know if it learned the right thing?"*

That second question is the entire job. Everything else — the math in Module 02,
the models in Module 04, the neural nets in Module 07 — is just machinery for
answering it well.

Now go run `setup_check.py`. Then open `tutorial.html` in your browser for the
full walkthrough with worked examples.

**Next:** `tutorial.html` → then `project.md`.
