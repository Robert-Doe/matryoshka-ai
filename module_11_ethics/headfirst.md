# Module 11 — Head First: The Part Nobody Should Skip

> Every previous module made you more *capable*. This one makes you *responsible* —
> and, practically, more employable and more publishable. Ethics and safety aren't a
> lecture bolted onto AI; they come up in every serious AI role, every review board,
> and every thesis defense. For you, they're also the bridge where your security
> expertise meets AI head-on.

---

## Why a capable engineer needs this

Because models don't stay in notebooks. They approve loans, screen résumés, flag
"suspicious" behavior, moderate speech, and drive cars. When a model is wrong, a
real person bears it. And a model can be **highly accurate overall while doing
systematic harm to a subgroup** — a fact your aggregate metrics will happily hide.
This module teaches you to look where the harm actually lives.

There's also a self-interested reason: "did you check for bias / privacy / misuse?"
is now a standard question in AI job interviews, model reviews, grant panels, and
paper reviews. Being fluent here is a differentiator, not a formality.

---

## Big idea 1: Garbage in, *injustice* out

You learned "garbage in, garbage out" in Module 03. Here it gets teeth. A model
learns the patterns in its data — **including society's past mistakes.** If historical
loan decisions approved one group less for the same qualifications, a model trained
on those decisions learns to do the same, and now it's automated, scaled, and wearing
a veneer of mathematical objectivity.

`bias_audit.py` shows exactly this: a loan model with **93% overall accuracy** that
approves Group B far less often and falsely rejects them more, purely because the
training labels encoded a historical bias. The model isn't buggy. It's a faithful
mirror. The lesson: **an aggregate metric can conceal a discriminatory pattern, and
only a per-subgroup audit reveals it.**

And the naive fix — "just delete the sensitive attribute" — usually fails, because
other features act as **proxies** (zip code for race, first name for gender). Fairness
through unawareness is not fairness. The script lets you verify this yourself.

---

## Big idea 2: "Fair" is not one thing

Here's the part that surprises everyone. **There are multiple, precise, mutually
incompatible mathematical definitions of "fair,"** and you usually can't satisfy them
all at once. `fairness_metrics.py` computes three on the same predictions:

- **Demographic parity** — every group approved at the same rate.
- **Equal opportunity** — every group's *qualified* members approved at the same rate.
- **Predictive parity** — a "yes" means the same thing for every group.

When groups have different base rates, satisfying one of these *forces* you to violate
another. This isn't sloppy engineering — it's a **theorem** (Kleinberg et al.;
Chouldechova). So "is it fair?" has no purely technical answer. You must **choose which
definition matters for this decision and defend the choice.** That act of choosing and
justifying is the real deliverable of a fairness analysis — and exactly the kind of
reasoning a committee will press you on.

---

## Big idea 3: The safety dimensions (and where you've already met them)

Responsible AI clusters into a handful of recurring axes. Strikingly, you've already
touched almost all of them mechanically in this course:

| Axis | The worry | You saw it in |
|------|-----------|---------------|
| Bias / fairness | unequal harm across groups | this module |
| Privacy | leaking training data / PII | memorization (M04), RAG (M10) |
| Robustness | fails on adversarial / shifted input | adversarial examples (M09) |
| Transparency | can't explain a decision | interpretable models (M04) vs. opaque nets (M07) |
| Security | attackable / misusable | poisoning (M03), prompt injection (M10) |
| Accountability | who's responsible when it's wrong | governance |

`alignment_notes.md` is a fuller primer on the safety/alignment side (specification
gaming, RLHF, interpretability, evals). `red_team_checklist.md` turns all of it into a
practical checklist you can run on any model — including your own.

---

## Big idea 4: This is your bridge, not a detour

You are a security researcher. Almost everything in responsible AI is threat modeling
applied to models:

- **Adversarial ML** (evasion, poisoning, extraction, membership inference) is your
  attack-surface instinct applied to ML.
- **Prompt injection and agent security** (M10) are the confused-deputy and
  untrusted-input problems you already understand, in a new medium.
- **Red-teaming and evals** are security testing with a different target.

The `red_team_checklist.md` is deliberately written as a threat-modeling document —
because that's what a fairness/safety audit *is*. You're not learning a foreign
discipline; you're porting one you already own onto a new system.

---

## What you'll do

1. `bias_audit.py` — watch a 93%-accurate model hide a discriminatory pattern; reveal
   it with a per-group audit; test whether dropping the sensitive feature helps.
2. `fairness_metrics.py` — compute three fairness definitions and see them conflict.
3. Read `alignment_notes.md` (the safety map) and `red_team_checklist.md` (the tool).
4. `project.md` — **audit one of YOUR earlier models** (M04, M06, or M09) for bias,
   document the harm, choose and justify a fairness criterion, and propose a mitigation.

**The mindset:** capability without responsibility is a liability. The most senior
engineers are the ones who ask "who could this hurt, and how would I know?" before
they ship.

**Next:** `tutorial.html` → `project.md`.
