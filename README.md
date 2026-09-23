# nyansapo-ai

I kept running into two kinds of AI material and hating both of them. One kind stays theoretical forever, all diagrams and vocabulary, and you finish it without being able to write a single line of code. The other throws you straight into a framework before you understand what that framework is quietly doing on your behalf, and you end up able to call `.fit()` without knowing what fitting even means. I built this course to be neither.

The name comes from Nyansapo, the Adinkra "wisdom knot" symbol from my own Akan heritage: wisdom, ingenuity, intelligence, and patience, all tied into one knot that only the patient hands can untie. That's the whole course in one image. AI isn't one flat subject, it's several layers tied together, and you only get to real understanding by untying them one at a time instead of yanking on the knot.

```
Artificial Intelligence
  └── Machine Learning        (systems that LEARN patterns from data)
        └── Deep Learning      (ML using many-layered neural networks)
              └── Generative AI / LLMs  (models that GENERATE text, images, code)
```

The only real way to understand that stack is to walk down through it one layer at a time, writing and running actual code at every single layer instead of just reading about the layer above it. Every module ships working Python you run yourself, plus a small hands-on project that forces you to prove you actually understood the concept rather than just recognized it when you saw it again.

Each module follows the same shape on purpose, so you always know where to look:

| File | Purpose |
|---|---|
| `headfirst.md` | Plain-English, intuition-first primer, read this one first |
| `tutorial.html` | The full styled walkthrough with diagrams and worked examples |
| `decisions.md` | Why the module teaches what it teaches, and what trade-offs I made |
| `*.py` / `*.ipynb` | The actual code you run and modify |
| `project.md` | The hands-on project that makes the concept stick |

## Module map

| # | Module | Layer | What you build |
|---|---|---|---|
| 01 | `module_01_setup` | Foundations | A working Python/AI toolchain; internalize the AI contains ML contains DL contains GenAI hierarchy; classify 12 real systems by which layer they actually live in |
| 02 | `module_02_math` | Foundations | Vectors, dot products, probability, and gradients; implement mean, variance, and normalization from scratch and match NumPy to 6 decimal places |
| 03 | `module_03_data` | Foundations | Clean a genuinely messy CSV (missing values, bad types, outliers) into a model-ready dataset with supporting plots |
| 04 | `module_04_supervised` | ML core | Linear regression and iris classification; a house-price predictor that beats a baseline, then gets deliberately overfit so you can feel the failure mode yourself |
| 05 | `module_05_unsupervised` | ML core | K-Means and PCA; segment synthetic customers into named clusters and justify your choice of k |
| 06 | `module_06_evaluation` | ML core | Precision, recall, F1, ROC-AUC, cross-validation, the bias-variance trade-off; pick the right metric for an imbalanced dataset |
| 07 | `module_07_neural_nets` | Deep learning | Hand-code a neuron and a two-layer net that learns XOR with zero libraries, then reproduce it in PyTorch and classify MNIST above 97% |
| 08 | `module_08_nlp` | The frontier | Tokenization, embeddings, and a from-scratch bigram language model; understand attention and transformers well enough to explain what an LLM is actually predicting and why |
| 09 | `module_09_vision` | The frontier | Convolution by hand, then a CNN classifier with learned filters visualized and explained |
| 10 | `module_10_genai` | The frontier | LLM APIs, prompt engineering, minimal RAG, a tool-using agent; a chat-with-your-notes app that refuses to answer outside its own documents |
| 11 | `module_11_ethics` | Responsibility | Bias auditing, fairness metrics, alignment and safety; audit an earlier model for disparate performance across a sensitive attribute |
| 12 | `module_12_capstone` | Prove it | Ship a complete, honestly evaluated, ethics-reviewed end-to-end project, your portfolio piece |

## Tech stack

Python 3 with NumPy, pandas, matplotlib/seaborn, and scikit-learn. PyTorch for the neural network modules (07 through 09). The Claude API for the generative AI and LLM module, covering prompting, RAG, and tool use. Jupyter notebooks handle the derivation-heavy modules like linear algebra, backprop, and attention, where seeing the math run step by step actually matters.

## Where this stands

Done. All 12 modules are scaffolded with a tutorial, a decisions log, working code, and a project brief. This is coursework as codebase. Every module is meant to be run, not just read.

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

Or just run `make setup && make check` on macOS/Linux, or `run.bat` on Windows.

Start at `module_01_setup/headfirst.md` and work down the stack in order. Each module assumes you already have the code and concepts from the ones before it.
