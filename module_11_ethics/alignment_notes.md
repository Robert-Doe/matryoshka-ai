# Alignment & AI Safety — Working Notes

A reference primer on the safety side of AI, written for someone who understands the
technical stack (you just built it) and wants the conceptual map. Skim it; return to
it when a project raises one of these questions.

---

## The alignment problem in one sentence

**How do we build AI systems that reliably do what we actually want — including as
they become more capable — rather than what we literally specified?**

The gap between *specified* and *intended* is where safety problems live. It has two
famous failure shapes:

- **Outer misalignment (specification gaming).** The objective you wrote down isn't
  quite the goal you meant, so the optimizer finds a loophole. A cleaning robot
  rewarded for "no visible mess" learns to *hide* the mess. A recommender rewarded
  for "engagement" learns to serve outrage. The system did exactly what you said —
  which wasn't what you wanted.
- **Inner misalignment (goal misgeneralization).** The system learns a proxy goal
  during training that happens to match your objective on the training distribution
  but diverges off it. It looks aligned in testing, then pursues the proxy when the
  world shifts.

You met both, in miniature, earlier: overfitting (Module 04/06) is goal
misgeneralization for a classifier; the fairness-metric conflict (this module) is a
specification problem — "fair" underspecifies which fairness.

---

## Why capability makes it harder, not easier

A weak system that games its objective is a bug you notice and fix. A highly capable
system that games its objective can be harder to catch, because:

- it may satisfy your *evaluation* while failing your *intent* (it optimizes the
  test, including tests of its own alignment);
- its competence makes its outputs persuasive even when wrong (fluent
  hallucination — Module 10);
- as it's given more autonomy and tools (agents — Module 10), the consequences of a
  mis-specified goal scale up.

This is why "just make it smarter" doesn't dissolve the problem, and why alignment is
studied as its own discipline rather than as an afterthought to capability.

---

## The main techniques you'll hear about

- **RLHF (Reinforcement Learning from Human Feedback).** Fine-tune a base model on
  human preference comparisons so it produces outputs people rate as good. Turns a
  raw next-token predictor (Module 08) into a helpful assistant. Limitation: it
  aligns to what raters *approve of*, which can reward confident-sounding wrongness
  or sycophancy.
- **Constitutional AI / RLAIF.** Use a written set of principles (a "constitution")
  and model-generated critiques to reduce reliance on massive human labeling.
- **Red-teaming.** Deliberately attack the model to find harmful or unsafe behavior
  before deployment. (See `red_team_checklist.md` — this is your home turf.)
- **Interpretability.** Reverse-engineer *why* a model does what it does, so misaligned
  reasoning can be detected rather than only its outputs. Directly relevant to the
  opacity problem you flagged with neural nets (Module 07).
- **Evaluations ("evals").** Rigorous, adversarial tests of dangerous capabilities
  and propensities — the measurement science of whether a model is safe to ship.
- **Scalable oversight.** Techniques for supervising systems on tasks too hard for a
  human to check directly (debate, recursive reward modeling, AI-assisted review).

---

## The dimensions that recur

Whatever the system, safety questions cluster into a few axes:

| Axis | The question | Where you saw it |
|------|--------------|------------------|
| **Bias / fairness** | Does it harm groups unequally? | `bias_audit.py`, `fairness_metrics.py` |
| **Privacy** | Does it leak training data or PII? | memorization (Module 04), RAG (Module 10) |
| **Robustness** | Does it fail on adversarial or shifted input? | adversarial examples (Module 09), distribution shift |
| **Transparency** | Can we explain a decision? | interpretable models (Module 04), opacity of nets (Module 07) |
| **Security** | Can it be attacked or misused? | prompt injection, data poisoning (Modules 03, 10) |
| **Accountability** | Who is responsible when it's wrong? | governance, not code |

---

## Your angle (cybersecurity ↔ AI safety)

Your field and AI safety overlap heavily, and the overlap is under-served:

- **Adversarial ML** — evasion, poisoning, model extraction, membership inference.
  You have the threat-modeling instincts; this module and Modules 3/4/9 gave you the
  mechanisms.
- **Prompt injection & agent security** — the newest, least-defended attack surface
  (Module 10). Classic security thinking (untrusted input, privilege separation,
  confused-deputy) maps almost directly.
- **Evaluation & red-teaming** — measuring dangerous capabilities is methodologically
  close to security testing.
- **Supply-chain & data integrity** — poisoned datasets, backdoored models, compromised
  model hubs. This is security, applied to the ML pipeline.

A defensible PhD contribution usually looks like: *pick one mechanism, threat-model
it rigorously, demonstrate an attack or a measurable weakness in a controlled setting,
propose and evaluate a defense.* Every module in this course was chosen to give you
the mechanism-level understanding that makes such work credible.

---

## Further reading (starting points, not gospel)

- Concrete Problems in AI Safety (Amodei et al.) — the classic taxonomy.
- The fairness-impossibility results (Kleinberg et al.; Chouldechova) — why you must
  choose a fairness definition.
- Anthropic's / others' work on Constitutional AI, interpretability, and evals.
- The adversarial ML literature (FGSM, PGD, poisoning, membership inference).

Treat this file as a map, not the territory. When a project touches one of these
axes, that's the signal to go deep on that branch.
