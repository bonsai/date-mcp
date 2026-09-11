# date-workflow

## Definition

**素材を与えると、状況が変化する。**

`date-workflow` は、イベント・場所・店・ルート・時刻・天気・予算・気分などの素材を組み合わせ、現在の状況を更新しながら、次に自然につながる行動を生成する。

```text
素材
 ↓
状況
 ↓
判断
 ↓
次の素材
 ↓
状況変化
 ↓
次の判断
 ↓
時間の流れ
```

## Inputs

- event
- place
- restaurant
- route
- time
- weather
- budget
- mood
- fatigue
- intimacy

## Search sources

Search can begin from either direction:

- event → surrounding places → route → next action
- place → nearby events → route → next action

## Agent judgment

The Agent does not merely rank search results. It evaluates whether candidates fit together as a sequence.

Questions include:

- Does the event fit the available time?
- What becomes possible after it ends?
- Does travel increase or reduce fatigue?
- Is there another enjoyable activity nearby?
- Does the plan naturally continue or end?
- Does the user's stated or inferred intimacy preference affect the next suggestion?

## Example

```text
20:00 event
  ↓
22:15 finish
  ↓
nearby food
  ↓
23:00 still open
  ↓
late-night option
  ↓
fatigue / last train / distance change
  ↓
Agent generates the next possible action
```

The goal is not to force an outcome. The goal is to discover a fun, coherent progression from the available materials.

## Principle

**Search returns points. date-workflow creates the line.**
