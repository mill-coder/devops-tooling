# Python Backend

The backend is a minimal Flask app (`app.py`). It is **optional** — tools that don't use the CORS proxy work without it.

## Routes

| Method | Path                 | Description |
|--------|----------------------|-------------|
| `GET`  | `/`                  | Serves `index.html` |
| `GET`  | `/tools.json`        | Serves the tool manifest |
| `GET`  | `/tools/<name>`      | Serves `tools/<name>.html`; returns 404 if not in registry |
| `GET`  | `/tools/<name>.json` | Serves static data files for a tool (allowlist-gated; e.g. `ecs-fields.json`) |
| `POST` | `/proxy`             | CORS proxy — forwards an HTTP request on behalf of the browser |

## CORS Proxy

The proxy accepts a JSON body and forwards the request to the target URL:

```json
{
  "url":     "https://target-host/api/endpoint",
  "method":  "POST",
  "headers": { "Authorization": "Basic ..." },
  "body":    "{\"key\": \"value\"}"
}
```

Response:

```json
{
  "status":  200,
  "headers": { "Content-Type": "application/json" },
  "body":    "..."
}
```

**Security**: The proxy is intended for local development and trusted internal networks only. Do not expose it publicly without adding authentication. Tools should check proxy availability on load and display a warning banner if it is unreachable.

## Conventions

- Keep `app.py` small. No business logic, no templating, no database.
- New routes should not be added without a clear need — prefer client-side solutions.
- The tool registry (`tools.json`) is loaded once at startup. Restart the server after editing it.

## Tests

Backend tests live in `tests/test_proxy.py`. Run with:

```bash
pytest tests/
```

See [dev-setup.md](dev-setup.md) for environment setup.
