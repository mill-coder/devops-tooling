# Development Setup

## Requirements

- Python 3.11+
- [direnv](https://direnv.net/) (optional but recommended)

## First-time Setup

```bash
# With direnv (recommended)
direnv allow          # creates .venv and activates it automatically

# Without direnv
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Running the Dev Server

```bash
python app.py
# → http://localhost:5000
```

Debug mode is on by default (`FLASK_DEBUG=1`). Set `FLASK_DEBUG=0` to disable.

## Working on Tools Without the Backend

Most tools (`proxy: false`) work by opening the HTML file directly:

```bash
xdg-open tools/base64.html    # Linux
open tools/base64.html         # macOS
```

`index.html` reads `tools.json` relative to itself, so it also works via `file://`.

## Adding a New Tool

1. Copy an existing tool file as a starting point.
2. Follow the conventions in [tool-conventions.md](tool-conventions.md).
3. Register it in `tools.json` — see [tools-json.md](tools-json.md).
4. Verify it works via `file://` before starting the Flask server.
