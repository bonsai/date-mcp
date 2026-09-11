# date-mcp

ふたりの時間を、自然言語から探す Semantic Agent。

## Concept

`date-mcp` is an agent-first REST service for discovering intimate, private, or relaxed date options.

- REST only
- semantic natural-language search
- intimacy is an optional signal
- intimate mode activates when the user's outing context passes an intimacy threshold
- lodging/private-stay options may be included as ambiguous semantic categories

## Relationship

- `odekake-mcp`: where to go
- `date-mcp`: what kind of two-person time they want

```text
natural language
      ↓
semantic intent
      ↓
outing options
      ↓
intimacy signal
      ↓
threshold passed?
   ┌──yes──→ intimate workflow
   └──no───→ normal date workflow
```

## Example

```json
POST /search
{
  "query": "明日、五反田で二人でゆっくりできるところ"
}
```

The agent can infer signals such as privacy, quietness, duration, budget, time of day, and distance without requiring users to explicitly say "いちゃいちゃ".

## API

Initial REST surface:

- `POST /search` — semantic search
- `POST /plan` — build a date plan
- `GET /places` — retrieve candidate places
- `GET /places/:id` — retrieve one candidate

## Principle

**曖昧な気持ちは曖昧なまま受け取り、検索可能な意味へ変換する。**

The repository is intentionally agent/workflow-first. MCP can be added as an adapter later; the core remains REST.
