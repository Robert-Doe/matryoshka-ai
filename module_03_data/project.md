# Module 03 — Project: Clean a Phishing Dataset Yourself

**Goal:** You've watched the login pipeline. Now do it solo on a *different* dirty
dataset — `messy_data_project.csv`, a set of emails labeled `phish`/`legit` — and
justify every cleaning decision. Justification is the graded skill.

**Time:** ~60 min. **Deliverable:** `clean_project.py` that produces
`clean_project.csv`, plus a short `cleaning_log.md` explaining your choices.

---

## The dataset

`messy_data_project.csv` — one row per email, columns:

| Column | Meaning |
|--------|---------|
| `email_id` | unique id |
| `sender_domain` | the From domain (note the lookalikes: `paypa1-secure.com`, `micros0ft-support.com`) |
| `num_links` | number of links in the body |
| `has_attachment` | yes/no (inconsistent casing) |
| `subject_len` | subject length in characters |
| `urgency_score` | 0–10 "act now!" language score |
| `label` | `phish` or `legit` (the target) |

It contains the same five problem classes as the lesson — plus a couple of new
twists. Find them all.

---

## Your tasks

**1. Explore.** Write code (or adapt `load_explore.py`) to report: shape, dtypes,
missing counts, duplicates, unique values of `has_attachment` and `label`, and
min/max of the numeric columns. List every problem you find.

**2. Clean.** Fix each problem, printing what you change. At minimum:
- Coerce `urgency_score` and `subject_len` to numbers (a `N/A` is hiding in one).
- Standardize `has_attachment` (`no`/`No` → `no`) and `label` (`LEGIT` → `legit`).
- Drop exact duplicate rows.
- Handle impossible values: negative `subject_len` (-5, -3) can't exist.
- Impute remaining missing numerics with the median; drop rows missing the `label`.
- Decide what to do with `subject_len == 999`. Is it noise or signal? Justify.

**3. Reflect (`cleaning_log.md`).** For each decision, one line: *what* you did and
*why*. Especially: how did you handle `subject_len == 999`, and why?

---

## Traps to catch (don't peek until you've tried)

<details><summary><strong>Reveal the intended issues</strong></summary>

- **Type:** `urgency_score` has an `N/A` (row 2019) → loads as text.
- **Missing:** blanks in `subject_len` (2004, 2027), `urgency_score` (2007), `label` (2016).
- **Duplicate:** email 2002 appears twice.
- **Categories:** `no`/`No`, `yes`/`YES`, `legit`/`LEGIT`.
- **Impossible:** `subject_len` of -5 and -3.
- **Outlier judgment:** `subject_len == 999` (row 2017). Unlike the login bytes,
  a 999-char subject is almost certainly a data error, not a real signal — most
  clients truncate subjects. Defensible to cap or drop. The point is that you
  reasoned about it rather than blanket-removing outliers.
- **Bonus insight (not a cleaning step):** the *lookalike domains* (`paypa1-`,
  `micros0ft-`, `bank0famerica-`) are the actual phishing signal. You could
  engineer a feature like "domain contains a digit substituting for a letter."
  Note it in your log — that's feature engineering, previewing Module 04.

</details>

---

## Mastery checklist
- [ ] You found all six problem types (not just the five from the lesson).
- [ ] Your cleaning code prints an audit trail of every change.
- [ ] `cleaning_log.md` justifies the `999` decision explicitly.
- [ ] You noticed the lookalike-domain signal and wrote it down.
- [ ] Final `clean_project.csv` has consistent types, no dupes, no impossible values,
      and a `label` column with exactly two clean classes.

## Stretch (optional)
Add an engineered feature `homoglyph_domain` = 1 if `sender_domain` contains a digit
where a letter belongs (e.g. `0` for `o`, `1` for `l`). Report how well it separates
phish from legit. You've just built a real detection feature — the kind of artifact
that belongs in a security-ML paper.

**Next module:** `../module_04_supervised/headfirst.md` — teach a machine to predict.
