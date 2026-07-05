# AI Red-Team Checklist

A practical checklist for probing an AI system for harm and failure BEFORE it ships
(or before it ships in your research write-up). Adapted for someone with a security
background — it's a threat-modeling exercise applied to a model instead of a network.

Use it on any model you build in this course (M04, M06, M09) or in your research.
Not every item applies to every system; skip what's irrelevant and justify why.

---

## 0. Scope & threat model (do this first)

- [ ] What is the system's intended use, and what are the out-of-scope uses?
- [ ] Who could be harmed, and how? (Users, third parties, subgroups, society.)
- [ ] Who are the adversaries, and what are their capabilities? (Curious user,
      motivated attacker, insider, another model.)
- [ ] What's the cost of each failure mode? (A wrong movie rec vs. a wrong bail decision.)

## 1. Bias & fairness

- [ ] Have you audited accuracy/error rates **per subgroup**, not just overall?
      (`bias_audit.py`)
- [ ] Which fairness definition did you choose, and why? (`fairness_metrics.py`)
- [ ] Could non-sensitive features act as **proxies** for a protected attribute?
      (Removing the attribute is not enough — test it.)
- [ ] Is the *training data* itself a product of biased historical decisions?
- [ ] Who did you NOT test on? (Missing subgroups in the data = unmeasured risk.)

## 2. Robustness & adversarial inputs

- [ ] Does it hold up on inputs far from the training distribution?
- [ ] Can a small, crafted perturbation flip the output? (Adversarial examples — M09.)
- [ ] Does it fail *safely* (abstain, flag low confidence) or *silently* (confident wrong)?
- [ ] For text/LLM systems: does it resist **prompt injection** from untrusted
      content it processes (documents, tool results, web pages)? (M10)
- [ ] What happens on malformed, empty, or maliciously oversized input?

## 3. Privacy & data leakage

- [ ] Can the model be probed to reveal its training data? (Memorization /
      membership inference — the flip side of overfitting, M04.)
- [ ] Does it emit PII, secrets, or copyrighted content?
- [ ] For RAG/agents: can a user reach documents or tools they shouldn't? (Access
      control on the *retrieval* and *tool* layers, not just the model.)
- [ ] Is sensitive data minimized, and is retention justified and compliant?

## 4. Security of the ML pipeline

- [ ] **Data poisoning:** could an adversary inject crafted training rows to plant a
      backdoor or degrade the model? (M03 — cleaning IS a control.)
- [ ] **Model supply chain:** are pretrained weights, datasets, and dependencies from
      trusted, verified sources?
- [ ] **Model extraction/theft:** can the model be cloned by querying it?
- [ ] For agents: is each tool action **authorized and gated** by risk? Can the model
      be tricked into a dangerous action (confused-deputy)?

## 5. Transparency & accountability

- [ ] Can you explain an individual decision to an affected person? (Interpretability
      trade-off — M04 vs M07.)
- [ ] Is there a documented model card: intended use, limits, evaluation, known risks?
- [ ] Is there a human-in-the-loop / appeal path for consequential decisions?
- [ ] Is it logged and monitored in production for drift and abuse?

## 6. Misuse & dual-use

- [ ] Could the system be repurposed for harm it wasn't intended for?
- [ ] Are there capabilities that warrant access controls, rate limits, or refusal?
- [ ] Have you considered the *societal* effect at scale, not just per-user behavior?

## 7. Sign-off

- [ ] Residual risks are documented and accepted by someone accountable (not hidden).
- [ ] There is a plan to detect and respond to failures after deployment.
- [ ] "Don't deploy" is on the table as a legitimate outcome.

---

## How to use this in a paper or a review

For each applicable item: state what you tested, what you found, and what you did
about it. Unchecked boxes aren't failures — *unexamined* boxes are. A rigorous
"we did not evaluate X because Y, which is a limitation" is worth more than silence.

The security mindset you already have — assume adversaries, enumerate attack
surfaces, defend in depth, and don't trust input — is exactly the mindset this
checklist operationalizes for AI. You're not learning a new discipline; you're
porting one you already have.
