# Module 01 — DECISIONS

Why this module is built the way it is. Read this if you want to understand the
*teaching* choices, not just the content. (Every module ships one of these so the
course's reasoning is transparent — and so you learn to think about trade-offs,
which is itself an AI-engineering skill.)

---

## Decision 1 — Environment check is a *diagnostic*, not an installer

`setup_check.py` deliberately **never installs anything**. It only inspects and
reports.

- **Why:** A script that silently installs packages is a script you don't learn
  from and can't trust. Making the tool *diagnose and instruct* ("here's what's
  missing, here's the exact command") keeps you in control and teaches you what
  the environment actually needs.
- **Trade-off:** One extra manual step (you run the `pip install` yourself). Worth
  it — you'll be debugging environments for the rest of your career; start now.

## Decision 2 — `hello_ai.py` uses ZERO libraries

The first learning program is pure Python — no NumPy, no scikit-learn.

- **Why:** The single most damaging beginner belief is that ML is "magic inside a
  library you call." By writing the loop by hand — prediction, error, gradient,
  adjust — you see there is no magic, just arithmetic repeated. Everything later
  (NumPy in M02, scikit-learn in M04, PyTorch in M07) is *speed and convenience*
  layered on top of this exact idea.
- **Trade-off:** The hand-rolled gradient descent is slower and less general than
  a library. That's fine; it's a teaching artifact, not production code.

## Decision 3 — We teach the "Russian dolls" before any technique

Before regression, before neural nets, we drill the AI ⊃ ML ⊃ DL ⊃ GenAI hierarchy.

- **Why:** Most beginner confusion is *category confusion* — mixing up "AI,"
  "machine learning," and "ChatGPT." Fix the taxonomy first and every later topic
  has a shelf to sit on. The project (`is_it_ai`) exists solely to make this
  automatic.
- **Trade-off:** It feels like "just vocabulary" early on. It pays off every single
  module afterward.

## Decision 4 — The four-step loop is the course's spine

We frame *data → model → prediction → feedback* as the thing that never changes.

- **Why:** A unifying mental model beats a pile of disconnected techniques.
  Supervised learning, neural nets, and even LLM training are all this loop at
  different scales. Returning to the same diagram in every module compounds
  understanding instead of resetting it.
- **Trade-off:** It's a simplification — reinforcement learning and some
  unsupervised methods bend the loop. We'll note the exceptions when we reach them
  rather than muddy the first exposure.

## Decision 5 — Project over quiz

Module 01 ends with a *do-it* project, not a multiple-choice quiz.

- **Why:** You remember what you produce, not what you recognize. Sorting 12 real
  systems and *justifying* each forces active recall and surfaces your own
  misconceptions (everyone mis-sorts at least one — that's the point).
- **Trade-off:** No auto-grading; you self-check against the discussion in
  `project.md`. Judgment is the skill, and judgment can't be auto-graded.

## Decision 6 — Colors degrade gracefully

`setup_check.py` disables ANSI colors when output isn't a real terminal and enables
virtual-terminal mode on Windows.

- **Why:** Beginners run scripts in all sorts of places (piped to a file, in an
  IDE console, in an old cmd.exe). Garbled `[92m` escape codes look like an error
  and erode confidence on step one. Robust output is a courtesy that matters most
  at the very start.

---

## What we deliberately LEFT OUT of Module 01

- **No GPUs / CUDA.** Everything runs on a plain CPU until Module 07, and even then
  we keep models tiny. Don't buy hardware to learn.
- **No conda.** We use the built-in `venv` to avoid a second package manager's
  quirks. If you already love conda, it works fine — just skip our venv step.
- **No cloud accounts.** The only external service in the whole course is the LLM
  API in Module 10, and that module explains keys/costs when you get there.
- **No heavy theory.** Zero calculus notation in Module 01 on purpose. The *idea*
  of "nudge toward less error" is enough; the formal gradient math arrives in M02
  when you have intuition to hang it on.
