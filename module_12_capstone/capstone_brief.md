# Capstone Brief

Your final project. Pick ONE track, build it end to end, and deliver it against the
`evaluation_rubric.md`. Budget ~8-15 hours. The goal is a complete, honest, well-
explained project — not a state-of-the-art model.

---

## Deliverables (all tracks)

1. **Working code** in a copy of `project_template/`, runnable from a clean checkout.
2. **`writeup.md`** — filled-in `writeup_template.md`: problem, data, method, results,
   ethics, limitations, next steps.
3. **A results artifact** — at least one plot or table that tells the story.
4. **An ethics/limitations section** — you ran `../module_11_ethics/red_team_checklist.md`
   on your own model and reported what you found.

---

## Track A — Classic ML Predictor

**Build:** a supervised model that predicts something useful from tabular data.

- **Suggested (security-flavored):** phishing-URL / spam / intrusion / fraud /
  anomaly classifier. Public datasets abound (UCI, Kaggle), or synthesize realistic
  data as we did in Modules 3 & 11.
- **Must include:** a train/test split (no leakage), a **baseline** (majority class /
  mean), the **right metric** for your class balance (precision/recall/F1, not just
  accuracy — Module 6), cross-validation with mean ± std, and a **bias audit** across
  some attribute (Module 11).
- **Great version:** feature engineering that reflects domain knowledge (e.g. the
  homoglyph-domain feature from Module 3), plus a precision-recall-vs-threshold
  analysis showing how you'd tune the operating point.

## Track B — Computer Vision App

**Build:** a CNN image classifier plus interpretation and robustness analysis.

- **Suggested:** cats-vs-dogs, Fashion-MNIST, or a small custom set. (Needs
  `pip install torch`; keep it CPU-sized.)
- **Must include:** a trained CNN beating a baseline, a **confusion matrix** showing
  where it errs, and a **visualization of learned filters** (Module 9).
- **Great version (recommended for you):** implement an **FGSM adversarial example**
  that fools your model, then a **defense** (adversarial training or input
  preprocessing) and measure how much it reduces attack success — the attack →
  defense → measure loop of an adversarial-ML paper.

## Track C — LLM-Powered Tool

**Build:** a genuinely useful RAG app or tool-using agent.

- **Suggested:** "chat with your research papers/notes," a log-triage assistant, or a
  security-Q&A tool grounded in a docs corpus. (Needs `pip install anthropic`;
  `MODEL=claude-haiku-4-5` keeps it cheap.)
- **Must include:** retrieval + **grounded** generation that refuses when the answer
  isn't in the corpus (Module 10), basic citation of sources, and a **prompt-injection
  test** with a documented defense.
- **Great version:** a small **evaluation set** of questions with expected answers, so
  you can measure answer quality objectively rather than by vibes — and a written
  analysis of the tool's failure modes.

---

## Rules that make it real

- **Baseline or it doesn't count.** Every result is reported against a dumb baseline.
- **Judge on unseen data only.** Test set / cross-validation, never train accuracy.
- **Honesty over heroics.** Report where it fails. A limitation section is required.
- **Reproducible.** Fixed random seeds, pinned requirements, a README that says how to run.
- **Ethics is not optional.** Every track has a required responsible-AI component.

---

## Suggested timeline

| Phase | Time | Output |
|-------|------|--------|
| Frame + get data | ~2 hrs | problem statement, clean dataset, EDA |
| Baseline + first model | ~2 hrs | a number that beats the baseline |
| Iterate + evaluate | ~3-4 hrs | proper metrics, CV, the "great version" extra |
| Ethics / red-team | ~1-2 hrs | bias audit or injection test, findings |
| Write up | ~2-3 hrs | finished `writeup.md`, plots, README |

Start by copying `project_template/` and opening `writeup_template.md`. Fill the
write-up as you work — it keeps you honest and turns a pile of code into a project.
