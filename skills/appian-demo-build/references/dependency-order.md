# Demo object order

Create in this order. Later objects reference earlier UUIDs from `objects.json`.

1. Application (default groups + folders)
2. Extra groups / folders
3. Constants
4. Record types + fields
5. Record type relationships (both directions)
6. Expression rules (validated)
7. Interfaces (validated, then `testInterface` on hidden branches)
8. Process models
9. Record actions, views, user filters
10. Site + pages
11. Documents uploaded to folders (usually the fixtures skill)

Skip a step only when discovery shows it already exists.

## Environment notes

- Use whichever Appian Dev MCP server the user already has configured. Do not hard-code cloud hostnames in this pack.
- Credentials live in the agent's MCP config or a local gitignored `.env`, not in git.
- Site path pattern: `https://<host>/suite/sites/<site-web-address>`
