#!/usr/bin/env python3
"""Date planning agent.

Ranks normalized event candidates for an event-centered date.
The event DB is supplied to the agent as a JSONL file; the output is a
compact date-plan JSON suitable for an MCP/tool layer.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_events(path: Path):
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def price_number(value):
    if isinstance(value, (int, float)):
        return int(value)
    digits = "".join(c for c in str(value or "") if c.isdigit())
    return int(digits) if digits else 0


def score(event, target, area="", category="owarai", max_price=5000):
    if event.get("date") != target:
        return -1
    text = " ".join(str(event.get(k, "")) for k in ("title", "type", "category", "venue", "area"))
    score = 0
    if category and category.lower() in text.lower():
        score += 5
    if area and area.lower() in text.lower():
        score += 4
    price = price_number(event.get("price"))
    if price and price <= max_price:
        score += 2
    if price == 0:
        score += 1
    if event.get("start_at"):
        score += 1
    return score


def build(events, target, area="", category="owarai", max_price=5000, limit=5):
    ranked = sorted(
        ((score(e, target, area, category, max_price), e) for e in events),
        key=lambda x: (-x[0], x[1].get("start_at", "")),
    )
    return {
        "kind": "date-plan",
        "date": target,
        "theme": f"{category} date",
        "area": area,
        "max_price": max_price,
        "events": [e for s, e in ranked if s >= 0][:limit],
        "plan": ["meet", "event", "dinner", "walk_or_cafe"],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--events", type=Path, required=True)
    p.add_argument("--date", required=True)
    p.add_argument("--area", default="")
    p.add_argument("--category", default="owarai")
    p.add_argument("--max-price", type=int, default=5000)
    p.add_argument("--output", type=Path, default=Path("data/date-plans.json"))
    args = p.parse_args()
    plan = build(load_events(args.events), args.date, args.area, args.category, args.max_price)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(plan, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
