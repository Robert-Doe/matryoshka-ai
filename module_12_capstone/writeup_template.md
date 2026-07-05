# <Your Project Title>

**Author:** <you> · **Track:** A (ML) / B (Vision) / C (LLM) · **Date:** <date>

> Fill this in *as you work*, not at the end. It keeps you honest and turns your code
> into a project someone else can understand and trust. Delete the italic prompts as
> you replace them.

---

## 1. Problem & motivation
*What are you predicting or building? Why does it matter? Who would use it, and what's
the cost of the model being wrong?*

## 2. Success criteria (defined before modeling)
*What metric decides success, and what's the bar? (e.g. "recall ≥ 0.8 on the attack
class, beating the majority-class baseline of X.") State the baseline here.*

## 3. Data
- **Source:** *where it came from / how you generated it.*
- **Size & shape:** *rows, features, classes.*
- **Class balance:** *the split — and why it matters for your metric choice.*
- **Cleaning:** *what problems you found and how you handled them.*
- **Leakage check:** *how you ensured no test info leaked into training.*

## 4. Method
- **Model(s):** *what you used and why (why the simplest-thing-that-works).*
- **Features / preprocessing:** *engineering, scaling, tokenization/embedding, etc.*
- **Training / validation setup:** *split or CV, seeds, key hyperparameters.*

## 5. Results
*Report against the baseline. Use the RIGHT metric. Include the spread (mean ± std) if
you cross-validated. Put your key figure/table here.*

| Model | Metric (name it) | Baseline | Notes |
|-------|------------------|----------|-------|
| baseline | | — | |
| your model | | | |

**Failure analysis:** *where does it go wrong, and why? (confusion matrix, error
cases, hardest inputs).*

## 6. Ethics, bias & safety
*The required responsible-AI component. For your track:*
- *Track A: bias audit across a sensitive attribute — the gap you found, the fairness
  definition you'd choose and why.*
- *Track B: adversarial robustness — attack success rate, and your defense's effect.*
- *Track C: prompt-injection test — what happened, and your defense.*

*Identify at least one concrete harm/risk and its trade-offs.*

## 7. Limitations
*What you did NOT test or handle, honestly. What would break this in the real world?*

## 8. What I'd do next
*The obvious next steps if you had more time — and, if relevant, how this connects to
your research.*

## 9. How to run
```bash
# from a clean checkout
pip install -r requirements.txt
python main.py            # or the entry point
```
*State any data download step, the expected runtime, and where results are written.*

---

### Self-assessment (from evaluation_rubric.md)
*Score yourself honestly, section by section. Note where you'd lose points and why —
this reflection is itself part of the learning.*
