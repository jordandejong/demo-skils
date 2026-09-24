---
name: appian-demo-script
description: "Write a timed Appian demo script in tell/show/tell plus a mermaid storyboard.md. Use for live or recorded Appian walkthroughs."
---

# Appian demo script

Use when the site (and fixtures) exist and the user needs a script a human or a browser agent can run.

**Pedamail CLIy is tell / show / tell** — the SE pattern. Frame what they are about to see, show it, then land what it proved. `DO` is not a fourth teaching scene; it is the click list the recorder executes during SHOW.

Quality bar: the Tokyo Gas payments scripts — opening frame, preflight, timed scenes, what to do when a number is challenged.

## Workflow

1. Read brief + `objects.json` + site URL. Walk the live site (or screenshots) before writing.
2. Copy `assets/script.template.md` to `demos/<slug>/script.md`.
3. Copy `assets/storyboard.template.md` to `demos/<slug>/storyboard.md`. Fill mermaid from the same scenes (audience journey, scene anatomy, per-scene board). No extra scenes that are not in the script.
4. One **success moment** in the first two minutes. Everything else supports it.
5. Every scene is tell / show / tell. Spoken lines only inside TELL (no stage directions in the quote).
6. Add `DO` under SHOW: page, control label, value to type. That is what `appian-demo-capture` consumes.
7. Add a recovery line per risky scene ("if the grid is empty, open fixture X").
8. Time the scenes to the brief's runtime. Cut until it fits. Keep storyboard.md in lockstep.

Anatomy, mermaid shapes, anti-patterns: `references/script-anatomy.md`.

## Rules

- Narration language from the brief; screen language may differ — say so in the opening tell.
- Do not invent UI labels. Copy them from the site.
- No "then we could also show…" appendix. Out of scope stays out.
- Mark scenes `record: skip` only for live-only asides; the mailed video must still make sense.
