# matryoshka-ai

**The AI Foundations Mastery Course — nest by nest, from "what even is AI" to a shipped project.**

## Why this exists

Most "intro to AI" material either stays theoretical forever or throws you into a framework
before you understand what it's hiding from you. This course does neither. It is built on one
idea: AI is a set of nested layers, like a matryoshka doll —

```
Artificial Intelligence
  └── Machine Learning        (systems that LEARN patterns from data)
        └── Deep Learning      (ML using many-layered neural networks)
              └── Generative AI / LLMs  (models that GENERATE text, images, code)
```

— and the way to actually understand that stack is to walk down through it one layer at a
time, writing and running real code at every layer, not just reading about it. Every module
ships working Python you execute yourself, and a small hands-on project that forces you to
prove you understood the concept rather than recognized it.

Each module follows the same shape so you always know where to look:

| File | Purpose |
|---|---|
| `headfirst.md` | Plain-English, intuition-first primer — read this first |
| `tutorial.html` | The full styled walkthrough with diagrams and worked examples |
| `decisions.md` | Why the module teaches what it teaches, and what trade-offs were made |
| `*.py` / `*.ipynb` | The actual code you run and modify |
| `project.md` | The hands-on project that makes the concept stick |

## Module map

| # | Module | Layer | What you build |
|---|---|---|---|
| 01 | `module_01_setup` | Foundations | Working Python/AI toolchain; internalize the AI⊃ML⊃DL⊃GenAI hierarchy; classify 12 real systems by which layer they live in |
| 02 | `module_02_math` | Foundations | Vectors, dot products, probability, and gradients — implement mean/variance/normalization from scratch and match NumPy to 6 decimal places |
| 03 | `module_03_data` | Foundations | Clean a genuinely messy CSV (missing values, bad types, outliers) into a model-ready dataset with supporting plots |
| 04 | `module_04_supervised` | ML core | Linear regression and iris classification; a house-price predictor that beats a baseline, then is deliberately overfit to feel the failure mode |
| 05 | `module_05_unsupervised` | ML core | K-Means and PCA; segment synthetic customers into named clusters and justify the choice of *k* |
| 06 | `module_06_evaluation` | ML core | Precision/recall/F1/ROC-AUC, cross-validation, bias–variance trade-off; pick the right metric for an imbalanced dataset |
| 07 | `module_07_neural_nets` | Deep learning | Hand-code a neuron and a 2-layer net that learns XOR with zero libraries, then reproduce it in PyTorch and classify MNIST at 97%+ |
| 08 | `module_08_nlp` | The frontier | Tokenization, embeddings, and a from-scratch bigram language model; understand attention and transformers well enough to explain what an LLM predicts and why |
| 09 | `module_09_vision` | The frontier | Convolution by hand, then a CNN classifier with learned filters visualized and explained |
| 10 | `module_10_genai` | The frontier | LLM APIs, prompt engineering, minimal RAG, and a tool-using agent; a "chat with your notes" app that refuses to answer outside its documents |
| 11 | `module_11_ethics` | Responsibility | Bias auditing, fairness metrics, alignment and safety; audit an earlier model for disparate performance across a sensitive attribute |
| 12 | `module_12_capstone` | Prove it | Ship a complete, honestly-evaluated, ethics-reviewed end-to-end project — your portfolio piece |

## Tech stack

- **Python 3** with NumPy, pandas, matplotlib/seaborn, scikit-learn
- **PyTorch** for neural networks (modules 07–09)
- **Claude API** for the generative AI / LLM module (prompting, RAG, tool use)
- Jupyter notebooks for the derivation-heavy modules (linear algebra, backprop, attention)

## Status

Complete: all 12 modules scaffolded with tutorial, decisions log, working code, and project brief.
This is coursework-as-codebase — every module is meant to be run, not just read.

## How to run it

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python module_01_setup/setup_check.py
```

```bat
:: Windows
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py module_01_setup\setup_check.py
```

Or simply `make setup && make check` (macOS/Linux) or `run.bat` (Windows).

Start at `module_01_setup/headfirst.md` and work down the stack in order — each module
assumes the code and concepts from the ones before it.
