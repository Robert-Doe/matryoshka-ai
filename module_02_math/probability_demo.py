"""
probability_demo.py  —  Module 02

Probability is how models express UNCERTAINTY. A classifier doesn't say
"spam" — it says "0.97 probability of spam." Understanding that number, and
how to update it with evidence (Bayes' rule), is core AI literacy.

We build a tiny Naive Bayes spam filter BY HAND — no ML library — because
it's the cleanest possible bridge between probability theory and a real
security tool you already rely on.

Run:  python module_02_math/probability_demo.py
"""

import numpy as np

line = lambda: print("-" * 60)


# ------------------------------------------------------------------ #
# PART 1 — Probability as uncertainty, and Bayes' rule
# ------------------------------------------------------------------ #
# Bayes' rule updates a belief when new evidence arrives:
#
#     P(cause | evidence) = P(evidence | cause) * P(cause) / P(evidence)
#
# The classic security-flavored example: a malware scanner.
print("PART 1 — Bayes' rule: 'the scanner alerted — is this file actually malware?'")

p_malware      = 0.01     # 1% of files are truly malware  (the "prior")
p_alert_if_mal = 0.99     # scanner catches 99% of real malware (true positive)
p_alert_if_ok  = 0.05     # but also alerts on 5% of clean files (false positive)

# Total probability of an alert (malware path + clean path):
p_alert = p_alert_if_mal * p_malware + p_alert_if_ok * (1 - p_malware)
# Bayes: given an alert, probability it's REALLY malware:
p_mal_given_alert = (p_alert_if_mal * p_malware) / p_alert

print(f"   Prior P(malware)            = {p_malware:.2%}")
print(f"   P(malware | scanner alerts) = {p_mal_given_alert:.2%}")
print("   >> Even a 99%-accurate scanner is right only ~17% of the time on an alert,")
print("      because malware is RARE. This 'base rate fallacy' burns security teams")
print("      (alert fatigue) and ML beginners alike. Probability protects you from it.")
line()


# ------------------------------------------------------------------ #
# PART 2 — A Naive Bayes spam filter, built by hand
# ------------------------------------------------------------------ #
print("PART 2 — Train a tiny Naive Bayes spam filter")

# Tiny labeled corpus. (label, text)
train = [
    ("spam", "free money win prize click now"),
    ("spam", "win free cash prize now"),
    ("spam", "click now free bonus money"),
    ("ham",  "meeting tomorrow about the project"),
    ("ham",  "can you review the report today"),
    ("ham",  "lunch tomorrow with the team"),
]

# Count word frequencies per class.
from collections import defaultdict
counts = {"spam": defaultdict(int), "ham": defaultdict(int)}
class_docs = {"spam": 0, "ham": 0}
vocab = set()
for label, text in train:
    class_docs[label] += 1
    for w in text.split():
        counts[label][w] += 1
        vocab.add(w)

total_docs = len(train)
prior = {c: class_docs[c] / total_docs for c in counts}


def word_prob(word, label):
    """P(word | class) with +1 Laplace smoothing so unseen words don't zero it out."""
    total_words = sum(counts[label].values())
    return (counts[label][word] + 1) / (total_words + len(vocab))


def classify(text):
    """Return P(spam | text) using log-probabilities (avoids underflow)."""
    scores = {}
    for c in counts:
        # start from the prior, then add evidence from each word
        logp = np.log(prior[c])
        for w in text.split():
            logp += np.log(word_prob(w, c))
        scores[c] = logp
    # convert two log-scores back to a normalized probability
    m = max(scores.values())
    exp = {c: np.exp(scores[c] - m) for c in scores}
    z = sum(exp.values())
    return exp["spam"] / z


line()
print("PART 3 — Test it on new messages")
tests = [
    "free prize click now",
    "meeting about the report tomorrow",
    "win cash today",
    "can we schedule lunch",
]
for msg in tests:
    p = classify(msg)
    verdict = "SPAM" if p > 0.5 else "ham "
    print(f"   [{verdict}]  P(spam)={p:5.1%}   \"{msg}\"")

print("\n   That's a working classifier from pure probability — no ML framework.")
print("   Real spam filters and many intrusion-detection features are this idea,")
print("   scaled to millions of words. You now understand what's under the hood.")
