#!/usr/bin/env python3
"""
Fetch ECS 9.3.0 flat field definitions from GitHub and write tools/ecs-fields.json.

Usage:
    pip install pyyaml requests
    python scripts/build-ecs-fields.py
"""

import json
import sys
from pathlib import Path

import requests
import yaml

ECS_VERSION = "9.3.0"
ECS_FLAT_URL = f"https://raw.githubusercontent.com/elastic/ecs/v{ECS_VERSION}/generated/ecs/ecs_flat.yml"
OUT_PATH = Path(__file__).parent.parent / "tools" / "ecs-fields.json"


def main():
    print(f"Fetching ECS {ECS_VERSION} flat field definitions...")
    resp = requests.get(ECS_FLAT_URL, timeout=30)
    resp.raise_for_status()

    raw = yaml.safe_load(resp.text)

    fields = {}
    for field_name, meta in raw.items():
        entry = {
            "type": meta.get("type", "keyword"),
            "level": meta.get("level", "extended"),
        }
        description = meta.get("short") or meta.get("description", "")
        if description:
            # Ensure single-line, truncated to 120 chars
            entry["description"] = description.replace("\n", " ").strip()[:120]
        example = meta.get("example")
        if example is not None:
            entry["example"] = str(example)
        fields[field_name] = entry

    output = {"version": ECS_VERSION, "fields": fields}

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, separators=(",", ":"))

    print(f"Wrote {len(fields)} fields to {OUT_PATH}")


if __name__ == "__main__":
    main()
