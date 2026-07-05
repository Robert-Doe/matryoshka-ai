"""
tiny_agent.py  —  Module 10

An AGENT is an LLM that can take ACTIONS by calling tools you give it, in a loop,
until the task is done. The loop:

    1. Send the question + the list of available tools to the model.
    2. If the model asks to use a tool, YOU run it and send the result back.
    3. Repeat until the model gives a final answer instead of a tool call.

We give the model two tools — a safe calculator and a fake "user lookup" — and
watch it decide which to call. This manual loop is the foundation of every agent
framework; understanding it means no agent library is a black box.

Run:  python module_10_genai/tiny_agent.py "What is 17 * 23, and what is Alice's role?"
(Requires:  pip install anthropic  + ANTHROPIC_API_KEY)
"""

import os
import sys

MODEL = os.environ.get("MODEL", "claude-opus-4-8")

# ---- The tools the agent can call. Each is just a Python function. ----
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression safely (digits and + - * / . () only)."""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "Error: only basic arithmetic is allowed."
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Error: {e}"

FAKE_DIRECTORY = {"alice": "Security Engineer", "bob": "PhD Student", "carol": "Admin"}
def lookup_user(name: str) -> str:
    """Look up a person's role in the (pretend) company directory."""
    return FAKE_DIRECTORY.get(name.lower(), f"No user named {name} found.")

# ---- Tool SCHEMAS the model sees (name, description, JSON input shape). ----
TOOLS = [
    {"name": "calculator", "description": "Evaluate a basic arithmetic expression.",
     "input_schema": {"type": "object",
        "properties": {"expression": {"type": "string", "description": "e.g. '17 * 23'"}},
        "required": ["expression"]}},
    {"name": "lookup_user", "description": "Get a person's job role from the directory.",
     "input_schema": {"type": "object",
        "properties": {"name": {"type": "string", "description": "first name"}},
        "required": ["name"]}},
]
DISPATCH = {"calculator": calculator, "lookup_user": lookup_user}


def main():
    task = " ".join(sys.argv[1:]) or "What is 17 * 23, and what is Alice's role?"
    print(f"Task: {task}\n")

    try:
        import anthropic
    except ImportError:
        print("Run:  pip install anthropic"); return 0
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY first (see call_claude.py)."); return 0

    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": task}]

    # THE AGENT LOOP.
    for step in range(6):   # cap iterations so a confused agent can't loop forever
        response = client.messages.create(
            model=MODEL, max_tokens=1024, tools=TOOLS, messages=messages)

        if response.stop_reason != "tool_use":
            # No tool requested -> the model has its final answer.
            answer = "".join(b.text for b in response.content if b.type == "text")
            print("Final answer:", answer)
            break

        # The model asked to use one or more tools. Run them and feed results back.
        messages.append({"role": "assistant", "content": response.content})
        results = []
        for block in response.content:
            if block.type == "tool_use":
                out = DISPATCH[block.name](**block.input)
                print(f"  [agent called {block.name}({block.input}) -> {out}]")
                results.append({"type": "tool_result",
                                "tool_use_id": block.id, "content": out})
        messages.append({"role": "user", "content": results})
    else:
        print("Stopped after 6 steps (safety cap).")

    print("\nThat's an agent: the model REASONED about which tool to use, you EXECUTED")
    print("it, and the loop continued until it could answer. Real agents add more tools")
    print("(web, code, files) and safety checks around each action.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
