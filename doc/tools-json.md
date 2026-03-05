# Tool Registry — tools.json

`tools.json` at the project root is the single source of truth for all registered tools.

## Schema

```json
[
  {
    "id": "base64",
    "name": "Base64 Encode/Decode",
    "description": "Encode or decode Base64 values",
    "file": "tools/base64.html",
    "proxy": false
  }
]
```

| Field         | Type     | Description |
|---------------|----------|-------------|
| `id`          | `string` | Unique slug. Must match the HTML filename (e.g. `base64` → `tools/base64.html`). |
| `name`        | `string` | Human-readable display name shown on the landing page. |
| `description` | `string` | One-line description shown on the tool card. |
| `file`        | `string` | Relative path to the HTML file from the project root. |
| `proxy`       | `bool`   | `true` if the tool requires the backend CORS proxy to function. |

## Adding a New Tool

1. Create `tools/<name>.html` following [tool-conventions.md](tool-conventions.md).
2. Add an entry to `tools.json` with all required fields.
3. The landing page (`index.html`) and Flask backend both consume this file automatically — no other changes needed.

## Consumers

- **`index.html`** — fetches `tools.json` client-side to render the tool grid.
- **`app.py`** — reads `tools.json` at startup to build the set of valid tool IDs for route validation.
