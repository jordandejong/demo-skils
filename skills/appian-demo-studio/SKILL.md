---
name: appian-demo-studio
description: "End-to-end Appian demo factory: brief, Dev MCP build, test documents, tell/show/tell demo script, browser recording with TTS, email delivery."
---

# Appian Demo Studio

Use when someone wants a **repeatable Appian demo** from brief to mailed recording, or to run this pack as a whole.

Load the matching sibling per stage. Do not paste their workflows into this file.

| Stage | Skill | Output |
|---|---|---|
| 0 Grill | `appian-demo-grill` | decisions; then `brief.md` |
| 1 Brief | this skill | `demos/<slug>/brief.md` |
| 2 Build | `appian-demo-build` | live application + `objects.json` |
| 3 Fixtures | `appian-demo-fixtures` | documents + sample rows |
| 4 Script | `appian-demo-script` | `script.md` + mermaid `storyboard.md` |
| 5 Capture | `appian-demo-capture` | narrated `walkthrough.mp4` + email draft |

Also load the vendor **appian** MCP skill before any Appian `create*` / `update*` / `delete*` call.

## Pipeline

0. If audience, success moment, environment, or language are missing, load `appian-demo-grill` and **stop**. Do not build on a thin brief.
1. Write `assets/brief.template.md` from the grill. User confirms shared understanding.
2. Build on the named site. Persist **real** UUIDs only.
3. Generate fixtures that match those record fields.
4. Write the script and mermaid storyboard. **Human gate:** user reviews script + storyboard + live site before recording.
5. Record, overlay TTS, draft the email. Send only after explicit approval.

Layout, gates, and naming: `references/pipeline.md`.

## Rules

- Named Appian site only (configured MCP server or user-supplied URL). Never write passwords into artifacts.
- Object deletion follows the vendor appian confirmation workflow. Always.
- Do not skip the gate between script and capture.
- One slug per demo; never mix two customers in the same `demos/<slug>/`.
- Do not load the `tdd` or full `grilling` skills for this pack. Demo grill is the small tree in `appian-demo-grill`; Appian MCP is not a red-green seam.
