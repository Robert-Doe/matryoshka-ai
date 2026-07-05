"""
prompt_patterns.py  —  Module 10

Prompt engineering is the skill of getting reliable output from an LLM. It's not
magic words — it's a few repeatable PATTERNS. This script demonstrates four you'll
use constantly. Each is a function you can lift into your own code.

Patterns shown:
  1. System prompt     — set role/rules once; steer everything after.
  2. Few-shot          — show examples of the input->output you want.
  3. Structured output — force machine-parseable JSON via a schema.
  4. Grounding         — tell the model to answer ONLY from provided text
                         (and to say "I don't know") — the anti-hallucination move.

Run:  python module_10_genai/prompt_patterns.py
(Requires:  pip install anthropic  + ANTHROPIC_API_KEY)
"""

import json
import os
import sys

MODEL = os.environ.get("MODEL", "claude-opus-4-8")
line = lambda: print("-" * 62)


def get_client():
    try:
        import anthropic
    except ImportError:
        print("Run:  pip install anthropic"); sys.exit(0)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY first (see call_claude.py)."); sys.exit(0)
    return anthropic.Anthropic()


def text_of(response):
    return "".join(b.text for b in response.content if b.type == "text")


def main():
    client = get_client()

    # 1. SYSTEM PROMPT — one instruction that shapes every response.
    print("1) SYSTEM PROMPT — steering the model's persona/rules")
    r = client.messages.create(
        model=MODEL, max_tokens=200,
        system="You are a terse security expert. Answer in one sentence, no fluff.",
        messages=[{"role": "user", "content": "What is XSS?"}])
    print("  ", text_of(r))
    line()

    # 2. FEW-SHOT — teach a format by example instead of by description.
    print("2) FEW-SHOT — classify log severity by showing examples")
    r = client.messages.create(
        model=MODEL, max_tokens=50,
        messages=[{"role": "user", "content":
            "Classify the log line severity as LOW/MED/HIGH.\n"
            "Log: 'user logged in' -> LOW\n"
            "Log: 'failed password for root x5' -> HIGH\n"
            "Log: 'disk usage at 82%' -> MED\n"
            "Log: 'sudo: 3 incorrect password attempts' ->"}])
    print("  ", text_of(r).strip())
    line()

    # 3. STRUCTURED OUTPUT — force JSON matching a schema (parseable, reliable).
    print("3) STRUCTURED OUTPUT — extract fields as JSON via a schema")
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "wants_demo": {"type": "boolean"},
        },
        "required": ["name", "email", "wants_demo"],
        "additionalProperties": False,
    }
    r = client.messages.create(
        model=MODEL, max_tokens=200,
        output_config={"format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content":
            "Extract contact info: Jane Doe (jane@co.com) asked for a product demo."}])
    data = json.loads(text_of(r))
    print("   parsed dict:", data, "->", type(data).__name__)
    line()

    # 4. GROUNDING — answer ONLY from given text; refuse otherwise (anti-hallucination).
    print("4) GROUNDING — force the model to stick to provided facts")
    context = "The lab server runs on port 5000. It has no authentication."
    r = client.messages.create(
        model=MODEL, max_tokens=150,
        system="Answer ONLY using the CONTEXT. If the answer isn't there, say "
               "'Not stated in the context.' Do not use outside knowledge.",
        messages=[{"role": "user", "content":
            f"CONTEXT:\n{context}\n\nQUESTION: What port does the lab server use?"}])
    print("   in-context Q:", text_of(r).strip())
    r = client.messages.create(
        model=MODEL, max_tokens=150,
        system="Answer ONLY using the CONTEXT. If the answer isn't there, say "
               "'Not stated in the context.' Do not use outside knowledge.",
        messages=[{"role": "user", "content":
            f"CONTEXT:\n{context}\n\nQUESTION: Who is the server administrator?"}])
    print("   out-of-context Q:", text_of(r).strip())
    line()
    print("Grounding is the core of RAG (next: rag_minimal.py) and your main defense")
    print("against hallucination — the model's tendency to confidently make things up.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
