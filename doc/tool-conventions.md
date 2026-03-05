# Tool Authoring Conventions

Each tool is a single self-contained HTML file in `tools/<name>.html`.

## File Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tool Name</title>
  <meta name="description" content="One-line description of what the tool does">
  <style>/* inline styles — use the color palette below */</style>
</head>
<body>
  <!-- markup -->
  <script>/* inline JS */</script>
</body>
</html>
```

## Rules

- **All JS and CSS must be inline** — no external files at runtime. Tools must work via `file://`.
- **No hard backend dependency** — if a tool requires the CORS proxy, detect its absence and show a clear warning. Never silently fail.
- **No frameworks required** — CDN libraries are acceptable for complex tools (e.g., highlight.js). Always include `integrity` and `crossorigin` attributes on CDN `<script>` tags.
- **Register in `tools.json`** — every new tool needs an entry. See [tools-json.md](tools-json.md).
- **Test file:// first** — before committing, open the file directly in a browser without the backend running.

## Dark-Mode Color Palette

Copy this `:root` block verbatim into each tool's `<style>`:

```css
:root {
  --bg:         #1e1e2e;
  --surface:    #2a2a3d;
  --accent:     #7c6af7;
  --text:       #cdd6f4;
  --text-muted: #6c7086;
  --border:     #313244;
  --success:    #a6e3a1;
  --error:      #f38ba8;
}
```

| Role       | Variable       | Value     |
|------------|----------------|-----------|
| Background | `--bg`         | `#1e1e2e` |
| Surface    | `--surface`    | `#2a2a3d` |
| Accent     | `--accent`     | `#7c6af7` |
| Text       | `--text`       | `#cdd6f4` |
| Muted text | `--text-muted` | `#6c7086` |
| Border     | `--border`     | `#313244` |
| Success    | `--success`    | `#a6e3a1` |
| Error      | `--error`      | `#f38ba8` |

## Standard UI Patterns

- **Header** — `<header>` with a `← back` link to `/` and an `<h1>` with the tool name.
- **Toolbar** — primary action buttons (accent background), secondary buttons (surface background + border).
- **Status line** — a small `<div class="status">` below controls; add class `ok` or `err` for color.
- **Textareas** — monospace font, surface background, focus outline uses `--accent`.
- **Proxy warning** — a banner with `--error` border, hidden by default, shown when backend is unreachable.
