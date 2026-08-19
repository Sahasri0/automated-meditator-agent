# Daily Meditation Agent

Scheduled personalized meditation generator.

Pipeline:
GitHub Actions → LangChain → Gemini Flash → Gemini TTS → Gmail → Apple Shortcut → iPhone

## Setup
1. Fill the three files in `context/`.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run locally with `python -m src.main`.
4. Configure GitHub secrets/variables described in `SETUP.md`.
5. Enable the GitHub Actions workflow.

The GitHub runner does not directly write to iCloud Drive. Gmail is the delivery waypoint; Apple Shortcuts can save the attachment to iCloud Drive and play it.
