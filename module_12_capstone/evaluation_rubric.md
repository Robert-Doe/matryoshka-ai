# Capstone Evaluation Rubric

Read this **before** you start — build toward it. Score yourself honestly (or hand it
to a peer/mentor). 100 points. The weighting is deliberate: framing, evaluation, and
communication are worth more than model performance, because that's what separates a
professional from a Kaggle-leaderboard chaser.

---

## 1. Problem framing & scope — 15 pts
- [ ] (5) The problem is clearly stated: what's predicted/built, and why it matters.
- [ ] (5) "Success" is defined *before* modeling (what metric, what bar).
- [ ] (5) Scope is realistic and the stakes/harms of errors are acknowledged.

## 2. Data handling — 15 pts
- [ ] (5) Data is cleaned and explored; problems (missing, outliers, imbalance) are found and handled.
- [ ] (5) A proper train/test split (or CV); **no data leakage** (dedup, no answer-derived features).
- [ ] (5) Class balance / distribution is reported and its implications noted.

## 3. Modeling — 15 pts
- [ ] (5) An appropriate model is chosen and justified (simplest thing that could work).
- [ ] (5) It **beats a stated baseline** (majority class / mean / random).
- [ ] (5) Reasonable iteration: at least one improvement attempt, with its effect measured.

## 4. Evaluation — 25 pts  ← the heaviest section, on purpose
- [ ] (7) The **right metric** for the problem (precision/recall/F1 on imbalanced data, not raw accuracy).
- [ ] (6) Results reported with a **baseline comparison** and, where relevant, **mean ± std** (CV).
- [ ] (6) **Failure analysis:** where and why the model errs (confusion matrix, error cases).
- [ ] (6) No self-deception: no train-accuracy claims, no cherry-picked split, no leakage.

## 5. Ethics & responsibility — 15 pts
- [ ] (5) A relevant responsible-AI component was done (bias audit / prompt-injection test / robustness).
- [ ] (5) A specific harm or risk is identified and discussed with its trade-offs.
- [ ] (5) An honest **limitations** section: what wasn't tested, and why.

## 6. Communication & reproducibility — 15 pts
- [ ] (5) `writeup.md` is clear enough that a non-author understands the project.
- [ ] (5) At least one figure/table communicates a key result effectively.
- [ ] (5) The code runs from a clean checkout (README, pinned deps, fixed seeds).

---

## Grade bands

| Score | Meaning |
|-------|---------|
| 90-100 | Portfolio-ready. Rigorous, honest, clearly communicated. Show this in interviews. |
| 75-89  | Solid mastery. Minor gaps in evaluation depth or write-up polish. |
| 60-74  | Works, but evaluation or ethics or communication is thin. Revisit the weak section. |
| < 60   | Likely a "cool model, weak method" project. Re-read Modules 6 and 11 and strengthen the rigor. |

---

## The rubric's hidden message

Notice that **Evaluation (25) + Ethics (15) + Communication (15) = 55 points** — more
than half — while raw Modeling is 15. That's not an accident. Anyone can call
`.fit()`. The scarce, valuable skills are: measuring honestly, thinking about harm,
and explaining clearly. Optimize for those and you'll be a better AI practitioner than
most people with fancier models. That is the entire thesis of this course.
