"""
rag_minimal.py  —  Module 10

RAG = Retrieval-Augmented Generation. The idea: an LLM only knows what it was
trained on. To make it answer questions about YOUR documents (that it never saw),
you (1) RETRIEVE the most relevant chunks of your text, then (2) hand them to the
model and tell it to answer using ONLY those chunks.

    question --> [retriever: find relevant chunks] --> [LLM: answer from chunks] --> answer

This gives the model private/current knowledge AND grounds it (fewer hallucinations).
We keep retrieval fully local (TF-IDF, from Module 05's toolbox) so the only external
call is the final generation step.

Run:  python module_10_genai/rag_minimal.py "how do I run the lab?"
(Requires:  pip install anthropic scikit-learn  + ANTHROPIC_API_KEY)
"""

import os
import sys

MODEL = os.environ.get("MODEL", "claude-opus-4-8")

# Our tiny "knowledge base" — pretend these are chunks from your own docs.
KNOWLEDGE = [
    "The bob_AI course has 12 modules, from environment setup to a capstone project.",
    "To run the XSS lab, execute 'python lab_server.py' and visit http://localhost:5000.",
    "Module 7 teaches neural networks by building one from scratch in NumPy.",
    "Adversarial examples are tiny input perturbations that fool a neural network.",
    "The capstone project requires an honest evaluation section and an ethics review.",
    "Data poisoning is an attack where an adversary injects malicious training data.",
]


def retrieve(query, k=2):
    """Return the k chunks most similar to the query (TF-IDF + cosine, all local)."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    vec = TfidfVectorizer().fit(KNOWLEDGE + [query])
    doc_vecs = vec.transform(KNOWLEDGE)
    q_vec = vec.transform([query])
    sims = cosine_similarity(q_vec, doc_vecs)[0]
    ranked = sorted(range(len(KNOWLEDGE)), key=lambda i: -sims[i])
    return [(KNOWLEDGE[i], sims[i]) for i in ranked[:k]]


def main():
    query = " ".join(sys.argv[1:]) or "how do I run the lab?"
    print(f"Question: {query}\n")

    # STEP 1 — RETRIEVE (local, no API).
    chunks = retrieve(query, k=2)
    print("Retrieved context (most similar chunks):")
    for text, score in chunks:
        print(f"   [{score:.2f}] {text}")
    print()

    # STEP 2 — GENERATE grounded in those chunks.
    try:
        import anthropic
    except ImportError:
        print("Install to run generation:  pip install anthropic")
        print("(Retrieval above already worked — that's the local half of RAG.)")
        return 0
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY to run the generation step.")
        print("(Retrieval above already worked — that's the local half of RAG.)")
        return 0

    context = "\n".join(f"- {t}" for t, _ in chunks)
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL, max_tokens=300,
        system="Answer the question using ONLY the provided context. If the context "
               "does not contain the answer, say 'I don't have that in my documents.' "
               "Never invent details.",
        messages=[{"role": "user", "content":
            f"Context:\n{context}\n\nQuestion: {query}"}])
    answer = "".join(b.text for b in response.content if b.type == "text")
    print("Grounded answer:")
    print("  ", answer)
    print("\nThat's RAG: the model answered about YOUR docs, using retrieved context,")
    print("and would refuse if the answer weren't there. Swap KNOWLEDGE for your own")
    print("files (your notes, a codebase, papers) and you have 'chat with your data'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
