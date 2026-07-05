# Module 11 — Project: Audit Your Own Model

**Goal:** Turn the audit tools on YOUR own work. Take a model you built earlier in the
course, find a bias in it, choose and justify a fairness criterion, and propose a
mitigation — the exact structure of a responsible-AI section in a paper or a model
review.

**Time:** ~90 min. **Deliverable:** `audit.py` + `audit_report.md` (the write-up).

---

## Pick a target

Choose one of your earlier models and give it a sensitive attribute to audit against:

- **Module 04/06** — the classifiers. Use a dataset with a group attribute (the
  Module 03 login data has `country`; or use scikit-learn's `fetch_openml("adult")`
  income data, which has `sex` and `race`).
- **Module 09** — your CNN. Audit accuracy across digit classes, or across a
  synthetic "group" you assign.

If you don't have a natural sensitive attribute, `fetch_openml("adult", version=2)`
is the standard fairness benchmark (predict income; audit across `sex`).

---

## Do the audit (adapt `bias_audit.py`)

1. **Overall metrics.** Report overall accuracy — the number that looks fine.
2. **Per-group breakdown.** For each group, report accuracy, positive-prediction rate,
   and false-negative (or false-positive) rate. Where's the gap?
3. **Proxy check.** Remove the sensitive attribute and re-audit. Does the disparity
   persist? (It usually does — explain why.)
4. **Fairness metrics.** Compute demographic parity, equal opportunity, and predictive
   parity across the groups (adapt `fairness_metrics.py`). Which pass, which fail?

## Write the report (`audit_report.md`)

Structure it like a paper's ethics section:

1. **System & context** — what the model does, who could be harmed, cost of errors.
2. **Findings** — the overall vs. per-group numbers; the gap, stated plainly.
3. **Fairness choice** — which definition you'd optimize for THIS decision, and *why*
   (tie it to the cost of a false rejection vs. a false approval).
4. **Mitigation** — at least one concrete option (reweighting, resampling, a fairness
   constraint, better data collection, threshold-per-group, or "don't deploy") and its
   trade-offs (fairness usually costs some accuracy — quantify it if you can).
5. **Limitations** — what you did NOT test, honestly.

---

## Mastery checklist
- [ ] You produced overall AND per-group metrics for a real model.
- [ ] You demonstrated the proxy effect (removing the attribute didn't fix it) or
      explained why it didn't apply.
- [ ] You chose a fairness definition and justified it with a cost argument.
- [ ] You proposed a concrete mitigation and named its trade-off.
- [ ] Your report has an honest "limitations" section.

## Stretch (dissertation-adjacent)
Actually implement one mitigation (e.g. reweight training samples, or set
group-specific decision thresholds) and measure the result: how much did the fairness
gap shrink, and what did it cost in overall accuracy? Plot the trade-off. Then, wearing
your security hat, add a paragraph: could an adversary *exploit* your fairness
intervention (e.g. game group-specific thresholds, or poison the data to shift the
measured base rates)? That intersection — adversarial attacks on fairness mechanisms —
is genuinely under-explored and squarely in your research lane.

**Next module:** `../module_12_capstone/headfirst.md` — put it all together and ship.
