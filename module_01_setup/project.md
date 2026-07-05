# Module 01 — Project: "Is it AI?"

**Goal:** Turn the AI ⊃ ML ⊃ DL ⊃ GenAI hierarchy from words you read into an
instinct you *have*. You'll classify 12 real systems and defend each call.

**Time:** ~30 minutes. **Deliverable:** fill in the table below (copy it into a new
file `my_answers.md`, or just edit this one).

---

## The task

For each system, decide the **most specific** box it belongs in:

- **RULES** — plain AI, a human wrote the logic; it does NOT learn from data.
- **ML** — machine learning; learns patterns from data, but not deep neural nets.
- **DL** — deep learning; uses many-layered neural networks.
- **GENAI** — generative AI / LLM; a deep-learning model that *creates* content.

Then write **one sentence** justifying it. The justification matters more than the
label — that's where the learning happens.

> Rule of thumb: ask *"Does it learn from data?"* (No → RULES). If yes, *"Neural
> network with many layers?"* (No → ML). If yes, *"Does it generate new content?"*
> (Yes → GENAI, otherwise → DL).

---

## The 12 systems

| # | System | Your box | One-sentence justification |
|---|--------|:--------:|----------------------------|
| 1 | A home thermostat that turns on heat below 68°F | | |
| 2 | Gmail's spam filter | | |
| 3 | Claude / ChatGPT writing an email | | |
| 4 | A Roomba bouncing off walls with bump sensors | | |
| 5 | Netflix's "because you watched..." recommendations | | |
| 6 | Face unlock on a phone | | |
| 7 | A chess engine from 1997 (hand-coded opening book + search) | | |
| 8 | Spotify generating a brand-new song in an artist's style | | |
| 9 | A bank's credit-score model (logistic regression on your history) | | |
| 10 | Self-driving car identifying pedestrians from camera feeds | | |
| 11 | A calculator app | | |
| 12 | Autocomplete suggesting the next word as you type on your phone | | |

---

## After you fill it in — check yourself

Don't peek until you've committed to all 12. Then compare:

<details>
<summary><strong>Click to reveal the discussion (try first!)</strong></summary>

1. **RULES** — Fixed threshold, no learning. Classic "AI" in the loosest sense; a human wrote the 68°F rule.
2. **ML** — Learns spam patterns from labeled emails. Classically done with non-deep models (e.g., Naive Bayes), though modern versions creep into DL.
3. **GENAI** — An LLM generating new text. The innermost doll.
4. **RULES** — Reactive logic ("bump → turn"). No learning from data. (Fancier robot vacuums that map rooms edge toward ML — note that nuance.)
5. **ML** (often **DL** now) — Learns your taste from behavior data. Recommenders were classic ML; big platforms now use deep models. Either answer is defensible *if you justify it* — that's the skill.
6. **DL** — Face recognition is powered by deep convolutional networks. It classifies, it doesn't generate, so DL not GENAI.
7. **RULES** — Hand-coded search + human-written heuristics. Strong, but it doesn't *learn*. (Contrast with AlphaZero, which would be DL.)
8. **GENAI** — Creating new audio content = generative.
9. **ML** — Logistic regression is machine learning but not a deep neural net.
10. **DL** — Pedestrian detection from images is deep learning (CNNs). Classifies/detects, doesn't generate → DL.
11. **Not AI at all** — Deterministic arithmetic. The trick question. If you put it in a box, ask yourself what it *learned*. (Nothing.) Good AI engineers know when something *isn't* AI.
12. **DL / GENAI (blurry)** — Old autocomplete was ML/statistics; modern phone keyboards use small neural language models that *predict/generate* the next token, nudging toward GENAI. Defend whichever you pick.

</details>

---

## What "mastery" looks like here

You're not graded on matching my labels. You've mastered this module when:

- You instinctively ask **"does it learn from data?"** as your first question.
- You can explain **why #11 (calculator) isn't AI** and **why #7 (old chess engine)
  is 'AI' but not 'ML'.**
- You noticed that **#5, #10, and #12 are genuinely blurry** and your justification —
  not the label — is what makes your answer right or wrong.

That last point is the real lesson: **the boxes have fuzzy edges, and a pro reasons
about the fuzz instead of pretending it isn't there.**

---

## Stretch (optional)

Add a 13th row: a system from *your own life or work*. Classify it, justify it, and
note what data it would need to learn from. Bring this instinct into Module 02.

**Next module:** `../module_02_math/headfirst.md` — the math that makes learning
possible (just enough, not a degree).
