# Module 10 — DECISIONS

## Decision 1 — Use a real, current LLM API (Anthropic/Claude)
The course calls a production model rather than a local toy.
- **Why:** The skills that matter here — prompting, structured output, RAG,
  agents — only become real against a capable model. A tiny local model would
  teach the plumbing but not the actual behavior (and its failures would be the
  model's weakness, not the pattern's). Claude is this course's default provider.
- **Trade-off:** Requires an API key and costs money. Mitigated by (a) graceful
  no-key fallbacks so nothing crashes, and (b) a `MODEL=claude-haiku-4-5` env
  override so experimentation is cheap.

## Decision 2 — Correct, current SDK usage (no guessing)
Scripts use `client.messages.create(...)`, read `response.content` blocks by
`.type`, use `output_config.format` for JSON, and the manual tool-use loop.
- **Why:** LLM APIs drift fast; stale patterns (e.g. old `output_format`,
  `budget_tokens`) now error. The code follows the current Anthropic SDK exactly so
  it actually runs, and so students learn today's API rather than a deprecated one.
- **Default model `claude-opus-4-8`:** the most capable general model; students can
  downgrade for cost, which is their call, not a default we impose.

## Decision 3 — Retrieval is LOCAL; only generation calls the API
`rag_minimal.py` does TF-IDF retrieval with scikit-learn, then one API call.
- **Why:** It keeps the RAG *concept* front and center (retrieve → ground →
  generate) without a second external dependency (an embeddings endpoint), reuses
  Module 05's cosine similarity so the course compounds, and means the retrieval
  half runs even with no API key. Real systems use vector embeddings; we note that
  and keep the teaching version transparent.

## Decision 4 — The agent is a MANUAL loop, not a framework
`tiny_agent.py` writes the tool-call loop by hand.
- **Why:** Same "no magic" philosophy as Module 07's backprop. Agent frameworks
  hide the loop; writing it once means the student understands (and can debug and
  secure) any framework. It also makes the prompt-injection attack surface concrete —
  you can *see* where untrusted tool output re-enters the model.

## Decision 5 — Security failure modes are first-class content
Hallucination and especially prompt injection are taught, not footnoted.
- **Why:** For a security PhD, the failure modes ARE the research surface.
  Prompt injection sits exactly at the AI/security border and is under-defended;
  framing agents around it turns "cool demo" into "attack surface I can study."

## Decision 6 — Every script degrades gracefully
No key / no package → a clear message and clean exit, never a traceback.
- **Why:** The one module that needs external setup shouldn't punish a student who
  hasn't finished it. They can read the code, run the local parts, and add the key
  when ready.

## What we left out
- **Fine-tuning / RLHF** — how base models become assistants; conceptual only,
  since it needs infrastructure beyond a laptop.
- **Vector databases & embeddings-based retrieval** — the production RAG upgrade;
  named, with TF-IDF as the teaching stand-in.
- **Streaming, caching, batching, cost-optimization** — real production concerns,
  flagged for when the student builds something at scale.
- **Multi-agent orchestration & evaluation harnesses** — advanced; the capstone
  (Module 12) is where a student can pursue them if they choose the LLM track.
