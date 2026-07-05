"""
setup_check.py  —  Module 01

Verifies your environment is ready for the whole course. It never installs
anything; it just LOOKS and tells you what's missing and how to fix it.

Run:  python module_01_setup/setup_check.py
"""

import importlib
import os
import platform
import sys


def _init_colors():
    """Enable ANSI colors on modern Windows; disable them when piped to a file."""
    if not sys.stdout.isatty():
        return False
    if os.name == "nt":
        # Enable virtual-terminal processing so \033[..m works in the console.
        os.system("")  # harmless trick that flips the flag on Windows 10+
    return True


_COLOR = _init_colors()

# (import name, pip name, first used in module)
REQUIRED = [
    ("numpy", "numpy", "M02"),
    ("pandas", "pandas", "M03"),
    ("matplotlib", "matplotlib", "M03"),
    ("sklearn", "scikit-learn", "M04"),
]

# Nice-to-have but not needed until later; we only warn on these.
OPTIONAL = [
    ("jupyter", "jupyter", "M02 (notebooks)"),
    ("torch", "torch", "M07 (deep learning)"),
    ("anthropic", "anthropic", "M10 (LLM API)"),
]

if _COLOR:
    GREEN, RED, YELLOW, DIM, RESET = "\033[92m", "\033[91m", "\033[93m", "\033[2m", "\033[0m"
else:
    GREEN = RED = YELLOW = DIM = RESET = ""


def check_python():
    major, minor = sys.version_info[:2]
    ok = (major, minor) >= (3, 9)
    tag = f"{GREEN}OK{RESET}" if ok else f"{RED}TOO OLD{RESET}"
    print(f"  Python {major}.{minor}  [{tag}]  (need >= 3.9)")
    if not ok:
        print(f"    {YELLOW}Install a newer Python from https://python.org{RESET}")
    return ok


def check_module(import_name, pip_name, where, required=True):
    try:
        mod = importlib.import_module(import_name)
        version = getattr(mod, "__version__", "?")
        print(f"  {import_name:<12} {version:<10} [{GREEN}OK{RESET}]  {DIM}used in {where}{RESET}")
        return True
    except ImportError:
        level = f"{RED}MISSING{RESET}" if required else f"{YELLOW}not yet{RESET}"
        print(f"  {import_name:<12} {'-':<10} [{level}]  {DIM}used in {where}{RESET}")
        if required:
            print(f"    {YELLOW}Fix: pip install {pip_name}{RESET}")
        return not required


def main():
    print("=" * 56)
    print("  bob_AI :: environment check")
    print("=" * 56)
    print(f"  OS: {platform.system()} {platform.release()}")
    print()

    results = [check_python()]
    print()
    print("  Required packages:")
    for import_name, pip_name, where in REQUIRED:
        results.append(check_module(import_name, pip_name, where, required=True))

    print()
    print("  Optional (install when you reach that module):")
    for import_name, pip_name, where in OPTIONAL:
        check_module(import_name, pip_name, where, required=False)

    print()
    print("-" * 56)
    if all(results):
        print(f"  {GREEN}All set! You're ready for Module 01.{RESET}")
        print("  Next: run  python module_01_setup/hello_ai.py")
    else:
        print(f"  {RED}Some required pieces are missing.{RESET}")
        print("  Quick fix:  pip install -r requirements.txt")
    print("-" * 56)
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
