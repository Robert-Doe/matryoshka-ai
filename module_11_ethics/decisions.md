# Module 11 — DECISIONS

## Decision 1 — Make bias measurable, not just discussable
`bias_audit.py` produces hard numbers (per-group accuracy, approval, false-reject).
- **Why:** Ethics modules fail when they're all prose. A runnable audit that shows a
  93%-accurate model discriminating turns an abstract worry into a concrete,
  reproducible finding — and teaches the actual skill (subgroup evaluation) rather
  than just the sentiment.

## Decision 2 — Bias is in the DATA/labels, not a coding error
The synthetic dataset bakes bias into historical labels, and the model just learns it.
- **Why:** The most important and most-missed point: an unbiased algorithm on biased
  data produces a biased model. Framing it this way (vs. "the model is broken")
  connects to Module 03's "garbage in, garbage out" and correctly locates the
  problem — and therefore the fix — outside the model code.

## Decision 3 — Show that "drop the sensitive feature" fails
We explicitly invite the student to remove the group column and re-audit.
- **Why:** "Fairness through unawareness" is the intuitive fix everyone reaches for,
  and it usually doesn't work because of proxy features. Letting the student *see*
  the gap persist prevents a common, confident mistake.

## Decision 4 — Teach the impossibility result, not a false resolution
`fairness_metrics.py` demonstrates that the three definitions conflict.
- **Why:** The honest, defensible position is that fairness requires a *choice*, not
  that there's one correct metric. Teaching the impossibility theorem equips the
  student to make and justify that choice — which is what rigor looks like in a
  fairness analysis and what a committee will probe.

## Decision 5 — Ship reference docs, not just scripts
`alignment_notes.md` and `red_team_checklist.md` are first-class module files.
- **Why:** Safety/alignment is broader than any single script. A map (alignment
  notes) plus a reusable tool (red-team checklist) gives the student durable
  references to return to, and models good practice: document your risk reasoning.

## Decision 6 — Frame everything through the security lens
Bias audit as subgroup testing; red-team checklist as threat modeling; safety as
adversarial ML + prompt injection + evals.
- **Why:** This student is a cybersecurity PhD. Mapping responsible-AI onto threat
  modeling they already do (a) makes it click immediately, (b) reveals the
  AI/security research border as *their* territory, and (c) turns an "ethics
  requirement" into a research opportunity.

## What we left out
- **Law & regulation specifics** (GDPR, EU AI Act, sectoral rules) — important and
  jurisdiction-dependent; named in the checklist, not drilled, because it dates fast
  and varies by region.
- **Formal causal-fairness methods** — a deeper, worthwhile branch; the module stays
  at observational metrics so the core intuition lands first.
- **Philosophical ethics** — utilitarian/deontological framing is valuable but out of
  scope for a hands-on module; the practical "who is harmed and how would I know"
  framing carries the weight here.
