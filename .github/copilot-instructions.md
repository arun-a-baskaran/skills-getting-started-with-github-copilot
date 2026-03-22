# GitHub Copilot Agent Instructions for This Workspace

Welcome to the Mergington High School Activities API project! This workspace is designed for hands-on learning with GitHub Copilot, including Copilot Agent Mode, Inline Chat, and Ask Mode. Follow these instructions to maximize your productivity and ensure consistent, high-quality contributions.

---

## Project Overview
- **Backend:** FastAPI app for managing extracurricular activities (see [src/app.py](src/app.py))
- **Frontend:** Simple HTML/CSS/JS (see [src/static/])
- **Docs & Exercises:** Step-by-step Copilot learning ([.github/steps/])

---

## Build & Run
- **Install dependencies:**
  ```
  pip install -r requirements.txt
  ```
- **Run the app:**
  ```
  python src/app.py
  ```
  or use the VS Code debugger (see [src/README.md](src/README.md))
- **Access the site:**
  - Main page: http://localhost:8000/
  - API docs: http://localhost:8000/docs

---

## Testing
- **Test files:** Place backend tests in a `tests/` directory (see Step 4 instructions)
- **Test runner:**
  ```
  pytest
  ```
- **Requirements:** Ensure `pytest` is in [requirements.txt](requirements.txt)

---

## Conventions & Tips
- **Data model:** Activities and participants are stored in-memory (see [src/app.py](src/app.py))
- **Frontend:** Update `src/static/app.js` and `index.html` for UI changes
- **Workflow:**
  - Use Copilot Agent Mode for multi-step tasks (see [step 3](.github/steps/3-step.md))
  - Use Inline Chat for targeted code edits
  - Use Ask Mode for codebase Q&A
- **Link, don’t embed:** Reference docs like [FIBONACCI_DOCUMENTATION.md](FIBONACCI_DOCUMENTATION.md) and [test_calculation_documentation.md](test_calculation_documentation.md) instead of duplicating content

---

## Common Pitfalls
- **Data loss:** All data is in-memory; restarting the server resets activities/participants
- **Duplicate registration:** Ensure students cannot register for the same activity twice (see [step 2](.github/steps/2-step.md))
- **Frontend sync:** After registration, refresh the activity list to reflect changes (see [step 3](.github/steps/3-step.md))

---

## Example Prompts
- "@workspace How do I add a new activity type?"
- "Agent: Add a participants list to each activity card."
- "Plan Agent: Propose a test plan for the FastAPI backend."

---

## Related Docs
- [src/README.md](src/README.md) — API and data model
- [.github/steps/](.github/steps/) — Guided Copilot exercises
- [FIBONACCI_DOCUMENTATION.md](FIBONACCI_DOCUMENTATION.md) — Fibonacci utility docs

---

## Next Steps
- Try the example prompts above
- For advanced customization, see [agent-customization skill](copilot-skill:/agent-customization/SKILL.md)

---

*Edit this file to update workspace agent instructions. For more advanced customizations, create or update `.instructions.md` or `AGENTS.md` as needed.*
