# date-mcp

ふたりの時間を、自然言語から探す Semantic Agent。

## Concept

`date-mcp` is an agent-first REST service for discovering date options from natural-language intent.

- REST / agent-first
- semantic natural-language search
- event-centered dates are first-class
- intimacy is an optional signal
- `POST /plan` can compose an outing around an event

## Relationship

- `stage-search`: what is happening / event discovery
- `date-mcp`: what kind of two-person time they want and how to compose it
- `odekake-mcp`: where to go

```text
natural language
      ↓
semantic intent
      ↓
STAGE / event candidates
      ↓
      date-mcp
      ↓
 ┌────┼──────────────┐
 meet event dinner walk/cafe
 └────┴──────────────┘
```

## Date Agent

`scripts/date_agent.py` ranks event candidates by date, area, category and budget and emits a `date-plan` JSON. The implementation was moved here from STAGE-Search so that STAGE-Search remains the event discovery layer while date-mcp owns the date-planning intent. fileciteturn26file0

Example:

```bash
python scripts/date_agent.py \
  --events ../stage-search/data/events.jsonl \
  --date 2026-09-19 \
  --area 新宿 \
  --category owarai \
  --output data/date-plans.json
```

Output contains the selected events plus the planning sequence:

```json
["meet", "event", "dinner", "walk_or_cafe"]
```

## API

Initial REST surface:

- `POST /search` — semantic search
- `POST /plan` — build a date plan
- `GET /places` — retrieve candidate places
- `GET /places/:id` — retrieve one candidate

## Principle

**曖昧な気持ちは曖昧なまま受け取り、検索可能な意味へ変換する。**

`date-mcp` owns the **date intent / planning layer**. Event discovery remains upstream.
