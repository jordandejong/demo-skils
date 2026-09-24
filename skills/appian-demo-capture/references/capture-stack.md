# Capture stack

## Auth (`.env`)

Pack root `.env` (gitignored) or `demos/<slug>/.env`. Copy `.env.example`. A local `.env` is the whole secret store for capture.

```
LCP_URL=https://….appiancloud.com
LCP_USERNAME=
LCP_PASSWORD=
```

`python3 scripts/load_capture_env.py --check --slug <slug>` → `{ok, url, username, password_set}` — never prints the password.

Login with those creds, **then** start `recordVideo`. From a phone there is no one at a keyboard and often no display.

## Browser

| Preference | How |
|---|---|
| Playwright | Drive Chrome with the script's visible labels. |
| Playwright MCP | If a browser MCP is configured: navigate → snapshot → click by ref → screenshot. |
| Phone / no display | Playwright `channel: "chrome"` headless + `recordVideo` 1920×1080. Login from `.env` first. |
| Live window | ffmpeg `x11grab` / `pipewire` only if the user asked for a true live capture of an already-open site. |

Work from accessibility snapshots or visible labels, never invented selectors.

## Voice

1. **Edge TTS** (preferred, Microsoft neural) if you run a local proxy: `POST http://127.0.0.1:<port>` `{"text","voice":"en"}` → wav.
2. **Piper** or another local TTS as fallback.
3. Match the brief's narration language. Do not mix voices in one video.

## Timing (scene clock, minimum dead air)

Do **not** record clicks, then slap concatenated TELL wavs on the file. Do **not** `sleep(14)` “for Copilot”.

1. Wavs first (duration known).
2. Cue TELL (before) + DO together.
3. `waitFor` the SHOW selector (new answer, fields, PDF), cap 12 s.
4. Remainder of before-wav only; then TELL (after) immediately; wait exactly that wav; next scene.
5. `cues.json` `{wav, start_sec}` → `adelay` mux.

Dead air left on the table is only: Copilot slower than TELL (before). If that happens often, **lengthen the TELL (before) line**, do not pad silence.

One snapshot per scene. No MCP poll loop.

## Compose

```
python3 scripts/compose_walkthrough.py \
  --shots demos/<slug>/capture/shots \
  --narration demos/<slug>/capture/narration \
  --out demos/<slug>/capture/walkthrough.mp4
```

Settled stills pair with `NN-after.wav`. Load screencast (or previous frame) pairs with `NN-before.wav`. Duration follows audio, no silent pad.

## Email

Draft first (local mail client or API). Attach `capture/walkthrough.mp4`. Send only after explicit approval in the same session.
