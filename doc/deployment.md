# Deployment

## Docker

Build and run the full stack (backend + tools) in a container:

```bash
docker build -t devops-tooling .
docker run -p 5000:5000 devops-tooling
# → http://localhost:5000
```

The `Dockerfile` uses `python:3.12-slim`, copies all project files, installs dependencies, and starts `python app.py` on port 5000.

## GitHub Pages

Tools with `proxy: false` are fully static and can be published to GitHub Pages directly from the repository.

**What gets published**: `index.html`, `tools/`, `static/`, `tools.json`
**What is NOT needed**: `app.py`, `Dockerfile`, `requirements.txt`, `tests/`

### Manual deploy

Push to the `gh-pages` branch or configure GH Pages to serve from the `main` branch root (or a `/docs` folder if preferred).

### Automated deploy (GH Actions)

Create `.github/workflows/pages.yml`:

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deploy.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - id: deploy
        uses: actions/deploy-pages@v4
```

### Limitations on GH Pages

- The Python backend and CORS proxy are **not available** on GH Pages.
- Tools with `proxy: true` will show a warning banner when the backend is unreachable — this is expected behaviour in the GH Pages context.
