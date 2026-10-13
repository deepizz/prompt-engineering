"""Entry point for the Travel Planner AI CrewAI project.

Running `crewai run` (or `python -m travel_planner.main`) executes the
`run()` function below, which collects the traveler's preferences,
kicks off the crew, and prints/saves the generated Markdown itinerary.
"""

import os
import sys
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv

# Load environment variables from a .env file in the project root
# before anything else needs GROQ_API_KEY.
load_dotenv()

# --- Workaround for a known CrewAI bug (crewAI issue #5886) ---------------
# Recent CrewAI versions tag outgoing messages with a "cache_breakpoint"
# field to support Anthropic-style prompt caching, but only strip that
# field for the Anthropic provider before sending the request. Non-native
# providers routed through LiteLLM (including Groq) receive the raw field
# and reject the request with:
#   GroqException - property 'cache_breakpoint' is unsupported
# Since Groq does not support this caching mechanism, we make the tagging
# function a no-op so no such field is ever added to outgoing messages.
# This is safe to remove once the upstream bug is fixed.
try:
    import crewai.llms.cache as _crewai_cache

    _crewai_cache.mark_cache_breakpoint = lambda msg: msg
except (ImportError, AttributeError):
    # Older/newer CrewAI versions that don't have this module/function
    # simply don't need the workaround.
    pass
# ---------------------------------------------------------------------------

from travel_planner.crew import TravelPlannerCrew


def _default_inputs() -> Dict[str, Any]:
    """Return a sensible default set of trip inputs.

    These defaults are used when the crew is run non-interactively
    (for example, via `crewai run` without a terminal attached, or via
    `train`/`test`/`replay` commands), and match the example given in
    the project specification.
    """
    return {
        "source": "Chennai",
        "destination": "Ooty",
        "days": "3",
        "budget": "15000",
        "travel_style": "Budget",
        "interests": "Nature, Photography",
    }


def _collect_inputs() -> Dict[str, Any]:
    """Interactively collect trip inputs from the user, when possible.

    Falls back to `_default_inputs()` if the process is not attached
    to an interactive terminal (stdin is not a TTY), which keeps
    `crewai run` working in non-interactive environments such as CI.
    """
    if not sys.stdin.isatty():
        return _default_inputs()

    defaults = _default_inputs()
    print("=== Travel Planner AI ===")
    print("Press Enter to accept the default shown in brackets.\n")

    def ask(prompt: str, key: str) -> str:
        value = input(f"{prompt} [{defaults[key]}]: ").strip()
        return value if value else defaults[key]

    return {
        "source": ask("Source location", "source"),
        "destination": ask("Destination", "destination"),
        "days": ask("Number of days", "days"),
        "budget": ask("Budget", "budget"),
        "travel_style": ask("Travel style (e.g. Budget, Luxury, Backpacking)", "travel_style"),
        "interests": ask("Interests (comma separated)", "interests"),
    }


def run() -> None:
    """Run the Travel Planner crew and save the resulting Markdown plan.

    This is the function invoked by `crewai run`.
    """
    inputs = _collect_inputs()

    # Ensure the output directory referenced by tasks.yaml exists.
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    crew_instance = TravelPlannerCrew().crew()
    result = crew_instance.kickoff(inputs=inputs)

    print("\n=== Generated Travel Plan ===\n")
    print(result.raw)
    print(f"\nSaved to: {output_dir / 'travel_plan.md'}")


def train() -> None:
    """Train the crew for a given number of iterations.

    Usage: `crewai train <n_iterations> <output_file>`
    """
    inputs = _default_inputs()
    n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    filename = sys.argv[2] if len(sys.argv) > 2 else "training_output.pkl"

    try:
        TravelPlannerCrew().crew().train(
            n_iterations=n_iterations, filename=filename, inputs=inputs
        )
    except Exception as exc:  # noqa: BLE001 - surface a clear CLI error
        raise RuntimeError(f"An error occurred while training the crew: {exc}") from exc


def replay() -> None:
    """Replay the crew execution from a specific task.

    Usage: `crewai replay <task_id>`
    """
    if len(sys.argv) < 2:
        raise ValueError("Please provide a task_id to replay from.")

    task_id = sys.argv[1]
    try:
        TravelPlannerCrew().crew().replay(task_id=task_id)
    except Exception as exc:  # noqa: BLE001 - surface a clear CLI error
        raise RuntimeError(f"An error occurred while replaying the crew: {exc}") from exc


def test() -> None:
    """Test the crew execution and evaluate performance.

    Usage: `crewai test <n_iterations> <eval_llm>`
    """
    inputs = _default_inputs()
    n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    eval_llm = sys.argv[2] if len(sys.argv) > 2 else os.environ.get(
        "MODEL", "groq/llama-3.3-70b-versatile"
    )

    try:
        TravelPlannerCrew().crew().test(
            n_iterations=n_iterations, eval_llm=eval_llm, inputs=inputs
        )
    except Exception as exc:  # noqa: BLE001 - surface a clear CLI error
        raise RuntimeError(f"An error occurred while testing the crew: {exc}") from exc


if __name__ == "__main__":
    run()
