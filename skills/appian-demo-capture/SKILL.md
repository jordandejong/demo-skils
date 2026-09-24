---
name: appian-demo-capture
description: "Execute an Appian demo script in a real browser, record it, overlay Edge TTS or Piper voiceover, and draft the delivery email."
---

# Appian demo capture

Use only after the user has reviewed `script.md` and said to record.

Stack notes: `references/capture-stack.md`. Composer: `scripts/compose_walkthrough.py`.

## Workflow

1. Parse `script.md` into `capture/scenes.json` (TELL before/after, SHOW, DO, URL, record flag). Two wavs per scene: `NN-before.wav` and `NN-after.wav`.
2. Load login from pack `.env` (or `demos/<slug>/.env`). Check with `python3 scripts/load_capture_env.py --check --slug <slug>`. Keys: `LCP_URL`, `LCP_USERNAME`, `LCP_PASSWORD` (aliases `APPIAN_*`). If `ok` is false, **stop** and say copy `.env.example` → `.env` — do not wait for an interactive login (must work from a phone).
3. Log in **before** the camera starts. Never type the password into a recorded page; never echo it.
4. Drive the browser. From a phone / no display: Playwright `channel: "chrome"` **headless** + `recordVideo` 1920×1080. Headed Chrome only when a display exists *and* the story needs the PDF viewer.
5. Synthesize **all** TELL wavs first (local TTS HTTP endpoint; see `references/capture-stack.md`). Know each duration before the camera starts.
6. **Scene clock — no fixed `sleep(14000)` for Copilot.** Per `record: yes` scene:
   1. Cue `NN-before` at video time `t`. Start DO in the same breath.
   2. Wait for the SHOW selector (new Copilot bubble, Extract fields, Generate again, PDF). **Cap 12 s**, then recover per script. Never a hardcoded 14–18 s pad.
   3. One snapshot: SHOW matches? If not, stop that scene.
   4. If `NN-before` is still playing, wait only the **remainder**. The instant it ends (or already ended), cue `NN-after` and wait **exactly** that wav — then next scene. No extra hold.
   Dead air = time with no TELL and no motion. The only wait without voice is SHOW not ready yet *and* before-wav already finished — keep that gap tiny by waiting on the selector, not the clock.
7. Mux from `cues.json` (each wav `adelay`'d to `start_sec`). Stills fallback only: `scripts/compose_walkthrough.py`.
8. Draft email from `assets/email.template.md`. **Do not send** until the user says send.

## Rules

- Script is the source of truth. Do not improvise extra screens in the mailed video.
- Re-snapshot after every navigation. Click visible labels from the script, not guessed CSS.
- Settled SHOW is for TELL (after). Do not mute the load; TELL (before) covers it.
- Never concatenate all wavs onto a completed click-through. That is what desyncs.
- If a DO step fails, stop that scene, recover per the script, recapture that scene only.
- No passwords in git, `demos/`, chat, or the video. Login only from `.env` / env vars, off-camera.
- Capture must be runnable from a phone: no interactive login, no headed-display requirement.
