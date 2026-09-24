# Appian Demo Studio

Repeatable agent pipeline: **brief → Appian Dev MCP build → test documents → demo script → browser recording + TTS → email**.

Skills are Agent Skills (`SKILL.md`); they load in Claude Code and other Agent Skills hosts.

## Skills

| Skill | When to load |
|---|---|
| `appian-demo-studio` | Whole factory, or "run the demo pipeline" |
| `appian-demo-grill` | Thin brief — audience, success moment, env, language |
| `appian-demo-build` | Create/extend the Appian application via Dev MCP |
| `appian-demo-fixtures` | Invoices, PDFs, CSVs, Doc Center files |
| `appian-demo-script` | Timed tell / show / tell script (+ DO for the recorder) |
| `appian-demo-capture` | Playwright (or a local browser) + TTS + email draft |

The vendor **appian** Dev MCP skill is still mandatory before any `create*` / `delete*` on the platform. This pack does not replace it.

## Install

```bash
PACK=/path/to/this-repo/skills
for s in appian-demo-studio appian-demo-grill appian-demo-build appian-demo-fixtures appian-demo-script appian-demo-capture; do
  ln -sfn "$PACK/$s" ~/.claude/skills/$s
done
```

Or copy `skills/*` into `~/.claude/skills/`.

## Monday-morning run

In Claude Code (or pi), with Appian Dev MCP connected to the target site:

> Load appian-demo-studio. Brief: HR onboarding on the target Appian site, 8 minutes, English narration, success moment is the live dashboard with five employees. Run the factory and stop for my review before recording.

Artifacts land locally in `demos/<slug>/` (gitignored). Recording does not start until you approve the script. Email is drafted, not sent.

## Guardrails

- No passwords in `demos/` or git. Do not commit `demos/` or `presentation/`.
- Deletion of Appian objects uses the vendor skill's confirmation workflow.
- Email: draft first; send when the user says send.
