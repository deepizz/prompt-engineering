# Travel Planner AI

An AI-powered travel planner built with [CrewAI](https://docs.crewai.com/), using
Groq's `llama-3.3-70b-versatile` model as the LLM.

Give it a source, destination, number of days, budget, travel style, and
interests, and it generates a complete Markdown travel plan including:

- Trip Summary
- Daily Itinerary (Morning / Afternoon / Evening for every day)
- Estimated Budget
- Recommended Hotels
- Recommended Attractions
- Local Food Suggestions
- Travel Tips
- Packing Checklist

## Project Structure

```
travel-planner-ai/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
└── src/
    └── travel_planner/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

## Requirements

- Python 3.12+
- A [Groq API key](https://console.groq.com/keys)

## Installation

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
```

### 2. Install dependencies

Install the CrewAI CLI and the project's dependencies:

```bash
pip install crewai
pip install -r requirements.txt
```

Alternatively, install the project itself (which pulls in the same
dependencies via `pyproject.toml`):

```bash
pip install -e .
```

### 3. Create your `.env` file

Copy the example file and add your Groq API key:

```bash
cp .env.example .env
```

Then edit `.env`:

```
GROQ_API_KEY=your_api_key_here
MODEL=groq/llama-3.3-70b-versatile
```

## Running the Project

From the project root, run:

```bash
crewai run
```

If your terminal is interactive, you'll be prompted for:

- Source Location
- Destination
- Number of Days
- Budget
- Travel Style
- Interests

Press Enter on any prompt to accept the default value shown in brackets. In
non-interactive environments, the crew runs automatically using the default
example trip (Chennai → Ooty, 3 days, ₹15,000, Budget, Nature & Photography).

The generated itinerary is printed to the console and saved to:

```
output/travel_plan.md
```

## Example Input

```json
{
  "source": "Chennai",
  "destination": "Ooty",
  "days": "3",
  "budget": "15000",
  "travel_style": "Budget",
  "interests": "Nature, Photography"
}
```

## How It Works

This crew uses **four specialized agents** working in a sequential pipeline,
each one building on the work of the agents before it:

1. **Destination Researcher** — researches attractions, culture/customs,
   and weather/best time to visit for the destination.
2. **Budget & Logistics Planner** — builds a numeric budget breakdown and
   recommends hotels and transport, using the destination research.
3. **Itinerary Planner** — builds the day-by-day (Morning/Afternoon/Evening)
   schedule, using both the research and the budget/logistics plan.
4. **Local Experience Consultant** — adds food recommendations, travel
   tips, and a packing checklist, then compiles everything the team has
   produced into the final, polished Markdown travel plan.

Each task is wired to receive the outputs of the relevant earlier tasks via
CrewAI's `context=` parameter (see `crew.py`), so later agents genuinely
build on earlier agents' work rather than starting from scratch.

- **Agents** (`config/agents.yaml`): role/goal/backstory for each of the
  four agents above, all configured to use Groq's `llama-3.3-70b-versatile`
  model via CrewAI's `LLM` class.
- **Tasks** (`config/tasks.yaml`): the four chained tasks described above;
  the final task's output is saved to `output/travel_plan.md`.
- **Crew** (`crew.py`): assembled with CrewAI's `@CrewBase` class-based
  syntax, agents and tasks linked with explicit `context=` chains, and run
  as a sequential process.
- **Entry point** (`main.py`): collects inputs, loads `.env`, runs the
  crew, and saves the Markdown output — this is what `crewai run` invokes.

## Other CrewAI Commands

```bash
crewai train <n_iterations> <output_file>   # Train the crew
crewai replay <task_id>                     # Replay from a specific task
crewai test <n_iterations> <eval_llm>       # Test and evaluate the crew
```

## Troubleshooting

- **`GROQ_API_KEY is not set`**: make sure you created a `.env` file (not
  just `.env.example`) in the project root and that it contains a valid key.
- **Model errors**: confirm your Groq account has access to
  `llama-3.3-70b-versatile`, or set `MODEL` in `.env` to another Groq model
  you have access to.
- **`ImportError: ... LiteLLM fallback package is not installed`**: Groq is
  not a "native" CrewAI provider, so CrewAI routes the request through
  LiteLLM. Make sure `litellm` is installed — it's included in
  `requirements.txt` and `pyproject.toml`, but if you installed dependencies
  before this was added, run `pip install litellm` (or `pip install -r
  requirements.txt` again) inside your virtual environment.
- **`GroqException - property 'cache_breakpoint' is unsupported`**: this is
  a known upstream CrewAI bug ([crewAI#5886](https://github.com/crewAIInc/crewAI/issues/5886))
  where CrewAI's prompt-caching feature tags messages for Anthropic-style
  caching but doesn't strip the tag for non-Anthropic providers like Groq.
  `main.py` already includes a small workaround (a no-op patch of
  `crewai.llms.cache.mark_cache_breakpoint`) that disables this tagging, so
  it should work out of the box. If you still see this error, make sure
  you're running the `main.py` from this project (not a script that
  bypasses it) and that your installed `crewai` version still exposes
  `crewai.llms.cache`.
