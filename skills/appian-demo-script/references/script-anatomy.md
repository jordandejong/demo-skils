# Script anatomy

Tell / show / tell is how a person teaches. DO is how the agent drives the site.

```
# Demo script — <title>
Runtime, presenter, site, language.
Preflight (environment, data, what to decide before going live).
Opening (frame the story; say what is live-calculated vs hardcoded).
Scenes (numbered).
Close + Q&A parking lot.
```

Each scene:

```
## Scene N — <name> (~Xs)
**TELL (before):**
> One or two sentences. Why this screen, what to watch for.
**SHOW:** <page / control in view>
**DO:**
1. Click "<visible label>"
2. Type "<value>" into "<label>"
**TELL (after):**
> What that just proved. Do not re-describe the clicks.
**URL:** <path after /suite/...>
**record:** yes | skip
**if it fails:** <one recovery>
```

Capture: **TELL (before) starts when DO starts** — it covers Appian load/spinners. Do not wait for settle and then talk into a still. **TELL (after)** lands on the settled SHOW. Keep both short enough that a whole recording stays under the brief runtime (default under 5 minutes).

## Storyboard (`storyboard.md`)

Same scenes as `script.md`, drawn in mermaid for sharing (Obsidian / GitHub). Sit it next to the script. Three diagrams from `assets/storyboard.template.md`:

1. Audience journey — opening → numbered capabilities → close (flowchart LR).
2. Scene anatomy — TELL before → DO → SHOW → TELL after (flowchart TB).
3. Per-scene board — DO + proof on screen (flowchart TD).

Obsidian-safe mermaid: `flowchart`, `<br/>` in node labels, no HTML besides that. Do not add a scene that is not in the script. If the script is cut, recut the storyboard.

## Anti-patterns

- TELL that describes clicks ("now I click save") — that belongs in DO. TELL is the business consequence.
- SHOW with no TELL-before — the audience (and the TTS) has no frame.
- Scenes with no SHOW — the recorder cannot aim.
- Hardcoded numbers presented as live calculations.
- Runtime that ignores Q&A (budget it, or it eats the close).
- Dead air: TELL (before) after the page has already loaded. Speak over the load.
