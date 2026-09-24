---
name: appian-demo-build
description: "Build or extend an Appian demo application and site via Appian Dev MCP. Use when creating record types, interfaces, process models, or sites for a demo."
---

# Appian demo build

Use after a filled brief, when the live Appian objects do not exist yet (or must be extended).

**Mandatory:** load the vendor `appian` skill (Dev MCP domain rules) before any MCP write. That skill owns naming, relationships, UUIDs, validation, and deletion confirmation. This skill only adds *demo* sequencing.

## Workflow

1. Confirm the target Appian site (named Dev MCP server or URL). Use the already-configured MCP server. Never copy passwords into `demos/`.
2. Discover first: list applications, record types, sites. Reuse what exists.
3. Plan in dependency order (see `references/dependency-order.md`).
4. Create objects. After each successful create, append `{name, type, uuid}` to `demos/<slug>/objects.json`.
5. Validate expressions with `validateExpression` before `createInterface` / `createExpressionRule`.
6. Smoke the site URL. Note the URL and login persona in `build-log.md`.

## Demo-specific rules

- Build toward the brief's **success moment**, not a complete product.
- Lookups get real-looking seed rows in the same pass (or hand off to `appian-demo-fixtures`).
- USER fields need the SYSTEM_RECORD_TYPE_USER relationship or names render as plain text.
- No fabricated UUIDs. If a tool did not return one, list the object again and store the real id.
- Japanese-primary demos: labels and seed data in Japanese; keep rule names ASCII.

When the site shows the success moment with sample data, stop and hand off to fixtures/script.
