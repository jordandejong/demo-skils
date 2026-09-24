#!/usr/bin/env python3
"""Load capture login env. --check prints url/username/password_set only."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[3]
KEYS = ("LCP_URL", "LCP_USERNAME", "LCP_PASSWORD")
ALIASES = {
    "LCP_URL": "APPIAN_URL",
    "LCP_USERNAME": "APPIAN_USERNAME",
    "LCP_PASSWORD": "APPIAN_PASSWORD",
}


def _parse_env_file(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        out[k.strip()] = v.strip().strip("'").strip('"')
    return out


def load(slug: str | None = None) -> dict[str, str]:
    merged: dict[str, str] = {}
    merged.update(_parse_env_file(PACK_ROOT / ".env"))
    if slug:
        merged.update(_parse_env_file(PACK_ROOT / "demos" / slug / ".env"))
    for k in list(KEYS) + list(ALIASES.values()):
        if os.environ.get(k):
            merged[k] = os.environ[k]
    creds = {}
    for k in KEYS:
        creds[k] = merged.get(k) or merged.get(ALIASES[k]) or ""
    return creds


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", default=None)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    creds = load(args.slug)
    if not args.check:
        raise SystemExit("refusing to print secrets; use --check")
    print(
        json.dumps(
            {
                "ok": all(creds[k] for k in KEYS),
                "url": creds["LCP_URL"],
                "username": creds["LCP_USERNAME"],
                "password_set": bool(creds["LCP_PASSWORD"]),
            }
        )
    )


if __name__ == "__main__":
    main()
