---
name: appian-demo-grill
description: "Grill an Appian demo brief: audience, success moment, environment, language, runtime. Use before building when the brief is thin or assumed."
---

# Appian demo grill

A **minimal** grilling pass, not the full `grilling` skill. Decisions only — look up facts yourself (site URL, existing apps, Appian version).

Do not start `appian-demo-build` until the user confirms shared understanding and `brief.md` is written.

## Shape

Same round format as `grilling`:

```
❓ **Q1** - **<title>**: <body, choices if any>

➡️ <your recommended answer>
```

Ask the **whole current frontier** in one round. Wait. Then the next. Two rounds is the budget; a third only if a success moment is still mushy.

Tree and default questions: `references/demo-tree.md`.

## Rules

- One success moment. If they name three, make them pick.
- Recommended answers are allowed — that is the point of a demo grill.
- Do not ask anything you can discover (MCP list applications, current site language).
- When the frontier is empty, write `demos/<slug>/brief.md` from the template in `appian-demo-studio` and stop. No building in the same breath.
- Do **not** load the `tdd` skill. Appian MCP creates are not a red-green seam; the brief's success moment is the acceptance test.
