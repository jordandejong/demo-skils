# Pipeline and artifact contract

Root: `demos/<slug>/` next to this pack, or a path the user names.

```
demos/<slug>/
  brief.md
  objects.json          # names + UUIDs returned by MCP — never invented
  build-log.md
  fixtures/             # generated documents + a manifest
  script.md
  storyboard.md          # mermaid audience journey; same scenes as script.md
  capture/
    scenes.json          # one entry per tell/show/tell (+ DO)
    shots/              # 01.png …
    narration/          # 01.wav …
    walkthrough.mp4
  delivery/
    email.md
```

`<slug>`: lowercase, hyphenated, customer-or-story (`tokyo-gas-payments`, `appian101-hr`).

## Stage gates

| After | Ready when |
|---|---|
| Grill | User answered the frontier (audience, success moment, environment, language, runtime, documents?) |
| Brief | Those answers plus in/out and personas are in `brief.md`; user said the understanding is shared |
| Build | Site URL loads; `objects.json` has UUIDs for every object the script will touch |
| Fixtures | Manifest maps each file to a record type / field; a sample row is visible in the site |
| Script | Every scene is tell / show / tell; DO is click-level; preflight is checked |
| Capture | User said "record"; video plays with voiceover in the brief's language |
| Deliver | Draft exists; send only if the user says send in this session |

## Failure policy

- MCP create failed → fix from the error, do not invent a workaround object name.
- Fixture does not round-trip into a record → regenerate; do not demo on empty grids.
- Script scene has no selector or URL → not automation-ready; rewrite before capture.
- Recording drifted from the script → recut that scene; do not ad-lib in the mailed video.
