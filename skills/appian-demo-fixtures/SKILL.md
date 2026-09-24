---
name: appian-demo-fixtures
description: "Generate realistic test documents and sample data that match an Appian demo's record types. Use for invoices, PDFs, emails, CSVs, or Doc Center uploads."
---

# Appian demo fixtures

Use when the site exists but grids, Doc Center, or processes have nothing believable to chew on.

## Workflow

1. Read `demos/<slug>/brief.md` and `objects.json`. List the record fields the documents must populate.
2. Choose kinds from `references/fixture-kinds.md`. Default to the fewest files that still make the success moment true.
3. Generate files under `demos/<slug>/fixtures/`. Names: `<slug>-<kind>-<id>.<ext>`.
4. Write `fixtures/manifest.json`: file → target record type / folder / expected extracted fields.
5. Upload via Appian document / folder MCP tools when the demo reads from Appian, not from disk.
6. Confirm one row (or one document) is visible in the site before calling fixtures done.

## Rules

- Invented people are obviously fake (Sarah Johnson, 株式会社サンプル). Never real customer PII.
- Amounts, dates, and IDs must be internally consistent across files that the process will reconcile.
- Language matches the brief (Japanese documents for Japanese-primary stories).
- Prefer real file types the platform will parse (PDF, DOCX, XLSX, EML). A renamed TXT is not a fixture.
- If extraction is in scope, include one messy document (stamp, scan-like PDF) so the happy path is not the only path.
