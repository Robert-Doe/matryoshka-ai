"""
call_claude.py  —  Module 10

Your first call to a real LLM. This is the "hello world" of building WITH AI
(as opposed to building AI from scratch, which is what Modules 1-9 did).

Setup (one time):
  1. pip install anthropic
  2. Get an API key from https://console.anthropic.com
  3. Set it:   setx ANTHROPIC_API_KEY "sk-ant-..."   (Windows, then reopen shell)
               export ANTHROPIC_API_KEY="sk-ant-..."  (mac/Linux)

Run:  python module_10_genai/call_claude.py "Explain gradient descent to a 10-year-old"

Cost note: this course defaults to claude-opus-4-8 (most capable). While LEARNING
and running lots of experiments, set  MODEL=claude-haiku-4-5  to spend far less.
"""

import os
import sys

# The model id. Override with the MODEL env var, e.g. MODEL=claude-haiku-4-5
MODEL = os.environ.get("MODEL", "claude-opus-4-8")


def main():
    try:
        import anthropic
    except ImportError:
        print("The 'anthropic' package isn't installed.  Run:  pip install anthropic")
        return 0

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("No ANTHROPIC_API_KEY found in your environment.")
        print("Get one at https://console.anthropic.com, then set it and re-run.")
        print("(This is the only script in the whole course that needs an API key.)")
        return 0

    prompt = " ".join(sys.argv[1:]) or "Explain what an embedding is, in two sentences."
    print(f"Model: {MODEL}")
    print(f"You:   {prompt}\n")

    client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from the environment
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system="You are a patient teacher. Explain clearly and concisely.",
        messages=[{"role": "user", "content": prompt}],
    )

    # response.content is a LIST of blocks; print the text ones.
    text = "".join(block.text for block in response.content if block.type == "text")
    print("Claude:", text)

    # The 'usage' object is how you track cost — tokens in and out.
    u = response.usage
    print(f"\n[tokens: {u.input_tokens} in, {u.output_tokens} out]")
    print("You just used an LLM as a component in your own program. That's the whole")
    print("game in Module 10: the model is an API you send text to and get text back.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
