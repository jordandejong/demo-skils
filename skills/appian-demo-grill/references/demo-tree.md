# Demo design tree

## Round 1 — always (independent)

Ask all of these unless the user already answered in the prompt.

1. **Audience** — role in the room, and what they will challenge (arithmetic, UX, security, AI accuracy).
2. **Success moment** — the single thing that must work on screen in the first two minutes.
3. **Environment** — configured Appian site / URL.
4. **Language** — narration vs screens (`en`, `ja`, or split).
5. **Runtime** — minutes for the mailed video or live run (default under 5).
6. **Documents?** — does SHOW include a PDF/Office viewer? (yes → headed Chrome later).

## Round 2 — unblocked by round 1

Only what now depends on answers:

- If documents: which kinds (invoice, email, exception file) and language.
- If Japanese-primary screens: ASCII rule names, Japanese labels/seed.
- Personas: on-screen user vs narrator vs driver.
- Out of scope: one list, so the script cannot grow a second story.
- Recording: mailed mp4 vs live-only (gates capture).

## Done

Frontier empty → `brief.md` has audience, success moment, environment, language, runtime, document yes/no, in/out. Then wait for "build".
