# DevOps Browser Tooling

Browser-based DevOps helper tools — each one a standalone HTML file, no build step required.

## Architecture

1. **Each tool = one HTML file** in `tools/` — all CSS and JS inline, works via `file://` or served.
2. **Optional Python backend** (`app.py`) — serves pages and provides a CORS proxy for tools that call external APIs.
3. **No build step** — no compilation needed. CDN libraries are acceptable for complex tools.
4. **GitHub Pages compatible** — `tools/` and `index.html` can be published as-is; backend is only needed for proxy features.

## Directory Structure

```
tooling/
├── CLAUDE.md
├── app.py              # Flask backend (optional)
├── tools.json          # Tool registry — source of truth for all tools
├── index.html          # Landing page
├── tools/              # One .html file per tool
├── static/             # shared.css, favicon
├── doc/                # Detailed documentation (see below)
├── Dockerfile
├── .envrc              # direnv: layout python3
└── requirements.txt
```

## Documentation

| Topic | File |
|-------|------|
| Writing and styling tools | [doc/tool-conventions.md](doc/tool-conventions.md) |
| tools.json schema and how to register a tool | [doc/tools-json.md](doc/tools-json.md) |
| Flask backend routes and proxy | [doc/backend.md](doc/backend.md) |
| Local dev setup | [doc/dev-setup.md](doc/dev-setup.md) |
| Docker and GitHub Pages deployment | [doc/deployment.md](doc/deployment.md) |

## Quick Start

```bash
direnv allow                  # or: python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py                 # http://localhost:5000
```

To work on a tool without the backend, open it directly: `xdg-open tools/base64.html`
