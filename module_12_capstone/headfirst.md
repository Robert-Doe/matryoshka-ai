# Module 12 — Head First: Ship Something Real

> You've built machine learning from scratch, trained neural nets, worked with LLMs,
> and learned to audit for harm. The capstone is where you prove it — not with a quiz,
> but with a complete, end-to-end project you could put in front of anyone. This is
> your portfolio piece and your rehearsal for doing AI work in your research.

---

## Why a capstone, and why it matters more than any exam

Knowledge you can *recall* is worth far less than knowledge you can *apply end to
end*. Every earlier module taught one piece in isolation. Real AI work is the whole
pipeline, with all its messy joins: framing a vague problem, wrangling real data,
choosing a model, evaluating honestly, checking for harm, and — crucially —
**explaining what you did so someone else believes it.** That last skill is the
difference between a script and a contribution.

For you specifically, this is a dry run for the applied-AI portions of your
dissertation: pose a question, build the thing, measure it without fooling yourself,
address the ethics, and write it up defensibly.

---

## The end-to-end pipeline (everything you learned, in order)

```
   1. FRAME      What's the question? What would "success" even mean?      (M01)
   2. DATA       Get it, clean it, explore it, split it. Guard leakage.    (M03, M04)
   3. MODEL      Pick the simplest thing that could work; train it.        (M04, M05, M07)
   4. EVALUATE   Right metric, baseline, cross-validation, honest numbers. (M06)
   5. ETHICS     Who could this harm? Audit for bias. Red-team it.         (M11)
   6. WRITE UP   Explain the problem, method, results, limits — clearly.   (all)
```

A capstone that nails steps 1, 4, and 6 beats one with a fancier model and sloppy
framing or evaluation every time. **Rigor and clarity are the deliverable**, not
leaderboard accuracy.

---

## Pick a track (choose ONE)

The `capstone_brief.md` details each; here's the shape:

- **Track A — Classic ML predictor.** Frame a prediction problem, engineer features,
  train and tune a model, evaluate properly, audit for bias. Best if you want to
  cement Modules 3-6 and 11. (Security flavor: a phishing/intrusion/anomaly classifier
  on a real or realistic dataset.)
- **Track B — Computer vision app.** Train a CNN on an image task, visualize what it
  learned, and (strongly encouraged for you) demonstrate an adversarial attack and a
  defense. Best if Module 9 excited you.
- **Track C — LLM-powered tool.** Build a RAG app or an agent that does something
  genuinely useful, with grounding and a prompt-injection defense. Best if Module 10
  is closest to your research and you want a tool you'll actually use.

All three tracks require the same *rigor*: baseline, honest evaluation, ethics section,
clear write-up. The track only changes the *subject*.

---

## What "done" looks like

Not "the model runs." Done means a reviewer can:

1. Read your `writeup.md` and understand **what problem you solved and why**.
2. Run your code and **reproduce your results**.
3. See an **honest evaluation** — the right metric, a baseline, and where the model
   fails, not just where it wins.
4. Find an **ethics/limitations section** that takes harm seriously.
5. Come away knowing **what you'd do next**.

The `evaluation_rubric.md` spells out exactly how each of these is judged — read it
*before* you start, and build toward it. The `project_template/` gives you a clean
folder structure so you're not inventing scaffolding. The `writeup_template.md` gives
you the report skeleton so you're not staring at a blank page.

---

## The one trap to avoid

**Don't spend 90% of your time chasing +2% accuracy and 10% on everything else.** The
common beginner capstone is a heroic model with no baseline, an accuracy metric on
imbalanced data (Module 6 warned you), no bias check, and a three-line README. It
looks impressive and convinces no one. The senior move is the reverse: a *simple*
model, a *clear* baseline, an *honest* evaluation, a *real* ethics section, and a
write-up someone can follow. Do that and you've demonstrated mastery of the whole
discipline — which is the entire point.

---

## How to work

1. Read `capstone_brief.md` and pick a track.
2. Read `evaluation_rubric.md` so you know the target.
3. Copy `project_template/` to a new folder and build there.
4. Fill in `writeup_template.md` **as you go**, not at the end — it keeps you honest
   about what you actually did.
5. Before you call it done, run your own model through `red_team_checklist.md` from
   Module 11.

There's no `project.md` here — **this whole module is the project.** Everything you've
learned converges on it. Go build something you're proud of.

**Next:** `tutorial.html` for the step-by-step, then `capstone_brief.md`.
